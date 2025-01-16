from fastapi import Request
import time
import logging
from datetime import datetime

access_logger = logging.getLogger("access")
error_logger = logging.getLogger("error")

async def monitoring_middleware(request: Request, call_next):
    start_time = time.time()
    timestamp = datetime.utcnow().isoformat()
    
    try:
        response = await call_next(request)
        
        process_time = time.time() - start_time
        access_logger.info({
            "timestamp": timestamp,
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "processing_time": f"{process_time:.2f}s",
            "client_ip": request.client.host if request.client else None,
            "user_agent": request.headers.get("user-agent")
        })
        
        return response
        
    except Exception as e:
        process_time = time.time() - start_time
        error_logger.error({
            "timestamp": timestamp,
            "method": request.method,
            "path": request.url.path,
            "error": str(e),
            "processing_time": f"{process_time:.2f}s",
            "client_ip": request.client.host if request.client else None,
            "user_agent": request.headers.get("user-agent")
        })
        raise 