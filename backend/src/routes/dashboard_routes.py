from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from ..database.database import get_db
from ..models.models import Divida
from ..schemas.dashboard_schema import DashboardSummary, DividaResumo
from typing import List

router = APIRouter()

@router.get("/summary", response_model=DashboardSummary)
def get_dashboard_summary(db: Session = Depends(get_db)):
    """
    Retorna um resumo estatístico das dívidas
    """
    hoje = datetime.now()
    todas_dividas = db.query(Divida).all()
    
    dividas_pagas = len([d for d in todas_dividas if d.status == "Pago"])
    dividas_vencidas = len([
        d for d in todas_dividas 
        if d.data_vencimento < hoje and d.status == "Pendente"
    ])
    
    total_pendente = sum([
        d.valor for d in todas_dividas 
        if d.status == "Pendente"
    ])
    
    return DashboardSummary(
        total_dividas=len(todas_dividas),
        total_valor_pendente=total_pendente,
        dividas_pagas=dividas_pagas,
        dividas_vencidas=dividas_vencidas
    )

@router.get("/resumo", response_model=List[DividaResumo])
def get_dashboard_resumo(db: Session = Depends(get_db)):
    """
    Retorna lista resumida de todas as dívidas
    """
    dividas = db.query(Divida).all()
    return [
        DividaResumo(
            id=d.id,
            titulo=d.descricao,
            valor=d.valor,
            data_vencimento=d.data_vencimento,
            status="Vencida" if d.data_vencimento < datetime.now() and d.status == "Pendente"
                  else d.status
        )
        for d in dividas
    ]
