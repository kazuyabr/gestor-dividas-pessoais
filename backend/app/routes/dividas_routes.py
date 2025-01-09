from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..models import models
from ..schemas.divida_schema import Divida, DividaCreate

router = APIRouter(
    prefix="/dividas",
    tags=["dividas"]
)

@router.get("/", response_model=List[Divida])
def listar_dividas(db: Session = Depends(get_db)):
    return db.query(models.Divida).all()

@router.post("/", response_model=Divida)
def criar_divida(divida: DividaCreate, usuario_id: int, db: Session = Depends(get_db)):
    db_divida = models.Divida(**divida.model_dump(), usuario_id=usuario_id)
    db.add(db_divida)
    db.commit()
    db.refresh(db_divida)
    return db_divida

@router.get("/{divida_id}", response_model=Divida)
def obter_divida(divida_id: int, db: Session = Depends(get_db)):
    divida = db.query(models.Divida).filter(models.Divida.id == divida_id).first()
    if not divida:
        raise HTTPException(status_code=404, detail="Dívida não encontrada")
    return divida

@router.delete("/{divida_id}")
def deletar_divida(divida_id: int, db: Session = Depends(get_db)):
    """
    Remove uma dívida do sistema.
    
    Parameters:
    - **divida_id**: ID da dívida a ser removida
    
    Returns:
    - Mensagem de sucesso
    """
    divida = db.query(models.Divida).filter(models.Divida.id == divida_id).first()
    if not divida:
        raise HTTPException(status_code=404, detail="Dívida não encontrada")
    db.delete(divida)
    db.commit()
    return {"message": "Dívida deletada com sucesso"}
