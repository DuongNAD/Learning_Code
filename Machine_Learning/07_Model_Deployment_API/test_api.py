"""
Unit tests for FastAPI Model Serving Endpoint.
"""

import sys
import os
import pytest
from fastapi.testclient import TestClient

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from server import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert "calibrated_threshold" in data


def test_predict_endpoint_valid_payload(client):
    payload = {
        "Pregnancies": 2.0,
        "Glucose": 150.0,
        "BloodPressure": 75.0,
        "SkinThickness": 25.0,
        "Insulin": 110.0,
        "BMI": 30.5,
        "DiabetesPedigreeFunction": 0.55,
        "Age": 42.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] in [0, 1]
    assert 0.0 <= data["probability"] <= 1.0
    assert "threshold_applied" in data
    assert "meaning" in data
    assert "clinical_recommendation" in data


def test_predict_batch_endpoint(client):
    batch = [
        {
            "Pregnancies": 1.0,
            "Glucose": 85.0,
            "BloodPressure": 66.0,
            "SkinThickness": 29.0,
            "Insulin": 0.0,
            "BMI": 26.6,
            "DiabetesPedigreeFunction": 0.351,
            "Age": 31.0
        },
        {
            "Pregnancies": 8.0,
            "Glucose": 183.0,
            "BloodPressure": 64.0,
            "SkinThickness": 0.0,
            "Insulin": 0.0,
            "BMI": 23.3,
            "DiabetesPedigreeFunction": 0.672,
            "Age": 32.0
        }
    ]
    response = client.post("/predict_batch", json=batch)
    assert response.status_code == 200
    results = response.json()
    assert len(results) == 2
    assert results[0]["prediction"] in [0, 1]
    assert results[1]["prediction"] in [0, 1]


def test_predict_missing_field(client):
    # Missing Age and BMI
    payload = {
        "Pregnancies": 2.0,
        "Glucose": 150.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  # Unprocessable Entity
