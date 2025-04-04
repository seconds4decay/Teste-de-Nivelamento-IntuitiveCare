from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import numpy as np
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dir = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(f"{dir}/dados/Relatorio_cadop.csv", delimiter=";", encoding="utf-8")

class BuscaOperadora(BaseModel):
    registro: str | None = None
    cnpj: str | None = None
    razao_social: str | None = None

@app.post("/api/buscar")
def buscar_operadora(dados: BuscaOperadora):

    if not dados.registro and not dados.cnpj and not dados.razao_social:
        return {"error": "Preencha pelo menos um parâmetro"}
    
    filtro = pd.Series([False] * len(df))

    if dados.registro is not None:
        if(not dados.registro.isnumeric()):
            return {"error": "O registro deve conter apenas números."}

        filtro |= df["Registro_ANS"].astype(str).str.contains(str(dados.registro), na=False, case=False)
    if dados.cnpj is not None:
        if(not dados.cnpj.isnumeric()):
            return {"error": "O CNPJ deve conter apenas números."}
        
        if(len(dados.cnpj) != 14):
            return {"error": "O CNPJ deve conter 14 dígitos."}

        filtro |= df["CNPJ"].astype(str).str.contains(str(dados.cnpj), na=False, case=False)
    if dados.razao_social is not None:
        filtro |= df["Razao_Social"].astype(str).str.contains(str(dados.razao_social), na=False, case=False)

    resultados = df[filtro]

    if resultados.empty:
        return {"error": "Nenhum resultado encontrado."}
    
    resultados = resultados.replace([np.inf, -np.inf], np.nan).fillna("N/A")

    return { "resultados": resultados.to_dict(orient="records")}