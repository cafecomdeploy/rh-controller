from typing import List
from app.models.funcionario import Funcionario
from app.repositories.funcionario_repository import FuncionarioRepository

class FuncionarioService:
    def __init__(self, funcionario_repository:  FuncionarioRepository) :
        self.funcionario_repository = funcionario_repository

    def create_funcionario(self, funcionario: Funcionario) -> Funcionario:
        return self.funcionario_repository.create(funcionario)
    
    def get_funcionario(self) -> List[Funcionario]:
        return self.funcionario_repository.get_all()