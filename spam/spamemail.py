import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib

def load_data():
    # Load the dataset
    data = pd.read_csv('spam.csv', encoding='latin-1')
    data = data.rename(columns={"v1": "label", "v2": "text"})
    data = data[['text', 'label']]
    return data

def preprocess_data(data):
    # Convert labels to binary format
    data['label'] = data['label'].map({'ham': 0, 'spam': 1})
    
    # Split the data into features and labels
    X = data['text']
    y = data['label']
    
    # Convert text data to TF-IDF features
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(X)
    
    return X, y, vectorizer

def train_model(X_train, y_train):
    # Train a Naive Bayes classifier
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

def save_model(model, vectorizer):
    # Save the trained model and vectorizer
    joblib.dump(model, 'spam_classifier.pkl')
    joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

def predict_email(text):
    # Load the model and vectorizer
    model = joblib.load('spam_classifier.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    
    # Transform the input text to TF-IDF features
    text_transformed = vectorizer.transform([text])
    
    # Predict and return the result
    prediction = model.predict(text_transformed)
    return 'spam' if prediction[0] else 'ham'

if __name__ == "__main__":
    # Load and preprocess the data
    data = load_data()
    X, y, vectorizer = preprocess_data(data)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    evaluate_model(model, X_test, y_test)
    
    # Save the model and vectorizer
    save_model(model, vectorizer)
    
    # Example usage of the prediction function
    new_email = input("Enter a new email text to classify: ")
    print("The new email is classified as:", predict_email(new_email))
