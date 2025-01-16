import pytest
from fastapi.testclient import TestClient
from src.server import app
import logging
import os
from src.config.settings import settings
from src.core.monitoring import setup_logging
import time

client = TestClient(app)

@pytest.fixture
def setup_test_logs(monkeypatch):
    # Configura diretório de teste para logs
    test_log_dir = "test_logs"
    monkeypatch.setattr(settings, "log_dir", test_log_dir)
    os.makedirs(test_log_dir, exist_ok=True)
    
    # Reconfigura o logging com o novo diretório
    setup_logging()
    
    yield test_log_dir
    
    # Fecha todos os handlers antes de tentar remover os arquivos
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    for logger in loggers:
        handlers = logger.handlers[:]
        for handler in handlers:
            logger.removeHandler(handler)
            if hasattr(handler, 'close'):
                handler.close()
    
    # Aguarda um momento para garantir que os arquivos foram liberados
    time.sleep(0.1)
    
    # Limpa logs após os testes
    if os.path.exists(test_log_dir):
        for file in os.listdir(test_log_dir):
            try:
                os.remove(os.path.join(test_log_dir, file))
            except PermissionError:
                print(f"Não foi possível remover {file}, será removido na próxima execução")
        try:
            os.rmdir(test_log_dir)
        except (PermissionError, OSError):
            print(f"Não foi possível remover o diretório {test_log_dir}, será removido na próxima execução")

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

class TestingLogHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.records = []

    def emit(self, record):
        self.records.append(record)

def test_middleware_timing():
    handler = TestingLogHandler()
    logger = logging.getLogger("access")
    logger.addHandler(handler)
    
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    
    assert any("processing_time" in str(record.__dict__) for record in handler.records)
    logger.removeHandler(handler) 