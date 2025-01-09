from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .routes import usuarios_routes, dividas_routes, health, auth_routes
from .database.database import engine
from .models import models
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gestor de Dívidas Pessoais API",
    description="""
    # Gestor de Dívidas Pessoais
    
    API REST para gerenciamento completo de dívidas pessoais.
    
    ## Funcionalidades Principais
    
    * **Usuários**
        * Cadastro de usuários
        * Autenticação segura
        * Gerenciamento de perfil
        
    * **Dívidas**
        * Cadastro de dívidas
        * Atualização de status
        * Filtros e buscas
        * Categorização
        
    * **Relatórios**
        * Visão geral de dívidas
        * Análise por período
        * Estatísticas
        
    ## Autenticação
    
    A API utiliza autenticação via JWT (JSON Web Token). Para acessar endpoints protegidos:
    1. Faça login para obter o token
    2. Inclua o token no header Authorization
    
    ## Códigos de Status
    
    * `200` - Sucesso
    * `201` - Criado com sucesso
    * `400` - Erro nos dados enviados
    * `401` - Não autorizado
    * `404` - Recurso não encontrado
    * `500` - Erro interno
    
    ## Formatos
    
    * Datas: ISO 8601 (YYYY-MM-DD)
    * Valores monetários: Decimal com 2 casas
    * Requisições/Respostas: JSON
    """,
    version="1.0.0",
    terms_of_service="http://gestordividas.com/terms/",
    contact={
        "name": "Suporte Técnico",
        "url": "http://gestordividas.com/support",
        "email": "suporte@gestordividas.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Tags para organização da documentação
tags_metadata = [
    {
        "name": "usuarios",
        "description": "Operações com usuários. Inclui cadastro, autenticação e gerenciamento.",
    },
    {
        "name": "dividas",
        "description": "Gerenciamento de dívidas. Cadastro, atualização, consultas e exclusão.",
    },
    {
        "name": "relatorios",
        "description": "Geração de relatórios e análises estatísticas.",
    },
    {
        "name": "health",
        "description": "Verificação de saúde e status da API.",
    }
]

app.openapi_tags = tags_metadata

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(
    usuarios_routes.router,
    prefix="/api/v1",
    tags=["usuarios"]
)

app.include_router(
    dividas_routes.router,
    prefix="/api/v1",
    tags=["dividas"]
)

app.include_router(
    health.router,
    prefix="/api/v1",
    tags=["health"]
)

app.include_router(
    auth_routes.router,
    prefix="/api/v1/auth",
    tags=["auth"]
)