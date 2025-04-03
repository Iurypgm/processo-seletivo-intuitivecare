import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# URL base do site da ANS com os anexos
BASE_URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Caminhos base para salvar os arquivos
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PDF_DIR = os.path.join(BASE_DIR, "anexos")
ZIP_FILENAME = os.path.join(BASE_DIR, "anexos_comprimidos.zip")

# Cria o diretório de anexos se ainda não existir
os.makedirs(PDF_DIR, exist_ok=True)

# Realiza requisição e parse do HTML da página
response = requests.get(BASE_URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Filtra os links para os anexos I e II (em PDF)
pdf_links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    texto = link.text.lower().replace(".", "")
    if ("anexo i" in texto or "anexo ii" in texto) and href.endswith(".pdf"):
        if not href.startswith("http"):
            href = "https://www.gov.br" + href
        pdf_links.append((texto.strip(), href))

# Faz o download de cada PDF e salva em 'anexos/'
pdf_paths = []
for name, link in pdf_links:
    filename = name.replace(" ", "_") + ".pdf"
    filepath = os.path.join(PDF_DIR, filename)
    response = requests.get(link)
    with open(filepath, "wb") as f:
        f.write(response.content)
    pdf_paths.append(filepath)

# Compacta todos os PDFs baixados em um único arquivo ZIP
with ZipFile(ZIP_FILENAME, "w") as zipf:
    for file_path in pdf_paths:
        zipf.write(file_path, os.path.basename(file_path))
