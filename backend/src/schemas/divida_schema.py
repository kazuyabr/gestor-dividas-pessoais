from pydantic import Field
from datetime import datetime
from .base_schema import BaseSchema

class DividaBase(BaseSchema):
    valor: float = Field(..., description="Valor monetário da dívida", example=1500.50)
    data_vencimento: datetime = Field(..., description="Data de vencimento")
    descricao: str = Field(..., description="Descrição da dívida")

class DividaCreate(DividaBase):
    pass

class Divida(DividaBase):
    id: int
    usuario_id: int
    data_criacao: datetime
