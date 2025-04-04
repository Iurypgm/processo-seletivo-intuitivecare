# Processo Seletivo - IntuitiveCare

Este repositório contém a resolução completa dos quatro testes propostos para o processo seletivo da IntuitiveCare.

---

## 📁 Estrutura do Projeto

```
processo-seletivo-intuitivecare/
├── teste_1_web_scraping/
│   ├── main.py
│   └── README.md
├── teste_2_transformacao_dados/
│   ├── main.py
│   ├── tabela_formatada.csv
│   ├── Teste_IuryMarques.zip
│   └── README.md
├── teste_3_banco_de_dados/
│   ├── 01_create_tables.sql
│   ├── 02_import_data_FINAL_LIMPO.sql
│   ├── 03_consultas_analiticas.sql
│   └── README.md
├── teste_4_API/
│   ├── backend/
│   │   └── main.py
│   ├── frontend/
│   │   ├── index.html
│   │   ├── vite.config.js
│   │   └── src/
│   │       ├── App.vue
│   │       ├── main.js
│   │       └── style.css
│   ├── postman/
│   │   └── Teste 4 - Busca Operadoras.postman_collection.json
│   └── README.md
├── .gitignore
├── requirements.txt
└── README.md  ← este arquivo
```

---

## ✅ Testes Realizados

### ✔️ Teste 1 – Web Scraping

- Acessa a página da ANS para buscar os anexos em PDF (Anexo I e II).
- Baixa e salva os arquivos na pasta `anexos/`.
- Compacta ambos em `anexos_comprimidos.zip`.

> Bibliotecas: `requests`, `BeautifulSoup`, `zipfile`, `os`

---

### ✔️ Teste 2 – Transformação de Dados

- Extrai todas as tabelas do PDF do Anexo I (a partir da página 3).
- Remove cabeçalhos duplicados e quebras de linha.
- Salva os dados estruturados em `tabela_formatada.csv`.
- Compacta o `.csv` original (pré-tratamento) em `Teste_IuryMarques.zip`.
- Reabre o CSV e aplica a legenda da ANS nas colunas OD e AMB (valores e cabeçalhos).

> Bibliotecas: `pdfplumber`, `PyMuPDF`, `pandas`, `zipfile`

---

### ✔️ Teste 3 – Banco de Dados (MySQL 8)

- Estrutura banco `intuitivecare_db` com três tabelas principais:
  - `operadoras`, `demonstrativos`, `demonstrativos_nao_importados`
- Importa e normaliza os dados da ANS (8 trimestres + cadastro das operadoras).
- Aplica tratamento e validação no processo de importação.
- Queries analíticas para:
  - **TOP 10 operadoras com maiores despesas na categoria** `"EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"` no último **trimestre** disponível
  - **TOP 10 operadoras com maiores despesas** nessa mesma categoria considerando os **últimos 4 trimestres**

> Observações:

- A importação usa `LOAD DATA LOCAL INFILE`, com validação e limpeza.
- Registros inconsistentes são armazenados separadamente para controle.

---

### ✔️ Teste 4 – API (Vue.js + FastAPI)

- API com `FastAPI` para realizar buscas textuais no cadastro de operadoras.
- Acesso via endpoint: `http://localhost:8000/operadoras`
- Busca ocorre em todos os campos do CSV `Relatorio_cadop.csv` (Testes 3).
- Frontend com `Vue 3` (via Vite) exibe resultados de forma dinâmica.
- Collection do Postman incluída para facilitar testes de API.

> Bibliotecas e tecnologias: `FastAPI`, `uvicorn`, `pandas`, `Vue.js`, `Vite`, `Postman`

---

## ⚙️ Requisitos

Instale todas as dependências com:

```bash
pip install -r requirements.txt
```

> Para o Teste 3, certifique-se de habilitar a variável global `local_infile` no seu MySQL e ajustar o caminho dos arquivos `.csv` no script.

---

## 👤 Desenvolvido por

**Iury Marques**  
[https://github.com/Iurypgm](https://github.com/Iurypgm)
