# Fraud Detection API

> A FastAPI service that scores transactions for fraud in real time, powered by
> a scikit-learn pipeline exported with joblib.

![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- 🚀 Lightweight FastAPI service with automatic OpenAPI docs
- 🤖 RandomForest pipeline with one-hot encoded categoricals
- ✅ Input validation with clear `422` errors
- 🧪 pytest suite covering every endpoint
- 🐳 Docker & docker-compose ready

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

### Example request

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d @sample_transaction.json
```

A successful response looks like:

```json
{"is_fraud": 0}
```

## Retraining the model

```bash
python train.py --data data/transactions.csv --model models/fraud_pipeline.joblib
```

## Docker

```bash
docker compose up --build
```

## Project structure

```
.
├── app.py                  # FastAPI application
├── train.py                # Training script
├── models/                 # Exported joblib pipeline
├── tests/                  # pytest suite
├── requirements.txt        # Runtime dependencies
├── requirements-dev.txt    # Test & lint dependencies
├── Dockerfile
├── docker-compose.yml
└── Makefile
```

## License

MIT — see [LICENSE](LICENSE).

## Author

**fiacredev** — fiacredeveloper@gmail.com
