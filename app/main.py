from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.controllers.funcionario_controller import router as funcionario_router
from app.controllers.cargo_controller import router as cargo_router
from app.database.config import engine
from app.database import base

app = FastAPI(default_response_class=JSONResponse)

# Cria as tabelas no banco de dados
base.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Inclui as rotas do funcionário
app.include_router(funcionario_router, prefix="/api", tags=["Funcionarios"])

# Inclui as rotas do cargo
app.include_router(cargo_router, prefix="/api", tags=["Cargo"])