import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def train_model():
    # Load dataset
    data = pd.read_csv("data/house_prices.csv")

    X = data.drop("Price", axis=1)
    y = data["Price"]

    # Encode categorical columns
    X = pd.get_dummies(X, drop_first=True)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print("✅ Model trained successfully")
    print(f"RMSE: {rmse:,.2f}, R²: {r2:.2f}")

    # Save model and columns
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/house_price_model.pkl")
    joblib.dump(X.columns.tolist(), "models/model_columns.pkl")
    print("💾 Model and feature columns saved successfully")

if __name__ == "__main__":
    train_model()
