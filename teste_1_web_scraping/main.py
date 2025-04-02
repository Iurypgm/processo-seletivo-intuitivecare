import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

BASE_URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
PDF_DIR = "anexos"
ZIP_FILENAME = "anexos_comprimidos.zip"

def criar_diretorio(destino):
    os.makedirs(destino, exist_ok=True)

def obter_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return None

def extrair_links_pdfs(html):
    soup = BeautifulSoup(html, 'html.parser')
    pdf_links = []

    for link in soup.find_all('a', href=True):
        href = link['href']
        texto = link.text.lower().replace(".", "").strip()

        if ("anexo i" in texto or "anexo ii" in texto) and href.endswith(".pdf"):
            if not href.startswith("http"):
                href = "https://www.gov.br" + href
            pdf_links.append((texto, href))

    return pdf_links

def baixar_pdfs(pdf_links, destino):
    caminhos = []

    for nome, url in pdf_links:
        filename = nome.replace(" ", "_") + ".pdf"
        filepath = os.path.join(destino, filename)

        if os.path.exists(filepath):
            print(f"Já existe: {filename}, pulando download.")
            caminhos.append(filepath)
            continue

        try:
            response = requests.get(url)
            response.raise_for_status()

            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"Baixado: {filename}")
            caminhos.append(filepath)

        except requests.RequestException as e:
            print(f"Erro ao baixar {filename}: {e}")

    return caminhos

def compactar_em_zip(caminhos, zip_nome):
    try:
        with ZipFile(zip_nome, "w") as zipf:
            for file_path in caminhos:
                zipf.write(file_path, os.path.basename(file_path))
        print(f"Arquivos compactados com sucesso em: {zip_nome}")
    except Exception as e:
        print(f"Erro ao compactar arquivos: {e}")

def main():
    print("Iniciando processo de scraping e compactação...")
    criar_diretorio(PDF_DIR)
    html = obter_html(BASE_URL)
    if not html:
        return
    pdf_links = extrair_links_pdfs(html)
    if not pdf_links:
        print("Nenhum PDF de Anexo I ou II encontrado.")
        return
    caminhos_pdfs = baixar_pdfs(pdf_links, PDF_DIR)
    if caminhos_pdfs:
        compactar_em_zip(caminhos_pdfs, ZIP_FILENAME)
    else:
        print("Nenhum arquivo foi baixado com sucesso.")

if __name__ == "__main__":
    main()
