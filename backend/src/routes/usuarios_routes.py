from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..models import models
from ..schemas.usuario_schema import Usuario, UsuarioCreate

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

@router.post("/", response_model=Usuario)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """
    Cria um novo usuário no sistema.
    
    Parameters:
    - **usuario**: Dados do usuário
        - nome: Nome completo do usuário
        - email: Email único do usuário
        - senha: Senha de acesso
    
    Returns:
    - Usuário criado com seus dados
    """
    db_usuario = models.Usuario(**usuario.model_dump())
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
