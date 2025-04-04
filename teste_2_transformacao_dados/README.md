# Teste 2 – Transformação de Dados

Este script realiza a extração e transformação dos dados do Anexo I em formato tabular estruturado.

## 📌 Funcionalidades

1. Lê o PDF do Anexo I baixado no Teste 1.
2. Extrai todas as tabelas a partir da página 3.
3. Remove cabeçalhos duplicados e quebras de linha.
4. Salva os dados estruturados em um arquivo `tabela_formatada.csv`.
5. Compacta o `.csv` original em `Teste_IuryMarques.zip`.
6. Reabre o CSV e aplica a legenda de siglas nas colunas OD e AMB (valores e cabeçalho).

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- **Python**
- `pdfplumber`
- `fitz` (PyMuPDF)
- `pandas`
- `zipfile`

## 📁 Estrutura

```
teste_2_transformacao_dados/
├── main.py
├── tabela_formatada.csv
├── Teste_IuryMarques.zip
└── README.md
```

## ▶️ Execução

Para rodar o script:

```bash
python main.py
```

> Certifique-se de que o PDF `anexo_i.pdf` esteja localizado na pasta `teste_1_web_scraping/anexos/`, pois o caminho de leitura é relativo ao projeto.
