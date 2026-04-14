import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path: str = "data/houses.csv"):
    """Load dataset from CSV"""
    df = pd.read_csv(path)
    return df

from sklearn.model_selection import train_test_split

def preprocess_data(df):
    # Drop non-numeric columns ('State' and 'City')
    X = df.drop(["Price", "State", "City"], axis=1)
    y = df["Price"]
    return train_test_split(X, y, test_size=0.2, random_state=42)
