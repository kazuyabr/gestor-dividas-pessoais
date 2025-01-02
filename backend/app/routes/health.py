from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "API esta funcionando normalmente"
    }
