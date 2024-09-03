from typing import List, Optional
from app.models.funcionario import Funcionario
from app.repositories.funcionario_repository import FuncionarioRepository
from app.schemas.funcionarioDTO import FuncionarioOut
from sqlalchemy.orm import Session

class FuncionarioService:
    def __init__(self, funcionario_repository:  FuncionarioRepository) :
        self.funcionario_repository = funcionario_repository

    def create_funcionario(self, funcionario: Funcionario) -> Funcionario:
        return self.funcionario_repository.create(funcionario)
    
    def get_all_funcionarios(self) -> List[Funcionario]:
        return self.funcionario_repository.get_all()
    
    def get_funcionario(self, funcionario_id: int) -> Optional[FuncionarioOut]:
        funcionario = self.funcionario_repository.get_funcionario(funcionario_id)
        if funcionario:
            return self.funcionario_repository.get_funcionario(funcionario_id)
        return None