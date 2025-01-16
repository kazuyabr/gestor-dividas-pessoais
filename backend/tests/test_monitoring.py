import pytest
from fastapi.testclient import TestClient
from src.server import app
import logging
import os
from src.config.settings import settings

client = TestClient(app)

@pytest.fixture
def setup_test_logs():
    # Configura diretório de teste para logs
    test_log_dir = "test_logs"
    settings.log_dir = test_log_dir
    os.makedirs(test_log_dir, exist_ok=True)
    yield test_log_dir
    # Limpa logs após os testes
    for file in os.listdir(test_log_dir):
        os.remove(os.path.join(test_log_dir, file))
    os.rmdir(test_log_dir)

def test_access_logging(setup_test_logs):
    # Faz uma requisição para gerar log
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    
    # Verifica se o arquivo de log foi criado
    access_log_path = os.path.join(setup_test_logs, "access.log")
    assert os.path.exists(access_log_path)
    
    # Verifica conteúdo do log
    with open(access_log_path) as f:
        log_content = f.read()
        assert "GET" in log_content
        assert "/api/v1/health" in log_content

def test_error_logging(setup_test_logs):
    # Faz uma requisição para uma rota inexistente
    response = client.get("/api/v1/invalid-route")
    assert response.status_code == 404
    
    # Verifica se o arquivo de log de erro foi criado
    error_log_path = os.path.join(setup_test_logs, "error.log")
    assert os.path.exists(error_log_path)

def test_log_format_json(setup_test_logs):
    settings.log_format = "json"
    response = client.get("/api/v1/health")
    
    access_log_path = os.path.join(setup_test_logs, "access.log")
    with open(access_log_path) as f:
        log_line = f.readline()
        # Verifica se o log está em formato JSON
        assert log_line.strip().startswith("{")
        assert log_line.strip().endswith("}")

def test_middleware_timing():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    
    # Verifica se o tempo de processamento está sendo registrado
    access_log = logging.getLogger("access")
    with pytest.LogCapture() as logs:
        access_log.info("Test log")
        assert "processing_time" in str(logs) 