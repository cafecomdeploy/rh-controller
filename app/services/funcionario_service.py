from typing import List, Optional
from app.models.funcionario import Funcionario
from app.repositories.funcionario_repository import FuncionarioRepository

class FuncionarioService:
    def __init__(self, funcionario_repository: FuncionarioRepository):
        self.funcionario_repository = funcionario_repository

    def create_funcionario(self, funcionario_data: Funcionario) -> Funcionario:
        return self.funcionario_repository.create(funcionario_data)

    def get_all_funcionarios(self):
        return self.funcionario_repository.get_all()

    def get_funcionario_by_id(self, funcionario_id: int):
        return self.funcionario_repository.get_by_id(funcionario_id)

    def update_funcionario(self, funcionario_id: int, funcionario_data: Funcionario) -> Funcionario:
        return self.funcionario_repository.update(funcionario_id, funcionario_data)

    def delete_funcionario(self, funcionario_id: int) -> bool:
        return self.funcionario_repository.delete(funcionario_id)