from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health")
def health_check():
    """
    Verifica o status de saúde da API.
    
    Returns:
    - status: Estado atual da API
    - message: Mensagem detalhada sobre o funcionamento
    """
    return {
        "status": "healthy",
        "message": "API esta funcionando normalmente"
    }
