import csv
import sqlite3  # Or your database library of choice (e.g., psycopg2 for PostgreSQL, pymysql for MySQL)

def insert_csv_into_db(csv_filepath, db_filepath, table_name, skip_header=True):
    """
    Inserts data from a CSV file into an SQLite database table.

    Args:
        csv_filepath (str):  Path to the CSV file.
        db_filepath (str):  Path to the SQLite database file.
        table_name (str):  Name of the table to insert the data into.  If the table
                          doesn't exist, it will be created automatically based on
                          the CSV's header row.  If it *does* exist, ensure the CSV
                          columns match the table columns.
        skip_header (bool, optional): Whether to skip the header row in the CSV file.
                                       Defaults to True.
    """

    try:
        # Connect to the database (creates the database file if it doesn't exist)
        conn = sqlite3.connect(db_filepath)
        cursor = conn.cursor()

        with open(csv_filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)

            header = next(reader)  # Get the header row (column names)

            if skip_header:  # Skip the header row if requested
                next(reader, None)  # Consume the next line if there IS a next line

            # Check if the table exists. If not, create it
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
            table_exists = cursor.fetchone() is not None

            if not table_exists:
                # Create the table based on the CSV header
                column_definitions = ", ".join(f"'{col}' TEXT" for col in header)  # Default all columns to TEXT type
                create_table_sql = f"CREATE TABLE '{table_name}' ({column_definitions});"
                cursor.execute(create_table_sql)
                print(f"Table '{table_name}' created.")

            # Prepare the SQL INSERT statement
            num_columns = len(header)
            placeholders = ", ".join(["?"] * num_columns)  # Create placeholders for values
            insert_sql = f"INSERT INTO '{table_name}' VALUES ({placeholders});"

            # Insert data row by row
            for row in reader:
                cursor.execute(insert_sql, row)

        # Commit the changes and close the connection
        conn.commit()
        print(f"Data from '{csv_filepath}' successfully inserted into table '{table_name}'.")


    except sqlite3.Error as e:
        print(f"Database error: {e}")
        conn.rollback()  # Rollback changes if an error occurred

    except FileNotFoundError:
        print(f"Error: CSV file '{csv_filepath}' not found.")

    except Exception as e:  # Catch any other potential errors
        print(f"An unexpected error occurred: {e}")
        conn.rollback()

    finally:
        if conn:
            conn.close()


# Example usage:
if __name__ == "__main__":
    csv_file = r"C:\Users\L0Q\Desktop\diseases.csv"  # Replace with the actual path to your CSV file
    db_file = r"C:\Users\L0Q\Desktop\medical -expert -system\database.db"  # Replace with the desired database file path
    table_name = "diseases"     # Replace with the desired table name

    

    insert_csv_into_db(csv_file, db_file, table_name)