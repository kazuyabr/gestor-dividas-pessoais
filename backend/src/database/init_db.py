from .database import Base, engine
from ..models.models import Usuario, Divida

def init_database():
    print("Criando todas as tabelas...")
    Base.metadata.drop_all(bind=engine)  # Remove todas as tabelas existentes
    Base.metadata.create_all(bind=engine)  # Cria todas as tabelas novamente
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    init_database()
