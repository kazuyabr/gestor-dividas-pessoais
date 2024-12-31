import uvicorn
from app.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.server:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.API_RELOAD
    )
