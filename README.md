
# Processo Seletivo - IntuitiveCare

Este repositório contém a resolução dos três testes propostos para o processo seletivo da IntuitiveCare.

## Estrutura do Projeto

```
processo-seletivo-intuitivecare/
├── teste_1_web_scraping/
│   ├── main.py
│   ├── README.md
│   └── anexos/
│       └── anexo_i.pdf
├── teste_2_transformacao_dados/
│   ├── main.py
│   ├── tabela_formatada.csv
│   ├── Teste_IuryMarques.zip
│   └── README.md
├── teste_3_banco_de_dados/
│   ├── 01_create_tables.sql
│   ├── 02_import_data.sql
│   ├── 03_consultas_analiticas.sql
│   ├── README.md
│   └── Arquivos/
│       ├── Relatorio_cadop.csv
│       ├── [8 arquivos trimestrais de demonstrativos].csv
├── .gitignore
├── requirements.txt
└── README.md  ← este arquivo
```

## Testes

### ✅ Teste 1 - Web Scraping
- Realiza o download do PDF de uma tabela da ANS com `requests` e `BeautifulSoup`.
- Salva o arquivo em uma pasta específica para uso posterior.

### ✅ Teste 2 - Transformação de Dados
- Extrai tabelas de todas as páginas do PDF baixado no teste 1 usando `pdfplumber`.
- Concatena e estrutura os dados em formato tabular (.csv).
- Realiza a substituição das siglas das colunas OD e AMB com base na legenda presente no próprio PDF.
- Remove quebras de linha e espaços duplicados.
- Compacta o CSV original antes da substituição em um arquivo `.zip` com o nome `Teste_IuryMarques.zip`.

### ✅ Teste 3 - Banco de Dados (MySQL 8)
- Estrutura e importa os dados dos arquivos de demonstrativos contábeis e operadoras da ANS.
- Cria uma tabela auxiliar `demonstrativos_nao_importados` para armazenar registros com problemas de chave estrangeira.
- Realiza tratamento e limpeza dos dados no momento da importação.
- Implementa queries analíticas para:
  - Listar as 10 operadoras com maiores despesas no último trimestre.
  - Listar as 10 operadoras com maiores despesas no último ano.

## Requisitos

Instale as dependências com:

```bash
pip install -r requirements.txt
```

> As importações no teste 3 são feitas com `LOAD DATA LOCAL INFILE`, portanto certifique-se que a variável global `local_infile` está habilitada no seu servidor MySQL.

## Desenvolvido por

**Iury Marques**  
[https://github.com/Iurypgm](https://github.com/Iurypgm)
