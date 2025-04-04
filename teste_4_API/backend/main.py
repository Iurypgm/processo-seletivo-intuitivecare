
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pathlib import Path

app = FastAPI()

# Permitir chamadas do frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Caminho para o CSV (usando mesmo local do teste 3)
CSV_PATH = Path(__file__).resolve().parents[2] / "teste_3_banco_de_dados" / "Arquivos" / "Relatorio_cadop.csv"

# Carrega os dados uma única vez
operadoras_df = pd.read_csv(CSV_PATH, sep=';', dtype=str).fillna("")

@app.get("/operadoras")
def buscar_operadoras(q: str = Query(..., min_length=1)):
    """
    Busca textual na base de operadoras.
    A busca é feita em todos os campos da tabela, convertendo cada linha em string.
    """
    termo = q.lower()
    resultados = operadoras_df[operadoras_df.apply(lambda row: termo in row.to_string().lower(), axis=1)]
    return resultados.to_dict(orient="records")
