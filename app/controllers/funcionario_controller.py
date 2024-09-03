from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import funcionario_service
from app.models.funcionario import Funcionario, FuncionarioResponse
from app.services.funcionario_service import FuncionarioService
from app.repositories.funcionario_repository import FuncionarioRepository
from app.schemas.funcionarioDTO import FuncionarioOut, FuncionarioCreate
from app.database.session import get_db

router = APIRouter()

# construtor
def get_funcionario_service(db: Session = Depends(get_db)):
    repository = FuncionarioRepository(db)
    return FuncionarioService(repository)

@router.post("/funcionarios/", response_model=FuncionarioResponse)
async def create_funcionario(
    funcionario: FuncionarioCreate,
    service: FuncionarioService = Depends(get_funcionario_service)
):
    funcionario_model = Funcionario(**funcionario.dict())
    created_funcionario = service.create_funcionario(funcionario_model)
    return created_funcionario

@router.get("/funcionarios/", response_model=list[FuncionarioResponse])
async def get_funcionarios(service: FuncionarioService = Depends(get_funcionario_service)):
    return service.get_all_funcionarios()

@router.get("/funcionarios/{funcionario_id}", response_model=FuncionarioResponse)
async def get_funcionario(funcionario_id: int, service: FuncionarioService = Depends(get_funcionario_service)):
    funcionario = service.get_funcionario_by_id(funcionario_id)
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return funcionario

@router.put("/funcionarios/{funcionario_id}", response_model=FuncionarioResponse)
async def update_funcionario(
    funcionario_id: int,
    funcionario: FuncionarioCreate,
    service: FuncionarioService = Depends(get_funcionario_service)
):
    funcionario_model = Funcionario(**funcionario.dict())
    updated_funcionario = service.update_funcionario(funcionario_id, funcionario_model)
    if not updated_funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return updated_funcionario

@router.delete("/funcionarios/{funcionario_id}", response_model=bool)
async def delete_funcionario(funcionario_id: int, service: FuncionarioService = Depends(get_funcionario_service)):
    deleted = service.delete_funcionario(funcionario_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return deleted
