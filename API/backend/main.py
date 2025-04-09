from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
import pandas as pd
import numpy as np
import os

# Configuração dos Middlewares
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar o arquivo CSV
dir = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(f"{dir}/dados/Relatorio_cadop.csv", delimiter=";", encoding="utf-8")

# Rota para buscar operadoras
@app.get("/api/buscar")
def buscar_operadora(
    registro: str = Query(default=None),
    cnpj: str = Query(default=None),
    razao_social: str = Query(default=None)
):
    if not registro and not cnpj and not razao_social:
        return {"error": "Preencha pelo menos um parâmetro"}
    
    filtro = pd.Series([False] * len(df))

    if registro is not None:
        if(not registro.isnumeric()):
            return {"error": "O registro deve conter apenas números."}
        
        filtro |= df["Registro_ANS"].astype(str).str.contains(registro, na=False, case=False)

    if cnpj is not None:
        if(not cnpj.isnumeric()):
            return {"error": "O registro deve conter apenas números."}

        if len(cnpj) != 14:
            return {"error": "O CNPJ deve conter 14 dígitos."}
        filtro |= df["CNPJ"].astype(str).str.contains(cnpj, na=False, case=False)

    if razao_social is not None:
        filtro |= df["Razao_Social"].astype(str).str.contains(razao_social, na=False, case=False)

    resultados = df[filtro]

    if resultados.empty:
        return {"error": "Nenhum resultado encontrado."}

    resultados = resultados.replace([np.inf, -np.inf], np.nan).fillna("N/A")

    return {"resultados": resultados.to_dict(orient="records")}