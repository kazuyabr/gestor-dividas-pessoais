from fastapi import Request
import time
import logging
import os
from datetime import datetime
from ..config.settings import settings

# Configurar loggers
access_logger = logging.getLogger("access")
error_logger = logging.getLogger("error")

async def monitoring_middleware(request: Request, call_next):
    start_time = time.time()
    
    try:
        response = await call_next(request)
        
        process_time = time.time() - start_time
        log_data = {
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "processing_time": f"{process_time:.2f}s",
            "timestamp": datetime.now().isoformat()
        }
        
        access_logger.info(str(log_data))
        return response
        
    except Exception as e:
        process_time = time.time() - start_time
        error_logger.error(f"Error: {str(e)}, Time: {process_time:.2f}s")
        raise 