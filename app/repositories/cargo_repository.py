from sqlalchemy.orm import Session
from app.models.cargo import Cargo
from typing import List, Optional

class CargoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, cargo: Cargo) -> Cargo:
        self.db.add(cargo)
        self.db.commit()
        self.db.refresh(cargo)
        return cargo

    def get_by_id(self, cargo_id: int) -> Optional[Cargo]:
        return self.db.query(Cargo).filter(Cargo.id == cargo_id).first()

    def get_all(self) -> List[Cargo]:
        return self.db.query(Cargo).all()

    def update(self, cargo: Cargo) -> Cargo:
        self.db.commit()
        self.db.refresh(cargo)
        return cargo

    def delete(self, cargo: Cargo):
        self.db.delete(cargo)
        self.db.commit()
