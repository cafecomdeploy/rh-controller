from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.schemas.cargoDTO import CargoCreate, CargoUpdate, CargoResponse
from app.services.cargo_service import CargoService

router = APIRouter()

@router.post("/cargos", response_model=CargoResponse)
async def create_cargo(cargo_create: CargoCreate, db: Session = Depends(get_db)) -> CargoResponse:
    cargo_service = CargoService(db)
    cargo = cargo_service.create_cargo(cargo_create)
    return CargoResponse.from_orm(cargo)

@router.get("/cargos/{cargo_id}", response_model=CargoResponse)
async def get_cargo(cargo_id: int, db: Session = Depends(get_db)) -> CargoResponse:
    cargo_service = CargoService(db)
    cargo = cargo_service.get_cargo(cargo_id)
    if not cargo:
        raise HTTPException(status_code=404, detail="Cargo not found")
    return CargoResponse.from_orm(cargo)

@router.get("/cargos", response_model=List[CargoResponse])
async def get_all_cargos(db: Session = Depends(get_db)) -> List[CargoResponse]:
    cargo_service = CargoService(db)
    cargos = cargo_service.get_all_cargos()
    return [CargoResponse.from_orm(cargo) for cargo in cargos]

@router.put("/cargos/{cargo_id}", response_model=CargoResponse)
async def update_cargo(cargo_id: int, cargo_update: CargoUpdate, db: Session = Depends(get_db)) -> CargoResponse:
    cargo_service = CargoService(db)
    cargo = cargo_service.update_cargo(cargo_id, cargo_update)
    if not cargo:
        raise HTTPException(status_code=404, detail="Cargo not found")
    return CargoResponse.from_orm(cargo)

@router.delete("/cargos/{cargo_id}", response_model=dict)
async def delete_cargo(cargo_id: int, db: Session = Depends(get_db)) -> dict:
    cargo_service = CargoService(db)
    success = cargo_service.delete_cargo(cargo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Cargo not found")
    return {"status": "Cargo deleted successfully"}
