from pydantic import Field, EmailStr
from datetime import datetime
from .base_schema import BaseSchema

class UsuarioBase(BaseSchema):
    nome: str = Field(..., description="Nome completo do usuário")
    email: EmailStr = Field(..., description="Email do usuário")

class UsuarioCreate(UsuarioBase):
    senha: str = Field(..., description="Senha do usuário", min_length=6)

class Usuario(UsuarioBase):
    id: int
    data_criacao: datetime
