import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import numpy as np

# Step 1: Data Collection
def load_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    return data

# Step 2: Data Preprocessing
def preprocess_data(data):
    # Assume the dataset has columns 'year' and 'birth_rate'
    # We will use the 'year' as the feature and 'birth_rate' as the target
    X = data[['year']].values
    y = data['birth_rate'].values
    return X, y

# Step 3: Model Selection and Training
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Step 4: Model Evaluation
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")

# Step 5: Save the Model
def save_model(model):
    joblib.dump(model, 'birthrate_predictor.pkl')

# Step 6: Load the Model and Predict
def predict_birthrate(year):
    model = joblib.load('birthrate_predictor.pkl')
    year = np.array(year).reshape(-1, 1)
    prediction = model.predict(year)
    return prediction

if __name__ == "__main__":
    # Load and preprocess the data
    data = load_data('birth_rate_data.csv')
    X, y = preprocess_data(data)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    evaluate_model(model, X_test, y_test)
    
    # Save the model
    save_model(model)
    
    # Predict birth rate for a given year
    year = int(input("Enter the year to predict the birth rate: "))
    prediction = predict_birthrate(year)
    print(f"The predicted birth rate for the year {year} is {prediction[0]}")
