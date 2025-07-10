# Fraud Detection API

> A FastAPI service that scores transactions for fraud in real time.

## Quickstart

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

Then open <http://127.0.0.1:8000/docs> for the interactive Swagger UI.

## Endpoints

| Method | Path       | Description                       |
|--------|------------|-----------------------------------|
| GET    | `/`        | Service banner                    |
| GET    | `/health`  | Liveness check                    |
| GET    | `/sample`  | Example transaction payload       |
| POST   | `/predict` | Score a transaction for fraud     |

More documentation coming soon.
