from fastapi.testclient import TestClient
from src.server import app
import random
import string

client = TestClient(app)

def gerar_email_unico():
    caracteres = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(caracteres) for _ in range(10))
    return f"test_{random_string}@test.com"

def test_login_usuario_inexistente():
    """Testa tentativa de login com usuário que não existe"""
    login_data = {
        "username": "naoexiste@test.com",
        "password": "qualquersenha123"
    }
    response = client.post("/api/v1/auth/token", data=login_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário não encontrado"

def test_login_senha_incorreta():
    """Testa tentativa de login com senha incorreta"""
    # Primeiro cria um usuário
    email = gerar_email_unico()
    user_data = {
        "nome": "Test User",
        "email": email,
        "senha": "senha123"
    }
    client.post("/api/v1/usuarios/", json=user_data)
    
    # Tenta login com senha errada
    login_data = {
        "username": email,
        "password": "senhaerrada123"
    }
    response = client.post("/api/v1/auth/token", data=login_data)
    assert response.status_code == 401
    assert response.json()["detail"] == "Senha incorreta"
