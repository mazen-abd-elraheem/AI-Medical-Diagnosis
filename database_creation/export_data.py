import sqlite3
import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def export_diseases_to_csv(db_path, csv_path):
    """
    Exports disease data (id, name, category) from a SQLite database to a CSV file.
    """

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)

        # Query the diseases table
        query = "SELECT id, name, category FROM diseases"
        df = pd.read_sql_query(query, conn)

        # Export the DataFrame to a CSV file
        df.to_csv(csv_path, index=False)  # index=False prevents writing row indices to the CSV
        logger.info(f"Successfully exported disease data to '{csv_path}'.")

    except sqlite3.Error as e:
        logger.error(f"Database error: {e}", exc_info=True)

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    DB_PATH = r"C:\Users\L0Q\Desktop\medical -expert -system\database.db"  # Replace with the actual path to your database file
    CSV_PATH = r"C:\Users\L0Q\Desktop\medical -expert -system\database_creation\exported_diseases.csv"  # Replace with the desired path for the CSV file
    export_diseases_to_csv(DB_PATH, CSV_PATH)