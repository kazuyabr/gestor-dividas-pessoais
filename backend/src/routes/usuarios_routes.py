from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..models import models
from ..schemas.usuario_schema import Usuario, UsuarioCreate
from ..auth.auth import get_password_hash

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

@router.post("/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=get_password_hash(usuario.senha)  # Hash da senha antes de salvar
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
@router.get("/", response_model=List[Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    """
    Lista todos os usuários cadastrados.
    
    Returns:
    - Lista de usuários com seus dados
    """
    return db.query(models.Usuario).all()
