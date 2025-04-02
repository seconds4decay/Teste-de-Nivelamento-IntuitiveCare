from fastapi import FastAPI, Query
from typing import List
import pandas as pd
import numpy as np
import os

app = FastAPI()

dir = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(f"{dir}/Arquivos/Relatorio_cadop.csv", delimiter=";", encoding="utf-8")

@app.get("/api/buscar")
def buscar_operadora(
    registro: int = Query(default=None),
    cnpj: str = Query(default=None),
    razao_social: str = Query(default=None)
):
    if(not registro and not cnpj and not razao_social):
        return {"error": "Preencha pelo menos um paramentro"} 
    
    filtro = pd.Series([False] * len(df))

    if registro is not None:
        filtro |= df["Registro_ANS"].astype(str).str.contains(str(registro), na=False, case=False)
    if cnpj is not None:
        filtro |= df["CNPJ"].astype(str).str.contains(cnpj, na=False, case=False)
    if razao_social is not None:
        filtro |= df["Razao_Social"].astype(str).str.contains(razao_social, na=False, case=False)

    resultados = df[filtro]

    if resultados.empty:
        return {"error": "Nenhum resultado encontrado."}
    
    resultados = resultados.replace([np.inf, -np.inf], np.nan).fillna("N/A")

    return { "resultados": resultados.to_dict(orient="records")}