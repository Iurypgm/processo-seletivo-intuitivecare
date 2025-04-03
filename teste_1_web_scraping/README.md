# Teste 1 – Web Scraping

Este script realiza as seguintes operações:

1. Acessa a página oficial da ANS sobre Atualização do Rol de Procedimentos.
2. Encontra e baixa os arquivos PDF do Anexo I e II.
3. Salva os arquivos na pasta `anexos`.
4. Compacta os dois arquivos em `anexos_comprimidos.zip`.

> Linguagem utilizada: Python  
> Bibliotecas principais: `requests`, `BeautifulSoup`, `zipfile`, `os`
