from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import routes, health
from .database.database import engine
from .models import models
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")
