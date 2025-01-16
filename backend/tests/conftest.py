import sys
import os
from pathlib import Path
import pytest
import logging
from src.core.monitoring import setup_logging
from src.config.settings import settings

# Adiciona o diretório raiz do projeto ao PYTHONPATH
root_dir = str(Path(__file__).parent.parent)
sys.path.append(root_dir)

@pytest.fixture(autouse=True)
def setup_test_environment():
    """Configura o ambiente de teste automaticamente para todos os testes"""
    # Configura diretório de logs para testes
    test_log_dir = "test_logs"
    os.makedirs(test_log_dir, exist_ok=True)
    
    # Guarda configuração original
    original_log_dir = settings.log_dir
    
    # Atualiza para diretório de teste
    settings.log_dir = test_log_dir
    
    # Configura logging
    setup_logging()
    
    yield
    
    # Fecha todos os handlers de log
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    for logger in loggers:
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)
    
    # Limpa logs após os testes
    if os.path.exists(test_log_dir):
        for file in os.listdir(test_log_dir):
            try:
                os.remove(os.path.join(test_log_dir, file))
            except PermissionError:
                pass  # Ignora se ainda não conseguir deletar
        try:
            os.rmdir(test_log_dir)
        except (PermissionError, OSError):
            pass  # Ignora se não conseguir deletar o diretório
    
    # Restaura configuração original
    settings.log_dir = original_log_dir
