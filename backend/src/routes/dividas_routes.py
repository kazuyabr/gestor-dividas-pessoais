from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..models.models import Divida as DividaModel
from ..schemas.divida_schema import DividaBase, DividaResponse, DividaUpdate

router = APIRouter(
    prefix="/dividas",
    tags=["dividas"]
)

@router.post("/", response_model=DividaResponse)
def criar_divida(divida: DividaBase, usuario_id: int, db: Session = Depends(get_db)):
    db_divida = DividaModel(**divida.dict(), usuario_id=usuario_id)
    db.add(db_divida)
    db.commit()
    db.refresh(db_divida)
    return db_divida

@router.get("/", response_model=List[DividaResponse])
def listar_dividas(db: Session = Depends(get_db)):
    return db.query(DividaModel).all()

@router.get("/{divida_id}", response_model=DividaResponse)
def obter_divida(divida_id: int, db: Session = Depends(get_db)):
    divida = db.query(DividaModel).filter(DividaModel.id == divida_id).first()
    if not divida:
        raise HTTPException(status_code=404, detail="Dívida não encontrada")
    return divida

@router.put("/{divida_id}", response_model=DividaResponse)
def atualizar_divida(divida_id: int, divida: DividaUpdate, db: Session = Depends(get_db)):
    db_divida = db.query(DividaModel).filter(DividaModel.id == divida_id).first()
    if not db_divida:
        raise HTTPException(status_code=404, detail="Dívida não encontrada")
    
    for key, value in divida.dict(exclude_unset=True).items():
        setattr(db_divida, key, value)
    
    db.commit()
    db.refresh(db_divida)
    return db_divida

@router.delete("/{divida_id}")
def deletar_divida(divida_id: int, db: Session = Depends(get_db)):
    divida = db.query(DividaModel).filter(DividaModel.id == divida_id).first()
    if not divida:
        raise HTTPException(status_code=404, detail="Dívida não encontrada")
    
    db.delete(divida)
    db.commit()
    return {"message": "Dívida deletada com sucesso"}