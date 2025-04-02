# Teste 1 - Web Scraping (IntuitiveCare)

Este script realiza web scraping no site da ANS para:

1. Acessar a página de atualização do rol de procedimentos
2. Baixar os Anexos I e II em PDF
3. Compactar os arquivos em um único `.zip`

## Como rodar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o script:

```bash
python main.py
```

Os PDFs serão salvos na pasta `anexos/` e compactados no arquivo `anexos_comprimidos.zip`.
