from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List

class UsuarioBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nome: str
    email: str

class UsuarioCreate(UsuarioBase):
    senha: str

class Usuario(UsuarioBase):
    id: int

class DividaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    valor: float
    data_vencimento: datetime
    descricao: str

class DividaCreate(DividaBase):
    pass

class Divida(DividaBase):
    id: int
    usuario_id: int
