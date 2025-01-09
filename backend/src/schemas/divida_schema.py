from pydantic import Field
from datetime import datetime
from .base_schema import BaseSchema
from typing import Optional

class DividaBase(BaseSchema):
    valor: float = Field(..., description="Valor monetário da dívida")
    data_vencimento: datetime = Field(..., description="Data de vencimento")
    descricao: str = Field(..., description="Descrição da dívida")

class DividaCreate(DividaBase):
    pass

class Divida(DividaBase):
    id: int
    usuario_id: int
    data_criacao: Optional[datetime] = Field(default_factory=datetime.now)
