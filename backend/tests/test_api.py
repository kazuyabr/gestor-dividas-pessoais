from fastapi.testclient import TestClient
from src.server import app
import random
import string
from datetime import datetime, timedelta

client = TestClient(app)

def gerar_email_unico():
    """Gera um email único para testes"""
    caracteres = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(caracteres) for _ in range(10))
    return f"test_{random_string}@test.com"

def test_health_check():
    """Testa o endpoint de health check"""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["message"] == "API esta funcionando normalmente"
    # Não vamos verificar o timestamp pois ele muda a cada execução

def test_ciclo_usuario():
    """Testa o ciclo completo de um usuário: criação e deleção"""
    # Criação
    email_unico = gerar_email_unico()
    user_data = {
        "nome": "Test User",
        "email": email_unico,
        "senha": "test123"
    }
    
    response = client.post("/api/v1/usuarios/", json=user_data)
    assert response.status_code == 200
    
    data = response.json()
    user_id = data["id"]
    assert data["nome"] == user_data["nome"]
    assert data["email"] == email_unico
    
    # Deleção
    delete_response = client.delete(f"/api/v1/usuarios/{user_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Usuário deletado com sucesso"

def test_ciclo_divida():
    """Testa o ciclo completo: criação de usuário, dívida e deleção"""
    # Cria usuário
    email_unico = gerar_email_unico()
    user_response = client.post(
        "/api/v1/usuarios/",
        json={
            "nome": "Test User",
            "email": email_unico,
            "senha": "test123"
        }
    )
    user_id = user_response.json()["id"]
    
    # Cria dívida
    divida_data = {
        "valor": 1500.00,
        "data_vencimento": (datetime.now() + timedelta(days=30)).isoformat(),
        "descricao": "Test Divida",
        "status": "Pendente",
        "observacoes": "Teste de criação de dívida"
    }
    
    divida_response = client.post(
        f"/api/v1/dividas/?usuario_id={user_id}",
        json=divida_data
    )
    
    assert divida_response.status_code == 200
    divida_id = divida_response.json()["id"]
    
    # Deleta dívida
    delete_divida_response = client.delete(f"/api/v1/dividas/{divida_id}")
    assert delete_divida_response.status_code == 200
    
    # Deleta usuário
    delete_user_response = client.delete(f"/api/v1/usuarios/{user_id}")
    assert delete_user_response.status_code == 200
    assert delete_user_response.json()["message"] == "Usuário deletado com sucesso"