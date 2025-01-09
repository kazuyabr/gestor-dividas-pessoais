from fastapi.testclient import TestClient
from src.server import app
import random
from datetime import datetime

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "message": "API esta funcionando normalmente"
    }

def test_create_user():
    response = client.post(
        "/api/v1/usuarios/",
        json={
            "nome": "Test User",
            "email": f"test{random.randint(1,1000)}@test.com",
            "senha": "test123"
        }
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "Test User"

def test_create_divida():
    response = client.post(
        "/api/v1/dividas/?usuario_id=1",
        json={
            "valor": 1500.00,
            "data_vencimento": "2024-03-20T00:00:00",
            "descricao": "Test Divida"
        }
    )
    assert response.status_code == 200
    assert response.json()["valor"] == 1500.00