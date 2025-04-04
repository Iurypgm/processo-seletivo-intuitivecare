# Teste 1 – Web Scraping

Este script automatiza a extração de arquivos PDF da ANS relacionados à atualização do Rol de Procedimentos.

## 📌 Funcionalidades

- Acessa a página oficial da ANS sobre Atualização do Rol de Procedimentos.
- Localiza e faz o download dos arquivos PDF do Anexo I e Anexo II.
- Salva os arquivos na pasta `anexos/`.
- Compacta os dois arquivos em `anexos_comprimidos.zip`.

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- **Python**
- `requests`
- `beautifulsoup4`
- `zipfile`
- `os`

## 📁 Estrutura

```
teste_1_web_scraping/
├── main.py
├── anexos/
│   ├── anexo_i.pdf
│   └── anexo_ii.pdf
└── anexos_comprimidos.zip
```

## ▶️ Execução

Para executar o script:

```bash
python main.py
```

Certifique-se de ter as dependências instaladas:

```bash
pip install -r ../../requirements.txt
```

> Este script prepara os arquivos que serão utilizados no Teste 2.
