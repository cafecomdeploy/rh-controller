from typing import List
from fastapi import APIRouter, HTTPException
from app.models.funcionario import Funcionario, FuncionarioResponse
from app.services.funcionario_service import FuncionarioService
from app.repositories.funcionario_repository import FuncionarioRepository

router = APIRouter()  # Usando APIRouter em vez de FastAPI

funcionario_repository = FuncionarioRepository()
funcionario_service = FuncionarioService(funcionario_repository)

@router.get("/retorna_func", response_model=List[FuncionarioResponse])
async def get_funcionarios() -> List[FuncionarioResponse]:
    try:
        funcionarios: List[Funcionario] = funcionario_service.get_funcionario()
        # Convertendo a lista de Funcionario para FuncionarioResponse usando list 
        return [FuncionarioResponse.from_orm(funcionario) for funcionario in funcionarios]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

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
