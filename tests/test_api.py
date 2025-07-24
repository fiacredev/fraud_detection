from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_home_returns_service_name():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Fraud Detection API"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_sample_payload_contains_required_fields():
    response = client.get("/sample")
    assert response.status_code == 200
    payload = response.json()
    for field in (
        "merchant", "category", "amt", "gender", "lat", "long",
        "city_pop", "job", "unix_time", "merch_lat", "merch_long",
    ):
        assert field in payload


def test_predict_rejects_missing_fields():
    response = client.post("/predict", json={"amt": 10.0})
    assert response.status_code == 422
    assert "missing fields" in response.json()["detail"]


def test_predict_scores_sample_transaction():
    payload = client.get("/sample").json()
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json()["is_fraud"] in (0, 1)
