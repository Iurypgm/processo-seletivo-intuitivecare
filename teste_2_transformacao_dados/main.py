import pdfplumber
import fitz
import pandas as pd
import re
from zipfile import ZipFile
from pathlib import Path

# Caminhos dos arquivos
BASE_DIR = Path(__file__).resolve().parent
PDF_PATH = BASE_DIR.parent / "anexos" / "anexo_i.pdf"
CSV_PATH = BASE_DIR / "tabela_formatada.csv"
ZIP_PATH = BASE_DIR / "Teste_IuryMarques.zip"

def extrair_legenda(pdf_path):
    """Extrai a legenda das siglas (OD, AMB) da última página do PDF."""
    legenda = {}
    with fitz.open(pdf_path) as doc:
        texto = doc[-1].get_text()
        for linha in texto.split("\n"):
            match = re.match(r"(\w{2,4})\s*[:：]\s*(.+)", linha)
            if match:
                sigla, descricao = match.groups()
                legenda[sigla.strip()] = descricao.strip()
    return legenda

def extrair_tabelas_do_pdf(pdf_path):
    """Extrai todas as tabelas a partir da página 3 do PDF."""
    dados = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, pagina in enumerate(pdf.pages):
            if i < 2:
                continue
            tabelas = pagina.extract_tables()
            for tabela in tabelas:
                if tabela:
                    for linha in tabela:
                        if any(campo is not None and campo.strip() for campo in linha):
                            linha_limpa = [campo.replace("\n", " ").replace("\r", " ").strip() if campo else "" for campo in linha]
                            dados.append(linha_limpa)
    return dados

def gerar_csv_e_zip(dados, csv_path, zip_path):
    """Gera o CSV original e compacta em um .zip."""
    colunas = [c.replace("\n", " ").replace("\r", " ").strip() for c in dados[0]]
    registros = dados[1:]
    df = pd.DataFrame(registros, columns=colunas)
    df = df[df["PROCEDIMENTO"].str.upper() != "PROCEDIMENTO"]
    df.to_csv(csv_path, sep=";", index=False, encoding="utf-8-sig")

    with ZipFile(zip_path, "w") as zipf:
        zipf.write(csv_path, arcname=csv_path.name)

def aplicar_legenda(csv_path, legenda):
    """
    Reabre o CSV e aplica as descrições da legenda para as colunas OD e AMB (Cabeçalho e valores)

    Essa decisão cobre a interpretação mais completa da instrução:
    "Substitua as abreviações das colunas OD e AMB pelas descrições completas"
    """
    df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")

    for col in ["OD", "AMB"]:
        if col in df.columns:
            df[col] = df[col].map(lambda x: legenda.get(x.strip(), x) if isinstance(x, str) else x)

    df.rename(columns={col: legenda.get(col, col) for col in ["OD", "AMB"]}, inplace=True)

    df.to_csv(csv_path, sep=";", index=False, encoding="utf-8-sig")

def main():
    legenda = extrair_legenda(PDF_PATH)
    dados = extrair_tabelas_do_pdf(PDF_PATH)
    gerar_csv_e_zip(dados, CSV_PATH, ZIP_PATH)
    aplicar_legenda(CSV_PATH, legenda)

if __name__ == "__main__":
    main()