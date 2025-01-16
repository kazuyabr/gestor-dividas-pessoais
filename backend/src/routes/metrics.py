from fastapi import APIRouter, Depends
from typing import Dict, Any
import psutil
import os
from datetime import datetime
from ..config.settings import settings
import logging

router = APIRouter()
logger = logging.getLogger("access")

@router.get("/metrics", tags=["monitoring"])
async def get_metrics() -> Dict[str, Any]:
    """
    Retorna métricas do sistema e da aplicação.
    """
    # Métricas do sistema
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    # Métricas de logs
    log_metrics = {
        "access_log_size": os.path.getsize(f"{settings.log_dir}/access.log") if os.path.exists(f"{settings.log_dir}/access.log") else 0,
        "error_log_size": os.path.getsize(f"{settings.log_dir}/error.log") if os.path.exists(f"{settings.log_dir}/error.log") else 0
    }
    
    metrics = {
        "timestamp": datetime.utcnow().isoformat(),
        "system": {
            "cpu_percent": cpu_percent,
            "memory_percent": memory.percent,
            "disk_percent": disk.percent,
        },
        "logs": log_metrics,
        "app_info": {
            "version": settings.API_VERSION,
            "environment": os.getenv("ENVIRONMENT", "development")
        }
    }
    
    logger.info("Metrics collected", extra={"metrics": metrics})
    return metrics

@router.get("/health", tags=["monitoring"])
async def health_check() -> Dict[str, Any]:
    """
    Verifica a saúde da aplicação e suas dependências.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": settings.API_VERSION,
        "uptime": psutil.boot_time()
    } 