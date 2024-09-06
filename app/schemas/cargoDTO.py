from pydantic import BaseModel
from typing import Optional, List
from app.models.funcionario import FuncionarioResponse

class CargoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class CargoCreate(CargoBase):
    pass

class CargoUpdate(CargoBase):
    pass

class CargoResponse(CargoBase):
    id: int
    funcionarios: List[FuncionarioResponse] = []

    class Config:
        from_attributes = True
