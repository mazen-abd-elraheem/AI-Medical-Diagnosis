from flask import Flask, render_template, request, url_for, redirect
import sqlite3
import joblib
import pandas as pd
import os
import logging
from Prolog.prolog_engine import prolog_diagnose
from ml_model.text_analyzer import extract_symptoms

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Load ML model with error handling for deployment
def load_ml_model():
    """Load ML model with proper error handling"""
    model_path = os.path.join(os.path.dirname(__file__), 'ml_model', 'symptom_checker.pkl')
    try:
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            logger.info("ML model loaded successfully.")
            return model
        else:
            logger.warning(f"ML model file not found at {model_path}")
            return None
    except Exception as e:
        logger.error("Error loading ML model: %s", e, exc_info=True)
        return None

ml_model = load_ml_model()

def get_db_connection():
    """
    Returns a SQLite connection with thread safety.
    """
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    try:
        conn = sqlite3.connect(db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        logger.debug("Database connection successful!")
        return conn
    except Exception as e:
        logger.error("Database connection error: %s", e, exc_info=True)
        return None

def initialize_data():
    """Initialize data from database with error handling"""
    valid_symptoms = {}
    symptom_descriptions = {}
    disease_names = {}
    disease_categories = {}
    
    try:
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                
                # Load symptoms
                cursor.execute('SELECT id, description FROM symptoms')
                symptoms = cursor.fetchall()
                if symptoms:
                    valid_symptoms = {row['description'].lower(): row['id'] for row in symptoms}
                    symptom_descriptions = {row['description'].lower(): row['description'] for row in symptoms}
                    logger.info(f"Loaded {len(symptoms)} symptoms from database.")
                else:
                    logger.warning("No symptoms found in the database!")

                # Load diseases
                cursor.execute('SELECT id, name, category FROM diseases')
                diseases = cursor.fetchall()
                if diseases:
                    disease_names = {row['id']: row['name'] for row in diseases}
                    disease_categories = {row['id']: row['category'] for row in diseases}
                    logger.info(f"Loaded {len(diseases)} diseases from database.")
                else:
                    logger.warning("No diseases found in the database!")

            except sqlite3.Error as e:
                logger.error(f"Error executing SQL query: {e}", exc_info=True)
        else:
            logger.error("Failed to establish a database connection.")
    except Exception as e:
        logger.error("Error initializing data: %s", e, exc_info=True)
    finally:
        if conn:
            conn.close()
    
    return valid_symptoms, symptom_descriptions, disease_names, disease_categories

# Initialize data
VALID_SYMPTOMS, SYMPTOM_DESCRIPTIONS, DISEASE_NAMES, DISEASE_CATEGORIES = initialize_data()

def validate_symptoms(symptoms):
    """
    Validates that the given symptoms are in the list of valid symptoms.
    Returns a list of validated symptom IDs and a list of unrecognized symptoms.
    """
    validated_symptom_ids = []
    unrecognized_symptoms = []
    for symptom in symptoms:
        if symptom.lower() in VALID_SYMPTOMS:
            validated_symptom_ids.append(VALID_SYMPTOMS[symptom.lower()])
        else:
            unrecognized_symptoms.append(symptom)

    if unrecognized_symptoms:
        logger.warning(f"Unrecognized symptoms found: {unrecognized_symptoms}")
    return validated_symptom_ids, unrecognized_symptoms

@app.route('/')
def home():
    """
    Home route: Redirects to the analysis page.
    """
    return redirect(url_for('analyze_symptoms'))

@app.route('/analyze', methods=['GET', 'POST'])
def analyze_symptoms():
    """
    Route for text-based symptom entry and analysis.
    """
    if request.method == 'POST':
        user_input = request.form['symptoms']
        logger.info("User input: %s", user_input)

        try:
            extracted_symptoms = extract_symptoms(user_input) if user_input else []
            logger.info("Extracted symptoms: %s", extracted_symptoms)

            validated_symptom_ids, unrecognized_symptoms = validate_symptoms(extracted_symptoms)

            if not validated_symptom_ids:
                return render_template('analyze.html', error_message="No valid symptoms recognized. Please try again.")

            # Perform diagnosis based on validated symptom IDs
            results = diagnose_from_symptom_ids(validated_symptom_ids)

            return render_template('results.html', results=results)
        except Exception as e:
            logger.error(f"Error during symptom analysis: {e}", exc_info=True)
            return render_template('analyze.html', error_message="An error occurred during analysis. Please try again.")

    return render_template('analyze.html', error_message=None)

def diagnose_from_symptom_ids(symptom_ids):
    """
    Diagnoses diseases based on a list of symptom IDs.
    """
    try:
        # Load disease symptom mapping from the database
        DISEASE_SYMPTOMS = {}
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('SELECT disease_id, symptom_id FROM disease_symptoms')
                disease_symptoms = cursor.fetchall()
                for row in disease_symptoms:
                    disease_id, symptom_id = row['disease_id'], row['symptom_id']
                    if disease_id not in DISEASE_SYMPTOMS:
                        DISEASE_SYMPTOMS[disease_id] = []
                    DISEASE_SYMPTOMS[disease_id].append(symptom_id)
                logger.info("Disease symptoms mapping loaded successfully from the database.")
            except sqlite3.Error as e:
                logger.error(f"Error loading disease-symptom mapping: {e}", exc_info=True)
                return []
            finally:
                conn.close()
        else:
            logger.error("No database connection.")
            return []

        # Find potential diseases
        potential_diseases = {}
        for disease_id, symptoms in DISEASE_SYMPTOMS.items():
            match_count = len(set(symptom_ids).intersection(symptoms))
            if match_count > 0:
                potential_diseases[disease_id] = match_count

        # Sort diseases by match count
        sorted_diseases = sorted(potential_diseases.items(), key=lambda item: item[1], reverse=True)

        # Generate diagnosis results with explanations
        results = []
        for disease_id, match_count in sorted_diseases[:5]:  # Limit to top 5
            disease_name = DISEASE_NAMES.get(disease_id, "Unknown Disease")
            disease_category = DISEASE_CATEGORIES.get(disease_id, "Unknown Category")

            matched_symptoms = []

            conn = get_db_connection()
            if conn:
                try:
                    cursor = conn.cursor()
                    for symptom_id in symptom_ids:
                        if symptom_id in DISEASE_SYMPTOMS[disease_id]:
                            cursor.execute('SELECT description FROM symptoms WHERE id = ?', (symptom_id,))
                            symptom_name = cursor.fetchone()
                            if symptom_name:
                                matched_symptoms.append(symptom_name[0])
                except sqlite3.Error as e:
                    logger.error(f"Error retrieving symptoms: {e}", exc_info=True)
                finally:
                    conn.close()

            explanation = f"Diagnosis of {disease_name} ({disease_category}) is suggested because of the presence of the following symptoms: {', '.join(matched_symptoms)}."
            results.append({
                'disease': disease_name,
                'explanation': explanation,
                'score': match_count * 10,  # Arbitrary scoring
                'treatment': 'Consult doctor',  # Placeholder
                'category': disease_category
            })

        return results
    except Exception as e:
        logger.error(f"Error in diagnosis: {e}", exc_info=True)
        return []

def get_db_diagnosis(symptoms):
    """
    Fetches potential diagnoses from the database based on symptom matches.
    """
    conn = get_db_connection()
    if not conn:
        return []

    try:
        placeholders = ','.join(['?'] * len(symptoms))
        query = f"""
        SELECT d.name, d.treatment, COUNT(*) as match_count 
        FROM diseases d
        JOIN disease_symptoms ds ON d.id = ds.disease_id
        JOIN symptoms s ON ds.symptom_id = s.id
        WHERE s.description IN ({placeholders})
        GROUP BY d.id
        ORDER BY match_count DESC
        LIMIT 5
        """

        results = conn.execute(query, symptoms).fetchall()
        db_results = [{'disease': r[0], 'treatment': r[1], 'score': r[2] * 2} for r in results]
        logger.info("Database diagnosis results: %s", db_results)
        return db_results
    except Exception as e:
        logger.error("Database query error: %s", e, exc_info=True)
        return []
    finally:
        conn.close()

def get_ml_diagnosis(symptoms):
    """
    Get diagnosis probabilities from the machine learning model.
    """
    if not ml_model:
        logger.warning("ML model not loaded; skipping ML diagnosis.")
        return []

    try:
        symptom_df = pd.DataFrame({feat: [0] for feat in ml_model.feature_names_in_})
        for symptom in symptoms:
            if symptom in symptom_df.columns:
                symptom_df[symptom] = 1

        # Handle missing columns (symptoms not in ML model)
        for col in symptom_df.columns:
            if col not in symptoms:
                symptom_df[col] = 0  # Set to 0 if symptom is not present

        probabilities = ml_model.predict_proba(symptom_df)[0]
        ml_results = list(zip(ml_model.classes_, probabilities))
        logger.info("ML diagnosis results: %s", ml_results)
        return [{'disease': d, 'score': p * 100, 'treatment': 'Consult doctor'} for d, p in ml_results]
    except Exception as e:
        logger.error("ML prediction error: %s", e, exc_info=True)
        return []

def combine_results(results):
    """
    Combines diagnosis results from database, ML, and Prolog into a unified list.
    """
    combined = {}

    for item in results.get('db', []):
        disease = item['disease']
        combined[disease] = {
            'score': item['score'],
            'treatment': item['treatment'],
            'sources': ['database']
        }

    for item in results.get('ml', []):
        disease = item['disease']
        score = item['score']
        if disease in combined:
            combined[disease]['score'] += score
            combined[disease]['sources'].append('ml')
        else:
            combined[disease] = {
                'score': score,
                'treatment': item['treatment'],
                'sources': ['ml']
            }

    for item in results.get('Prolog', []):
        disease = item.get('disease')
        treatment = item.get('treatment', 'Consult doctor')
        if disease in combined:
            combined[disease]['score'] += 30
            combined[disease]['sources'].append('Prolog')
        else:
            combined[disease] = {
                'score': 30,
                'treatment': treatment,
                'sources': ['Prolog']
            }

    sorted_results = sorted(combined.items(), key=lambda x: x[1]['score'], reverse=True)[:5]
    logger.info("Final combined diagnosis results: %s", sorted_results)

    return [{'disease': k, 'score': v['score'], 'treatment': v['treatment'], 'sources': v['sources']} for k, v in sorted_results]

# Health check endpoint for deployment platforms
@app.route('/health')
def health_check():
    """Health check endpoint for deployment platforms"""
    return {'status': 'healthy', 'message': 'Medical Diagnosis App is running'}, 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404 if os.path.exists('templates/404.html') else "Page not found", 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {error}")
    return "Internal server error", 500

if __name__ == '__main__':
    # Configuration for different environments
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '127.0.0.1')
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    logger.info(f"Starting Flask app on {host}:{port} (debug={debug})")
    app.run(host=host, port=port, debug=debug)
else:
    # This runs when the app is imported (e.g., by gunicorn)
    logger.info("Flask app loaded for production deployment")