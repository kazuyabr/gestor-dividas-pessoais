from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..auth.auth import verify_password, create_access_token
from ..models.models import Usuario

router = APIRouter()

@router.post("/token", 
    response_model=dict,
    summary="Autenticação de usuário",
    description="Rota para autenticar usuário e gerar token JWT",
    responses={
        200: {
            "description": "Login realizado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                        "token_type": "bearer"
                    }
                }
            }
        },
        401: {
            "description": "Credenciais inválidas",
            "content": {
                "application/json": {
                    "example": {"detail": "Email ou senha incorretos"}
                }
            }
        }
    }
)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Autentica um usuário e retorna um token JWT.

    - **username**: Email do usuário
    - **password**: Senha do usuário
    
    Retorna um token JWT que deve ser usado no header Authorization das requisições.
    """
    user = db.query(Usuario).filter(Usuario.email == form_data.username).first()
    
    # Verifica se o usuário existe
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    
    # Verifica se a senha está correta
    if not verify_password(form_data.password, user.senha):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Senha incorreta",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
