from typing import List
from app.models.funcionario import Funcionario

class FuncionarioRepository:
    def __init__(self):
        self.funcionarios = []
        self._id_counter = 1

    def create(self, funcionario: Funcionario) -> Funcionario:
        funcionario.id = self._id_counter
        self.funcionarios.append(funcionario)
        self._id_counter += 1
        return funcionario

    def get_all(self) -> List[Funcionario]:
        return self.funcionarios
