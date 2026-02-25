import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np

class FraudDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)

    def load_data(self, filepath):
        self.df = pd.read_csv(filepath, parse_dates=['timestamp'])
        self.df['total_value'] = self.df['quantity'] * self.df['price']
        return self.df

    def detect_fraud(self):
        X = self.df[['quantity', 'price', 'total_value']]
        self.model.fit(X)
        self.df['fraud_score'] = self.model.decision_function(X)
        self.df['is_fraud'] = self.model.predict(X)
        self.df['is_fraud'] = self.df['is_fraud'].map({1: 0, -1: 1})
        return self.df

    def get_fraudulent_transactions(self):
        return self.df[self.df['is_fraud'] == 1]
