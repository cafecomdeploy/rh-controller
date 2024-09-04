from pydantic import BaseModel
from typing import Optional, List

class CargoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class CargoCreate(CargoBase):
    pass

class CargoUpdate(CargoBase):
    pass

class CargoResponse(CargoBase):
    id: int
    funcionarios: List[str] = []

    class Config:
        from_attributes = True
