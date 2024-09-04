from sqlalchemy.orm import Session
from app.repositories.cargo_repository import CargoRepository
from app.models.cargo import Cargo
from app.schemas.cargoDTO import CargoCreate, CargoUpdate
from typing import List, Optional

class CargoService:
    def __init__(self, db: Session):
        self.cargo_repository = CargoRepository(db)

    def create_cargo(self, cargo_create: CargoCreate) -> Cargo:
        cargo = Cargo(**cargo_create.dict())
        return self.cargo_repository.create(cargo)

    def get_cargo(self, cargo_id: int) -> Optional[Cargo]:
        return self.cargo_repository.get_by_id(cargo_id)

    def get_all_cargos(self) -> List[Cargo]:
        return self.cargo_repository.get_all()

    def update_cargo(self, cargo_id: int, cargo_update: CargoUpdate) -> Optional[Cargo]:
        cargo = self.cargo_repository.get_by_id(cargo_id)
        if not cargo:
            return None
        for key, value in cargo_update.dict(exclude_unset=True).items():
            setattr(cargo, key, value)
        return self.cargo_repository.update(cargo)

    def delete_cargo(self, cargo_id: int) -> bool:
        cargo = self.cargo_repository.get_by_id(cargo_id)
        if cargo:
            self.cargo_repository.delete(cargo)
            return True
        return False
