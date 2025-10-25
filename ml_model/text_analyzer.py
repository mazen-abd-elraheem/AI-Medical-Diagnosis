import spacy
import string
"""text_analyzer.py"""
# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_symptoms(text):
    """
    Extract symptoms from the user's text input using spaCy.
    """
    # Tokenization and preprocessing
    doc = nlp(text.lower())
    tokens = [token.text for token in doc if token.text not in string.punctuation]

    # Load symptoms from the CSV file
    import pandas as pd
    symptoms_df = pd.read_csv('database_creation/symptoms.csv') 
    symptoms_list = symptoms_df['description'].tolist()

    # Match tokens with symptoms
    found_symptoms = [symptom for symptom in symptoms_list if symptom in tokens]
    return found_symptoms