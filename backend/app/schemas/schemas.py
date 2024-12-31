from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class DividaBase(BaseModel):
    valor: float
    data_vencimento: datetime
    descricao: Optional[str] = None

class DividaCreate(DividaBase):
    pass

class Divida(DividaBase):
    id: int
    usuario_id: int

    class Config:
        from_attributes = True

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    senha: str

class Usuario(UsuarioBase):
    id: int
    dividas: List[Divida] = []

    class Config:
        from_attributes = True
