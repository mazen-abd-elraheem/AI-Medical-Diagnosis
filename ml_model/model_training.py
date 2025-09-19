import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model():
    # Load the dataset (ensure 'ml_model/dataset.csv' exists and is formatted correctly)
    try:
        data = pd.read_csv('ml_model/dataset.csv')
    except Exception as e:
        print("Error loading CSV file:", e)
        return

    # Ensure that the 'diagnosis' column exists in the dataset
    if 'diagnosis' not in data.columns:
        print("Error: 'diagnosis' column not found in the dataset.")
        return

    # Separate features and target
    X = data.drop('diagnosis', axis=1)
    y = data['diagnosis']

    # Preprocess features:
    # Convert any categorical/string features into numerical format using one-hot encoding.
    # This will convert all columns with object dtype into dummy/indicator variables.
    X = pd.get_dummies(X)
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a RandomForestClassifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Evaluate the model on the test set
    accuracy = clf.score(X_test, y_test)
    print(f"Model accuracy on test set: {accuracy * 100:.2f}%")
    
    # Save the trained model to a file
    joblib.dump(clf, 'ml_model/symptom_checker.pkl')
    print("Model training complete and saved as 'ml_model/symptom_checker.pkl'.")

if __name__ == '__main__':
    train_model()
