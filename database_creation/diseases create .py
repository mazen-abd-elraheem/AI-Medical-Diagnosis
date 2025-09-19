import sqlite3
import logging
import pandas as pd  # Import pandas

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def categorize_diseases(db_path, csv_path):
    """
    Categorizes diseases in the database based on predefined categories and a CSV file.
    """

    # Define disease categories
    disease_categories = {
        'INF': [
            'Eczema', 'Psoriasis', 'Contact Dermatitis', 'Fungal Infections',
            'Common Cold', 'Allergic Rhinitis', 'Asthma', 'Bronchitis', 'Pneumonia', 'Sinusitis',
            'Tuberculosis', 'COVID-19', 'HIV/AIDS',
            'Zika Virus', 'Dengue Fever', 'Chikungunya', 'Malaria', 'Typhoid Fever',
            'Mumps', 'Rubella (German Measles)', 'Measles', 'Chickenpox',
            'Acute Sinusitis', 'Chronic Sinusitis', 'Conjunctivitis (Pink Eye)',
            'Otitis Media (Middle Ear Infection)', 'Hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Chlamydia', 'Gonorrhea', 'Syphilis', 'Trichomoniasis', 'Herpes Simplex Virus (HSV)', 'Human Papillomavirus (HPV)'
        ],
        'AI': [
            'Rheumatoid Arthritis', 'Systemic Lupus Erythematosus', 'Scleroderma',
            'Irritable Bowel Syndrome (IBS)', 'Crohn\'s Disease', 'Ulcerative Colitis',
            'Psoriatic Arthritis', 'Sjogren\'s Syndrome', 'Vasculitis', 'Behcet\'s Disease',
            'Rheumatic Fever', 'Systemic Scleroderma', 'Lupus Nephritis',
            'Amyloidosis', "Adult Still's Disease", 'Hypersensitivity Pneumonitis', 'Interstitial Cystitis (Painful Bladder Syndrome)'
        ],
        'NEU': [
            'Stroke', 'Epilepsy', 'Multiple Sclerosis', 'Parkinson\'s Disease',
            'Alzheimer\'s Disease', 'Huntington\'s Disease',
            'Amyotrophic Lateral Sclerosis (ALS)', 'Guillain-Barré Syndrome (GBS)',
            'Meniere\'s Disease', 'Motor Neurone Disease (MND)',
            'Creutzfeldt-Jakob Disease', 'Progressive Supranuclear Palsy (PSP)',
            'Multiple System Atrophy (MSA)', 'Tay-Sachs Disease', "Agnosia", "Aphasia"
        ],
        'CAR': [
            'Heart Disease', 'Hypertension', 'Myocardial Infarction',
            'Arteriosclerosis', 'Aortic Aneurysm', 'Brugada Syndrome',
            'Arrhythmias', 'Arteriosclerosis', 'Hypercholesterolemia', "Hypotension", "Thalassemia", 'Carcinoid Syndrome', 'Cardiomyopathy', 'Atrial Fibrillation'
        ],
        'GAS': [
            'Gastroenteritis', 'Peptic Ulcers', 'Irritable Bowel Syndrome (IBS)',
            'Crohn\'s Disease', 'Ulcerative Colitis', 'Diverticulitis',
            'Gastroesophageal Reflux Disease (GERD)', 'Peptic Ulcer Disease',
            'Celiac Disease', 'Hepatitis', 'Gallstones', 'Biliary Atresia', 'Gastroparesis', 'Esophageal Varices'
        ],
        'END': [
            'Diabetes Mellitus', 'Hyperthyroidism', 'Hypothyroidism',
            'Cushing\'s Syndrome', 'Addison\'s Disease', 'Hyperparathyroidism',
            'Hypoparathyroidism', 'Diabetes Insipidus',
            'Polycystic Ovary Syndrome (PCOS)', 'Hypoglycemia', "Hyperglycemia", 'Congenital Adrenal Hyperplasia', "Hypophosphatemia", "Hyperphosphatemia", "Hypomagnesemia", "Hypermagnesemia", "Hypocalcemia", "Hypercalcemia", "Hypokalemia", "Hyperchloremia"
        ],
        'MEN': [
            'Anxiety Disorders', 'Bipolar Disorder', 'Schizophrenia',
            'Post-Traumatic Stress Disorder (PTSD)', 'Major Depressive Disorder',
            'Anorexia Nervosa', 'Bulimia Nervosa', 'Obsessive-Compulsive Disorder (OCD)',
            'Panic Disorder', 'Social Anxiety Disorder', 'Borderline Personality Disorder (BPD)',
            'Seasonal Affective Disorder (SAD)', 'Asperger\'s Syndrome'
        ],
        'SKIN': ['Alopecia Areata', 'Acanthosis Nigricans', 'Hidradenitis Suppurativa', 'Porphyria', 'Ehlers-Danlos Syndrome (EDS)', 'Xeroderma Pigmentosum', "Rothmund-Thomson Syndrome"],
        'OTHER': ['Anemia', 'Deep Vein Thrombosis (DVT)', 'Degenerative Disc Disease', 'Frozen Shoulder', 'Glaucoma', "Gum Disease (Periodontitis)", 'Hemochromatosis', "Hereditary Angioedema", "Hirschsprung's Disease", "Hyperemesis Gravidarum", "Idiopathic Pulmonary Fibrosis", "Kawasaki Disease", "Klinefelter Syndrome", "Lesions", "Bacterial Vaginosis", "Candida Infections (Thrush)", "Carpal Tunnel Syndrome", "Cervical Spondylosis", "Hemolytic Anemia", "Myelodysplastic Syndromes (MDS)", "Aplastic Anemia", "Duchenne Muscular Dystrophy (DMD)", "Becker Muscular Dystrophy (BMD)", "Charcot-Marie-Tooth Disease (CMT)", "Friedreich's Ataxia", "Spinal Muscular Atrophy (SMA)", "Alport Syndrome", "Fabry Disease", "Gaucher Disease", "Pompe Disease", "Wilson's Disease", "Phenylketonuria (PKU)", "Hypoparathyroidism", "Hyperparathyroidism", "Aplastic Anemia", "Arrhythmias", "Myasthenia Gravis", "Klinefelter Syndrome", "Turner Syndrome", "Marfan Syndrome", "Hunter Syndrome (Mucopolysaccharidosis Type II)", "Hurler Syndrome (Mucopolysaccharidosis Type I)", "Fabry Disease", "Cystic Fibrosis", "Sturge-Weber Syndrome", "Thalassemia", "Lyme Disease", "Albinism", "Color Blindness", "Hemophilia", "Chronic Fatigue Syndrome (CFS)"]
    }


    try:
        # Read disease names from CSV into a dictionary
        disease_df = pd.read_csv(csv_path)
        disease_names = {row['id']: row['name'] for index, row in disease_df.iterrows()}

        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Add the 'category' column if it doesn't exist
        try:
            cursor.execute("ALTER TABLE diseases ADD COLUMN category TEXT")
            logger.info("Added 'category' column to the 'diseases' table.")
        except sqlite3.OperationalError as e:
            if "duplicate column name" in str(e):
                logger.info("'category' column already exists in the 'diseases' table.")
            else:
                logger.error(f"Error adding 'category' column: {e}")
                conn.close()
                return

        # Iterate through disease categories and update the database
        for category, disease_list in disease_categories.items():
            for disease_name in disease_list:
                # Find the disease ID from the CSV dictionary
                disease_id = None
                for id, name in disease_names.items():
                    if name == disease_name:
                        disease_id = id
                        break

                if disease_id:
                    try:
                        cursor.execute("UPDATE diseases SET category = ? WHERE id = ?", (category, disease_id))
                    except sqlite3.Error as e:
                        logger.error(f"Error updating category for '{disease_name}' (ID: {disease_id}): {e}", exc_info=True)
                else:
                    logger.warning(f"Disease '{disease_name}' not found in the CSV file.")

        # Commit the changes and close the connection
        conn.commit()
        logger.info("Successfully categorized diseases in the database.")

    except sqlite3.Error as e:
        logger.error(f"Database error: {e}", exc_info=True)

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    DB_PATH = r"C:\Users\L0Q\Desktop\medical -expert -system\database.db"  # Replace with the actual path to your database file
    CSV_PATH = r"C:\Users\L0Q\Desktop\medical -expert -system\database_creation\diseases.csv" # The CSV that contains disease names and IDs
    categorize_diseases(DB_PATH, CSV_PATH)