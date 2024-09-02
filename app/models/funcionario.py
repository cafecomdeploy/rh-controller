from sqlalchemy import Column, Integer, String, Date
from app.database.config import Base
from pydantic import BaseModel
from datetime import date

class Funcionario(Base):
    __tablename__ = "funcionario"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, index=True)
    datanascimento= Column(Date)
    cod_cargo = Column(Integer)

class FuncionarioResponse(BaseModel):
    id: int
    nome: str
    datanascimento: date
    cod_cargo: int

    class Config:
        orm_mode = True
        from_attributes = True  # Permite utilizar from_orm