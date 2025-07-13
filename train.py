"""Train the fraud detection pipeline and export it with joblib."""

import argparse

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

DATA_PATH = "data/transactions.csv"
MODEL_PATH = "models/fraud_pipeline.joblib"

NUMERIC_FEATURES = [
    "amt", "lat", "long", "city_pop", "unix_time", "merch_lat", "merch_long"
]
CATEGORICAL_FEATURES = ["merchant", "category", "gender", "job"]


def build_pipeline() -> Pipeline:
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", "passthrough", NUMERIC_FEATURES),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
        ]
    )

    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", RandomForestClassifier(random_state=42)),
        ]
    )


def train(data_path: str = DATA_PATH, model_path: str = MODEL_PATH) -> Pipeline:
    df = pd.read_csv(data_path)
    print(f"Loaded {len(df)} rows from {data_path}")

    X = df.drop(columns=["is_fraud"])
    y = df["is_fraud"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    print(classification_report(y_test, pipeline.predict(X_test)))

    joblib.dump(pipeline, model_path)
    print(f"Saved pipeline to {model_path}")
    return pipeline


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train the fraud pipeline")
    parser.add_argument("--data", default=DATA_PATH, help="Path to training CSV")
    parser.add_argument("--model", default=MODEL_PATH, help="Output model path")
    args = parser.parse_args()

    train(args.data, args.model)
