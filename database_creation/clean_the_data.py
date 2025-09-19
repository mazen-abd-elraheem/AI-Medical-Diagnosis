import sqlite3
import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def categorize_uncategorized_diseases(db_path, csv_path):
    """
    Categorizes diseases in the database based on predefined categories and a CSV file.
    """

    # Define comprehensive disease categories
    disease_categories = {
        'Arthritis': "AI",
        'Osteoarthritis': "AI",
        'Fibromyalgia': "AI",
        'Chronic Fatigue Syndrome': "OTHER",
        'Leukemia': "OTHER",
        'Lymphoma': "OTHER",
        'Chronic Obstructive Pulmonary Disease (COPD)': "AI",
        'Sleep Apnea': "MEN",
        'Vertigo': "NEU",
        'Hypoglycemia (Low Blood Sugar)': "END",
        'Hyperglycemia (High Blood Sugar)': "END",
        'Human Immunodeficiency Virus (HIV)': "INF",
        'Irritable Bowel Syndrome (IBS)': "GAS",
        'Celiac Disease': "GAS",
        'Generalized Anxiety Disorder (GAD)': "MEN",
        'Raynaud\'s Phenomenon': "AI",
        'Systemic Lupus Erythematosus (SLE)': "AI",
        'Addison\'s Disease': "END",
        'Cushing\'s Syndrome': "END",
        'Sarcoidosis': "AI",
        'Wegener\'s Granulomatosis (Granulomatosis with Polyangiitis)': "AI",
        'Hemolytic Uremic Syndrome (HUS)': "OTHER",
        'Krabbe Disease': "NEU",
        'Adrenoleukodystrophy (ALD)': "NEU",
        'Angelman Syndrome': "NEU",
        'Huntington\'s Disease': "NEU",
        'Treacher Collins Syndrome': "OTHER",
        'Cri du Chat Syndrome': "NEU",
        'Tay-Sachs Disease': "NEU",
        'Canavan Disease': "NEU",
        'Appendicitis': "GAS",
        "Hypersomnia": "MEN",
        "Hypochondriasis": "MEN",
        "Tuberous Sclerosis Complex (TSC)": "SKIN",
        "Diabetic Ketoacidosis (DKA)": "END",
        "Anaphylaxis": "INF",
        'Progeria': "OTHER",
        'Alkaptonuria': "OTHER",
        'Klinefelter Syndrome': "OTHER",
        'Goodpasture\'s Syndrome': "AI",
        'Encephalitis': "INF",
        "Ovarian Cancer": "OTHER",
        "Aortic Dissection": "CAR",
        "Prader-Willi Syndrome": "OTHER",
        "Lesch-Nyhan Syndrome": "NEU",
        "Pemphigus": "SKIN",
        "Guillain-Barré Syndrome": "NEU",
        "Sjogren-Larsson Syndrome": "NEU",
        "Ehlers-Danlos Syndrome (EDS)": "SKIN",
        "Biliary Atresia": "GAS",
        'Hyperemesis Gravidarum': "GAS",
        "Klinefelter Syndrome": "OTHER",
        "Schwannomatosis": "NEU",
        "Lymphedema": "OTHER",
        "Wilson's Disease": "OTHER",
        "Noonan Syndrome": "OTHER",
        "Fabry Disease": "OTHER",
        "Hurler Syndrome": "OTHER",
         "Hunter Syndrome": "OTHER",
        "Aicardi-Goutieres Syndrome": "NEU",
        "Brugada Syndrome": "CAR",
        "Dengue Fever": "INF",
        "Hyperkalemia": "END",
        "Hypokalemia": "END",
        "Heat Rash": "SKIN",
        "Down Syndrome": "OTHER",
        "Polycystic Kidney Disease": "OTHER",
        "Polycystic Ovary Syndrome (PCOS)": "END",
        "Primary Immunodeficiency": "OTHER",
        "Zellweger Syndrome": "OTHER",
        "von Hippel-Lindau Disease": "OTHER",
       "Niemann-Pick Disease": "OTHER",
       "Thalassemia": "CAR"
    ,   "Hemophilia" : "CAR",
    "Leukodystrophy": "NEU",
    "Parkinson's Disease" : "NEU",
    "Acromegaly": "END",
    "Aplastic Anemia": "OTHER",
    "Asphyxia":"OTHER",
     "Barrett's Esophagus":"GAS",
     "Celiac Disease":"GAS",
     "Chondrocalcinosis (Pseudogout)":"AI",
     "Chronic Fatigue Syndrome (CFS)":"OTHER",
     "Chronic Obstructive Pulmonary Disease (COPD)":"AI",
    "Cirrhosis": "GAS",
     "Costochondritis": "OTHER",
     "Creutzfeldt-Jakob Disease (CJD)":"NEU",
     "Cushing's Syndrome":"END",
     "Diverticulitis":"GAS",
      "Ehlers-Danlos Syndrome (EDS)":"SKIN",
    "Epilepsy": "NEU",
    "Fibromyalgia":"AI",
      "Graves' Disease":"END",
        "Hemochromatosis":"END",
         "Hepatitis (A, B, C)":"INF",
        "Interstitial Cystitis (Painful Bladder Syndrome)":"OTH",
        "Irritable Bowel Syndrome (IBS)":"GAS",
        "Klinefelter Syndrome":"OTHER"
       ,  "Myasthenia Gravis":"AI"
    ,    "Phenylketonuria (PKU)":"END"
    ,      "Adrenoleukodystrophy (ALD)":"NEU"

    }

    try:
        # Read disease names from CSV into a dictionary
        disease_df = pd.read_csv(csv_path)
        disease_names = {row['id']: row['name'] for index, row in disease_df.iterrows()}

        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Iterate through disease categories and update the database *only* for NULL categories
        for disease_name, category in disease_categories.items():
            # Find the disease ID from the CSV dictionary
            disease_id = None
            for id, name in disease_names.items():
                if name == disease_name:
                    disease_id = id
                    break

            if disease_id:
                try:
                    # Only update if the category is NULL
                    cursor.execute("UPDATE diseases SET category = ? WHERE id = ?", (category, disease_id))
                except sqlite3.Error as e:
                    logger.error(f"Error updating category for '{disease_name}' (ID: {disease_id}): {e}", exc_info=True)
            else:
                logger.warning(f"Disease '{disease_name}' not found in the CSV file.")

        # Commit the changes and close the connection
        conn.commit()
        logger.info("Successfully categorized diseases with NULL categories in the database.")

    except sqlite3.Error as e:
        logger.error(f"Database error: {e}", exc_info=True)

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    DB_PATH = r"C:\Users\L0Q\Desktop\medical -expert -system\database.db"  # Replace with the actual path to your database file
    CSV_PATH = r"C:\Users\L0Q\Desktop\medical -expert -system\exported_diseases.csv"  # The CSV that contains disease names and IDs
    categorize_uncategorized_diseases(DB_PATH, CSV_PATH)