from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.config import Base
from pydantic import BaseModel
from datetime import date

class Funcionario(Base):
    __tablename__ = "funcionario"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, index=True)
    datanascimento= Column(Date)
    cargo_id = Column(Integer, ForeignKey('cargos.id'))


    cargo = relationship("Cargo", back_populates="funcionarios")

class FuncionarioResponse(BaseModel):
    id: int
    nome: str
    datanascimento: date
    cargo_id: int

    class Config:
        orm_mode = True
        from_attributes = True  # Permite utilizar from_orm