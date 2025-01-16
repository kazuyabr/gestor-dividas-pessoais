from fastapi import APIRouter
from datetime import datetime, timezone
from typing import Dict, Any

router = APIRouter()

@router.get("/health", tags=["monitoring"])
async def health_check() -> Dict[str, Any]:
    """
    Verifica a saúde da aplicação.
    """
    return {
        "status": "healthy",
        "message": "API esta funcionando normalmente",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
