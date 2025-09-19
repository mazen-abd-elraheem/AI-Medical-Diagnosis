from flask import Flask, render_template, request, url_for, redirect
import sqlite3
import joblib
import pandas as pd
import os
import logging

# Import your modules (comment out if they don't exist to test basic functionality)
try:
    from Prolog.prolog_engine import prolog_diagnose
except ImportError:
    print("Warning: Prolog module not found")
    def prolog_diagnose(*args): return []

try:
    from ml_model.text_analyzer import extract_symptoms
except ImportError:
    print("Warning: Text analyzer not found")
    def extract_symptoms(text): return text.split(',') if text else []

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
        if symptom.lower().strip() in VALID_SYMPTOMS:
            validated_symptom_ids.append(VALID_SYMPTOMS[symptom.lower().strip()])
        else:
            unrecognized_symptoms.append(symptom)

    if unrecognized_symptoms:
        logger.warning(f"Unrecognized symptoms found: {unrecognized_symptoms}")
    return validated_symptom_ids, unrecognized_symptoms

# MAIN ROUTES - These are crucial for your website to work

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Main route - shows symptom input form and processes results
    """
    if request.method == 'GET':
        # Show the symptom input form
        return render_template('analyze.html', error_message=None)
    
    elif request.method == 'POST':
        # Process the form submission
        try:
            user_input = request.form.get('symptoms', '').strip()
            logger.info("User input: %s", user_input)

            if not user_input:
                return render_template('analyze.html', error_message="Please enter your symptoms.")

            # Extract symptoms from user input
            extracted_symptoms = extract_symptoms(user_input) if user_input else []
            logger.info("Extracted symptoms: %s", extracted_symptoms)

            # If no symptoms extracted, treat input as comma-separated list
            if not extracted_symptoms:
                extracted_symptoms = [s.strip() for s in user_input.split(',') if s.strip()]

            if not extracted_symptoms:
                return render_template('analyze.html', error_message="No symptoms could be identified. Please try again.")

            validated_symptom_ids, unrecognized_symptoms = validate_symptoms(extracted_symptoms)

            if not validated_symptom_ids:
                error_msg = "No valid symptoms recognized. Please try again."
                if unrecognized_symptoms:
                    error_msg += f" Unrecognized: {', '.join(unrecognized_symptoms)}"
                return render_template('analyze.html', error_message=error_msg)

            # Perform diagnosis based on validated symptom IDs
            results = diagnose_from_symptom_ids(validated_symptom_ids)

            return render_template('results.html', results=results, symptoms=extracted_symptoms)

        except Exception as e:
            logger.error(f"Error during symptom analysis: {e}", exc_info=True)
            return render_template('analyze.html', error_message="An error occurred during analysis. Please try again.")

@app.route('/analyze', methods=['GET', 'POST'])  
def analyze():
    """
    Alternative route - redirects to main route for consistency
    """
    return home()

@app.route('/test')
def test():
    """
    Test route to verify the app is working
    """
    return "<h1>Flask App is Working!</h1><p>Your medical diagnosis system is running properly.</p><a href='/'>Go to Main App</a>"

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
                return [{"disease": "Database Error", "explanation": "Could not load disease data", "score": 0, "treatment": "Consult a doctor", "category": "Error"}]
            finally:
                conn.close()
        else:
            logger.error("No database connection.")
            return [{"disease": "Connection Error", "explanation": "Could not connect to database", "score": 0, "treatment": "Consult a doctor", "category": "Error"}]

        # Find potential diseases
        potential_diseases = {}
        for disease_id, symptoms in DISEASE_SYMPTOMS.items():
            match_count = len(set(symptom_ids).intersection(symptoms))
            if match_count > 0:
                potential_diseases[disease_id] = match_count

        # If no matches found, return a helpful message
        if not potential_diseases:
            return [{
                "disease": "No Specific Match Found", 
                "explanation": "The symptoms provided don't match any specific disease pattern in our database. This could be normal or require professional evaluation.",
                "score": 0,
                "treatment": "Please consult a healthcare professional for proper diagnosis",
                "category": "General"
            }]

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
                        if symptom_id in DISEASE_SYMPTOMS.get(disease_id, []):
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
                'score': match_count * 20,  # Score out of 100
                'treatment': 'Consult a doctor for proper diagnosis and treatment',
                'category': disease_category
            })

        return results
        
    except Exception as e:
        logger.error(f"Error in diagnosis: {e}", exc_info=True)
        return [{
            "disease": "System Error", 
            "explanation": f"An error occurred during diagnosis: {str(e)}", 
            "score": 0,
            "treatment": "Please try again or consult a healthcare professional",
            "category": "Error"
        }]

# Health check endpoint for deployment platforms
@app.route('/health')
def health_check():
    """Health check endpoint for deployment platforms"""
    return {'status': 'healthy', 'message': 'Medical Diagnosis App is running'}, 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    logger.error(f"404 error: {error}")
    return f"<h1>Page Not Found</h1><p>The page you're looking for doesn't exist.</p><a href='/'>Go to Home</a>", 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {error}")
    return f"<h1>Internal Server Error</h1><p>Something went wrong.</p><a href='/test'>Test App</a>", 500

# Basic template fallback if templates don't exist
@app.route('/basic')
def basic_interface():
    """Basic HTML interface if templates are missing"""
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>Medical Diagnosis System</title></head>
    <body>
        <h1>Medical Diagnosis System</h1>
        <form method="POST" action="/">
            <p>Enter your symptoms (separated by commas):</p>
            <textarea name="symptoms" rows="4" cols="50" placeholder="e.g., headache, fever, nausea"></textarea><br><br>
            <input type="submit" value="Analyze Symptoms">
        </form>
        <p><a href="/test">Test if app is working</a></p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    # Configuration for different environments
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')  # Changed to 0.0.0.0 for external access
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'  # Default to False for production
    
    logger.info(f"Starting Flask app on {host}:{port} (debug={debug})")
    print(f"🚀 Medical Diagnosis System starting on http://{host}:{port}")
    print(f"📊 Database status: {'Connected' if get_db_connection() else 'Error'}")
    print(f"🤖 ML Model status: {'Loaded' if ml_model else 'Not loaded'}")
    
    app.run(host=host, port=port, debug=debug)
else:
    # This runs when the app is imported (e.g., by gunicorn)
    logger.info("Flask app loaded for production deployment")
