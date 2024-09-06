from pydantic import BaseModel
from datetime import date

class FuncionarioBase(BaseModel):
    id: int
    nome: str
    datanascimento: date
    cargo_id: int

class FuncionarioCreate(FuncionarioBase):
    pass

class FuncionarioUpdate(FuncionarioBase):
    pass

class FuncionarioOut(FuncionarioBase):
    id: int

    class Config:
        from_attributes = True
