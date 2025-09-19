from pyswip import Prolog

def prolog_diagnose(symptoms):
    """
    Query the Prolog knowledge base to diagnose diseases based on symptoms.
    
    Args:
        symptoms (list): A list of symptoms provided by the user.
    
    Returns:
        list: A list of dictionaries containing diagnosis results.
    """
    prolog = Prolog()
    prolog.consult(r'Prolog/medical_kb.pl')  # Ensure the path is correct

    results = []
    query = "diagnose(Disease, Symptoms, Treatment)"
    
    try:
        for result in prolog.query(query):
            res_symptoms = result.get('Symptoms', [])

            # Convert symptoms to a list if they are stored as a comma-separated string
            if isinstance(res_symptoms, str):
                res_symptoms = [s.strip() for s in res_symptoms.split(',')]
            
            # Check for a significant match between user symptoms and Prolog symptoms
            common_symptoms = set(res_symptoms) & set(symptoms)
            if len(common_symptoms) >= 1:  # Adjust threshold as needed
                results.append({
                    'disease': result.get('Disease'),
                    'treatment': result.get('Treatment'),
                    'matched_symptoms': list(common_symptoms),
                    'score': len(common_symptoms)  # Add a score based on the number of matched symptoms
                })
        
        # Sort results by score (number of matched symptoms) in descending order
        results = sorted(results, key=lambda x: x['score'], reverse=True)
        
        # Limit the results to the top 5 diagnoses
        results = results[:5]
        
    except Exception as e:
        print(f"Error querying Prolog: {e}")
        results = [{"message": "An error occurred while querying the Prolog knowledge base."}]
    
    return results if results else [{"message": "No diagnosis found based on provided symptoms."}]