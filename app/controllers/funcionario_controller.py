from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import funcionario_service
from app.models.funcionario import Funcionario, FuncionarioResponse
from app.services.funcionario_service import FuncionarioService
from app.repositories.funcionario_repository import FuncionarioRepository
from app.schemas.funcionarioDTO import FuncionarioOut
from app.database.session import get_db

router = APIRouter()  # Usando APIRouter em vez de FastAPI

@router.get("/retorna_func", response_model=List[FuncionarioResponse])
async def get_funcionarios(db: Session = Depends(get_db)) -> List[FuncionarioResponse]:
    try:
        # Crie uma instância de FuncionarioService
        funcionario_service = FuncionarioService(FuncionarioRepository(db))
        
        # Chame o método get_all_funcionarios
        funcionarios: List[Funcionario] = funcionario_service.get_all_funcionarios()
        
        # Convertendo a lista de Funcionario para FuncionarioResponse usando list comprehension
        return [FuncionarioResponse.from_orm(funcionario) for funcionario in funcionarios]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/funcionarios/{funcionario_id}", response_model=FuncionarioOut)
def get_funcionario(id: int, db: Session = Depends(get_db)):
    service = FuncionarioService(db)
    funcionario = service.get_funcionario(id)
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionario not found")
    return funcionario

@router.post("/funcionarios/", response_model=FuncionarioResponse)
async def create_funcionario(funcionario: FuncionarioResponse) -> FuncionarioResponse:
    try:
        # Convert FuncionarioResponse to Funcionario (modelo SQLAlchemy)
        funcionario_model = Funcionario(**funcionario.model_dump())

        # Create funcionario using the service
        func = funcionario_service.create_funcionario(funcionario_model)

        # Convert the SQLAlchemy object to FuncionarioResponse
        funcionario_response = FuncionarioResponse.from_orm(func)
        return funcionario_response

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
