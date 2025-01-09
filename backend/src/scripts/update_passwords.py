from sqlalchemy.orm import Session
from ..database.database import SessionLocal, engine
from ..models.models import Usuario
from ..auth.auth import get_password_hash

def update_existing_passwords():
    db = SessionLocal()
    usuarios = db.query(Usuario).all()
    
    for usuario in usuarios:
        # Defina uma senha padrão temporária ou use uma lógica específica
        nova_senha = get_password_hash("senha123")
        usuario.senha = nova_senha
    
    db.commit()
    db.close()

if __name__ == "__main__":
    update_existing_passwords()
