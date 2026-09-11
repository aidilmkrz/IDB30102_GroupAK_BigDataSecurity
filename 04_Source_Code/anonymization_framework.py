import time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


class PrivacyFramework:
    def __init__(self, data_path):
        """
        Initializes the framework with the UCI Adult Census Income dataset.
        """
        self.data_path = data_path
        self.raw_data = None
        self.processed_data = None
        self.feature_cols = ['age', 'workclass', 'education', 'marital-status', 
                             'occupation', 'relationship', 'race', 'sex', 
                             'capital-gain', 'capital-loss', 'hours-per-week', 'native-country']
        self.target_col = 'income'
        self.quasi_identifiers = ['age', 'marital-status']

    def load_data(self):
        """Loads and cleans raw data."""
        column_names = [
            'age', 'workclass', 'fnlwgt', 'education', 'education-num',
            'marital-status', 'occupation', 'relationship', 'race', 'sex',
            'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'
        ]
        self.raw_data = pd.read_csv(self.data_path, names=column_names, skipinitialspace=True)
        # Drop rows with missing values denoted by '?'
        self.raw_data = self.raw_data.replace('?', np.nan).dropna()
        return self.raw_data

    def apply_k_anonymity(self, k=3):
        """
        Applies standard k-anonymity via generalization on quasi-identifiers.
        - Generalizes 'age' into 10-year interval bins.
        - Suppresses non-conforming equivalence classes if size < k.
        """
        start_time = time.time()
        df = self.raw_data.copy()

        # Generalization: Bin age into ranges (e.g., 20-29, 30-39)
        age_bins = [0, 20, 30, 40, 50, 60, 70, 80, 100]
        age_labels = ['<20', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']
        df['age'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False).astype(str)

        # Suppression: Identify and drop equivalence groups smaller than k
        group_counts = df.groupby(self.quasi_identifiers)[self.target_col].transform('count')
        df_k_anonymous = df[group_counts >= k].copy()

        execution_time_ms = (time.time() - start_time) * 1000
        return df_k_anonymous, execution_time_ms

    def apply_differential_privacy(self, epsilon=1.0):
        """
        Applies Differential Privacy using Laplace noise injection on numeric features.
        """
        start_time = time.time()
        df = self.raw_data.copy()

        numeric_cols = ['age', 'capital-gain', 'capital-loss', 'hours-per-week']
        
        for col in numeric_cols:
            # Calculate sensitivity (max difference)
            col_min = df[col].min()
            col_max = df[col].max()
            sensitivity = float(col_max - col_min)
            
            # Calibrate noise scale b = sensitivity / epsilon
            scale = sensitivity / epsilon
            noise = np.random.laplace(0, scale, size=len(df))
            
            # Inject noise and clip values to valid domain
            df[col] = np.clip(df[col] + noise, col_min, col_max)

        execution_time_ms = (time.time() - start_time) * 1000
        return df, execution_time_ms

    @staticmethod
    def calculate_reidentification_risk(df, quasi_identifiers):
        """
        Calculates re-identification risk based on equivalence class sizes.
        Risk = 1 / Equivalence_Class_Size for unique quasi-identifier combinations.
        """
        groups = df.groupby(quasi_identifiers).size()
        avg_class_size = groups.mean()
        # Proportion of unique records (size = 1) relative to total rows
        unique_records = (groups[groups == 1]).sum()
        risk_percentage = (unique_records / len(df)) * 100
        return round(risk_percentage, 2)

    def evaluate_utility(self, df):
        """
        Evaluates data utility using a Random Forest downstream classification model.
        """
        df_encoded = pd.get_dummies(df[self.feature_cols], drop_first=True)
        y = (df[self.target_col] == '>50K').astype(int)

        X_train, X_test, y_train, y_test = train_test_split(
            df_encoded, y, test_size=0.3, random_state=42
        )

        clf = RandomForestClassifier(n_estimators=50, random_state=42)
        clf.fit(X_train, y_train)
        predictions = clf.predict(X_test)
        
        acc = accuracy_score(y_test, predictions) * 100
        return round(acc, 2)