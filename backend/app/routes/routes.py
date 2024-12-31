from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database.database import SessionLocal
from ..models import models
from ..schemas import schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas de Usuário
@router.post("/usuarios/", response_model=schemas.Usuario)
def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@router.get("/usuarios/", response_model=List[schemas.Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()

# Rotas de Dívida
@router.post("/dividas/", response_model=schemas.Divida)
def criar_divida(divida: schemas.DividaCreate, usuario_id: int, db: Session = Depends(get_db)):
    db_divida = models.Divida(**divida.dict(), usuario_id=usuario_id)
    db.add(db_divida)
    db.commit()
    db.refresh(db_divida)
    return db_divida

@router.get("/dividas/", response_model=List[schemas.Divida])
def listar_dividas(db: Session = Depends(get_db)):
    return db.query(models.Divida).all()

@router.get("/dividas/{divida_id}", response_model=schemas.Divida)
def obter_divida(divida_id: int, db: Session = Depends(get_db)):
    divida = db.query(models.Divida).filter(models.Divida.id == divida_id).first()
    if not divida:
        raise HTTPException(status_code=404, detail="Dívida não encontrada")
    return divida

@router.delete("/dividas/{divida_id}")
def deletar_divida(divida_id: int, db: Session = Depends(get_db)):
    divida = db.query(models.Divida).filter(models.Divida.id == divida_id).first()
    if not divida:
        raise HTTPException(status_code=404, detail="Dívida não encontrada")
    db.delete(divida)
    db.commit()
    return {"message": "Dívida deletada com sucesso"}
