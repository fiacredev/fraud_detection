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
