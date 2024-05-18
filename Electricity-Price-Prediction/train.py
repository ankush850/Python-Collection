"""
Electricity Price Prediction - Model Training Pipeline
Converts exploratory analysis and model training from Jupyter notebook into a clean Python script.
"""

import os
import argparse
import pickle
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor


def load_data(filepath: str) -> pd.DataFrame:
    """Load and perform basic validation on the dataset."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset file not found at: {filepath}")
    
    df = pd.read_csv(filepath)
    print(f"Dataset loaded successfully with shape: {df.shape}")
    
    null_counts = df.isnull().sum()
    print("\nMissing values per column:")
    print(null_counts)
    
    return df


def evaluate_models(X_train, X_test, y_train, y_test, preprocessor):
    """Train and compare baseline models."""
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(random_state=42)
    }

    results = []
    print("\n--- Baseline Model Comparison ---")
    for name, model in models.items():
        pipe = Pipeline([
            ('preprocessing', preprocessor),
            ('regressor', model)
        ])
        
        pipe.fit(X_train, y_train)
        y_pred = pipe.predict(X_test)
        
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        results.append([name, rmse, mae, r2])

    results_df = pd.DataFrame(results, columns=['Model', 'RMSE', 'MAE', 'R²'])
    print(results_df.to_string(index=False))
    return results_df


def train_best_model(X, y, X_train, X_test, y_train, y_test, preprocessor, n_estimators=500):
    """Train tuned Random Forest pipeline and evaluate."""
    print(f"\n--- Training Optimized Random Forest (n_estimators={n_estimators}) ---")
    
    pipe = Pipeline([
        ('preprocessing', preprocessor),
        ('regressor', RandomForestRegressor(
            n_estimators=n_estimators,
            max_depth=None,
            min_samples_leaf=2,
            max_features='sqrt',
            bootstrap=True,
            oob_score=True,
            random_state=42
        ))
    ])

    # 5-fold Cross-Validation
    print("Performing 5-fold cross-validation...")
    scores = cross_val_score(pipe, X, y, cv=5, scoring='r2')
    print(f"Cross-validated R² scores: {scores}")
    print(f"Average CV R²: {scores.mean():.4f}")

    # Train on training set
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    # Performance metrics
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print("\nFinal Test Set Performance:")
    print(f"  R² Score : {r2:.4f}")
    print(f"  MAE      : {mae:.4f}")
    print(f"  RMSE     : {rmse:.4f}")

    return pipe


def save_model(model_pipeline, output_path: str):
    """Serialize and save the trained pipeline."""
    with open(output_path, "wb") as f:
        pickle.dump(model_pipeline, f)
    print(f"\nTrained model successfully saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Train Electricity Price Prediction ML Model")
    parser.add_argument("--data", type=str, default="electricity_cost_dataset.csv", help="Path to input CSV dataset")
    parser.add_argument("--model-output", type=str, default="model2.pkl", help="Path to save trained model pickle")
    parser.add_argument("--n-estimators", type=int, default=100, help="Number of trees in Random Forest")
    args = parser.parse_args()

    # 1. Load Data
    df = load_data(args.data)

    target_col = 'electricity cost'
    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not found in dataset columns: {list(df.columns)}")

    # 2. Split Features & Target
    X = df.drop(target_col, axis=1)
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Preprocessor (One-hot encode categorical feature at column index 1: 'structure type')
    categorical_features = [1]
    preprocessor = ColumnTransformer([
        ('ohe', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ], remainder='passthrough')

    # 4. Compare baseline models
    evaluate_models(X_train, X_test, y_train, y_test, preprocessor)

    # 5. Train and validate final model
    final_pipeline = train_best_model(X, y, X_train, X_test, y_train, y_test, preprocessor, n_estimators=args.n_estimators)

    # 6. Save Model
    save_model(final_pipeline, args.model_output)


if __name__ == "__main__":
    main()
