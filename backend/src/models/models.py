from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)
    dividas = relationship("Divida", back_populates="usuario")

class Divida(Base):
    __tablename__ = "dividas"
    
    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float, nullable=False)
    data_vencimento = Column(DateTime, nullable=False)
    descricao = Column(String(200))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario", back_populates="dividas")
