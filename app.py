from fastapi import FastAPI

app = FastAPI(title="Fraud Detection API")


@app.get("/")
def home():
    return {
        "message": "Fraud Detection API"
    }


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
