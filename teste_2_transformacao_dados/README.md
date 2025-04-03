# Teste 2 – Transformação de Dados

Este script realiza as seguintes tarefas:

1. Lê o PDF do Anexo I baixado no Teste 1.
2. Extrai todas as tabelas a partir da página 3.
3. Remove cabeçalhos duplicados e quebras de linha.
4. Salva os dados estruturados em um arquivo `tabela_formatada.csv`.
5. Compacta o `.csv` original em `Teste_IuryMarques.zip`.
6. Reabre o CSV e aplica a legenda de siglas nas colunas OD e AMB (valores e cabeçalho).

> Linguagem utilizada: Python  
> Bibliotecas principais: `pdfplumber`, `fitz` (PyMuPDF), `pandas`, `zipfile`
