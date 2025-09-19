import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create tables (if they already exist, this will not overwrite them)
cursor.execute("""
CREATE TABLE IF NOT EXISTS diseases (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS symptoms (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS disease_symptoms (
    disease_id INTEGER,
    symptom_id INTEGER,
    FOREIGN KEY (disease_id) REFERENCES diseases(id),
    FOREIGN KEY (symptom_id) REFERENCES symptoms(id)
);
""")

# Load CSV data
diseases = pd.read_csv("diseases.csv")
symptoms = pd.read_csv("symptoms.csv")
disease_symptoms = pd.read_csv("disease_symptoms.csv")

# Insert data into tables using 'replace' so that any existing data is dropped
diseases.to_sql("diseases", conn, if_exists="replace", index=False)
symptoms.to_sql("symptoms", conn, if_exists="replace", index=False)
disease_symptoms.to_sql("disease_symptoms", conn, if_exists="replace", index=False)

conn.commit()
conn.close()
