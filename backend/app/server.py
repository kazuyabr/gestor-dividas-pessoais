from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import routes
from .database.database import engine
from .models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gestor de Dívidas API",
    description="API para gerenciamento de dívidas pessoais",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router, prefix="/api/v1")
