import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def find_uncategorized_diseases(db_path):
    """
    Finds diseases with NULL values in the 'category' column and prints their IDs and names.
    """

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Find diseases with NULL categories
        cursor.execute("SELECT id, name FROM diseases WHERE category IS NULL")
        uncategorized_diseases = cursor.fetchall()

        if uncategorized_diseases:
            logger.info("The following diseases have NULL categories:")
            for disease_id, disease_name in uncategorized_diseases:
                logger.info(f"  ID: {disease_id}, Name: {disease_name}")
        else:
            logger.info("All diseases have been categorized.")

    except sqlite3.Error as e:
        logger.error(f"Database error: {e}", exc_info=True)

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    DB_PATH = r"C:\Users\L0Q\Desktop\medical -expert -system\database.db"  # Replace with the actual path to your database file
    find_uncategorized_diseases(DB_PATH)
    