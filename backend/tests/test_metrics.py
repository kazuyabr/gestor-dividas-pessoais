import pytest
from fastapi.testclient import TestClient
from src.server import app
from datetime import datetime

client = TestClient(app)

def test_metrics_endpoint():
    response = client.get("/api/v1/metrics")
    assert response.status_code == 200
    
    data = response.json()
    # Verifica estrutura da resposta
    assert "timestamp" in data
    assert "system" in data
    assert "logs" in data
    assert "app_info" in data
    
    # Verifica métricas do sistema
    system = data["system"]
    assert "cpu_percent" in system
    assert "memory_percent" in system
    assert "disk_percent" in system
    
    # Verifica métricas de logs
    logs = data["logs"]
    assert "access_log_size" in logs
    assert "error_log_size" in logs
    
    # Verifica informações da aplicação
    app_info = data["app_info"]
    assert "version" in app_info
    assert "environment" in app_info

def test_health_check_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "version" in data
    assert "uptime" in data
    
    # Verifica formato do timestamp
    timestamp = datetime.fromisoformat(data["timestamp"].replace("Z", "+00:00"))
    assert isinstance(timestamp, datetime)

def test_metrics_performance():
    # Testa o tempo de resposta do endpoint
    start_time = datetime.now()
    response = client.get("/api/v1/metrics")
    end_time = datetime.now()
    
    assert response.status_code == 200
    # Verifica se a resposta é rápida (menos de 1 segundo)
    assert (end_time - start_time).total_seconds() < 1

@pytest.mark.parametrize("endpoint", [
    "/api/v1/metrics",
    "/api/v1/health"
])
def test_endpoints_content_type(endpoint):
    response = client.get(endpoint)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

def test_metrics_values_range():
    response = client.get("/api/v1/metrics")
    data = response.json()
    
    # Verifica se os valores estão dentro dos ranges esperados
    system = data["system"]
    assert 0 <= system["cpu_percent"] <= 100
    assert 0 <= system["memory_percent"] <= 100
    assert 0 <= system["disk_percent"] <= 100 