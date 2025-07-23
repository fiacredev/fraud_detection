import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

app = FastAPI(
    title="Fraud Detection API",
    description="Score transactions for fraudulent activity in real time.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = os.getenv("MODEL_PATH", "models/fraud_pipeline.joblib")
pipeline = joblib.load(MODEL_PATH)

REQUIRED_FIELDS = [
    "merchant", "category", "amt", "gender", "lat", "long",
    "city_pop", "job", "unix_time", "merch_lat", "merch_long"
]


@app.get("/")
def home():
    return {
        "message": "Fraud Detection API"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/sample")
def sample_transaction():
    return {
        "merchant": "fraud_Rippin, Kub and Mann",
        "category": "grocery_pos",
        "amt": 125.5,
        "gender": "M",
        "lat": 40.1234,
        "long": -75.1234,
        "city_pop": 50000,
        "job": "Engineer",
        "unix_time": 1371816865,
        "merch_lat": 40.2345,
        "merch_long": -75.2345
    }


@app.post("/predict")
def predict(data: dict):

    missing = [f for f in REQUIRED_FIELDS if f not in data]
    if missing:
        raise HTTPException(
            status_code=422,
            detail=f"missing fields: {', '.join(missing)}",
        )

    df = pd.DataFrame([data])

    prediction = pipeline.predict(df)[0]

    return {
        "is_fraud": int(prediction)
    }
