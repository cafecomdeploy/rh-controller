from pydantic import BaseModel

class FuncionarioBase(BaseModel):
    nome: str
    cargo: str
    salario: int

class FuncionarioCreate(FuncionarioBase):
    pass

class FuncionarioUpdate(FuncionarioBase):
    pass

class FuncionarioOut(FuncionarioBase):
    id: int

    class Config:
        from_attributes = True
