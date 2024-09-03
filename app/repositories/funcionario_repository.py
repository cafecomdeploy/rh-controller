from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.funcionario import Funcionario

class FuncionarioRepository:
    def __init__(self, db: Session):
        self.funcionarios = []
        self._id_counter = 1
        self.db = db

    def create(self, funcionario: Funcionario) -> Funcionario:
        funcionario.id = self._id_counter
        self.funcionarios.append(funcionario)
        self._id_counter += 1
        return funcionario

    def get_all(self) -> List[Funcionario]:
        return self.funcionarios
    
    def get_funcionario(self, funcionario_id: int) -> Optional[Funcionario]:
        return self.db.query(Funcionario).filter(Funcionario.id == funcionario_id).first()
