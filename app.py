from fastapi import FastAPI

app = FastAPI(title="Fraud Detection API")


@app.get("/")
def home():
    return {
        "message": "Fraud Detection API"
    }
