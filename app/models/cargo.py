from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.config import Base

class Cargo(Base):
    __tablename__ = 'cargos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True, nullable=False)
    descricao = Column(String, nullable=True)

    # Relacionamento com Funcionario
    funcionarios = relationship("Funcionario", back_populates="cargo")
