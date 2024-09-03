from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.funcionario import Funcionario

class FuncionarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, funcionario: Funcionario) -> Funcionario:
        self.db.add(funcionario)
        self.db.commit()
        self.db.refresh(funcionario)
        return funcionario

    def get_all(self):
        return self.db.query(Funcionario).all()

    def get_by_id(self, funcionario_id: int):
        return self.db.query(Funcionario).filter(Funcionario.id == funcionario_id).first()

    def update(self, funcionario_id: int, updated_funcionario: Funcionario) -> Funcionario:
        existing_funcionario = self.get_by_id(funcionario_id)
        if not existing_funcionario:
            return None
        for key, value in vars(updated_funcionario).items():
            if key != "_sa_instance_state":
                setattr(existing_funcionario, key, value)
        self.db.commit()
        self.db.refresh(existing_funcionario)
        return existing_funcionario

    def delete(self, funcionario_id: int) -> bool:
        funcionario = self.get_by_id(funcionario_id)
        if funcionario:
            self.db.delete(funcionario)
            self.db.commit()
            return True
        return False