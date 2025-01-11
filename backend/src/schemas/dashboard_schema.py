from pydantic import BaseModel
from datetime import datetime
from typing import List

class DashboardSummary(BaseModel):
    total_dividas: int
    total_valor_pendente: float
    dividas_pagas: int
    dividas_vencidas: int

class DividaResumo(BaseModel):
    id: int
    titulo: str
    valor: float
    data_vencimento: datetime
    status: str
