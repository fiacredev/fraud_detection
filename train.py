"""Train the fraud detection pipeline and export it with joblib."""

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
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


if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)
    print(f"Loaded {len(df)} rows from {DATA_PATH}")

    pipeline = build_pipeline()
    pipeline.fit(df.drop(columns=["is_fraud"]), df["is_fraud"])

    joblib.dump(pipeline, MODEL_PATH)
    print(f"Saved pipeline to {MODEL_PATH}")
