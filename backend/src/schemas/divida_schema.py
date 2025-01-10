from pydantic import Field
from datetime import datetime
from typing import Optional
from .base_schema import BaseSchema

class DividaBase(BaseSchema):
    valor: float = Field(..., description="Valor monetário da dívida")
    data_vencimento: datetime = Field(..., description="Data de vencimento")
    descricao: str = Field(..., description="Descrição da dívida")
    status: str = Field(default="Pendente", description="Status da dívida")
    observacoes: Optional[str] = Field(None, description="Observações adicionais")

class DividaUpdate(BaseSchema):
    valor: Optional[float] = Field(None, description="Valor monetário da dívida")
    data_vencimento: Optional[datetime] = Field(None, description="Data de vencimento")
    descricao: Optional[str] = Field(None, description="Descrição da dívida")
    status: Optional[str] = Field(None, description="Status da dívida")
    observacoes: Optional[str] = Field(None, description="Observações adicionais")

class DividaResponse(DividaBase):
    id: int
    usuario_id: int