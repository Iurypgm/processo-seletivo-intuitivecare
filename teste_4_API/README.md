# Teste 4 - API (IntuitiveCare)

Este teste consiste na criação de uma interface web utilizando Vue.js que consome uma API desenvolvida em Python (FastAPI), permitindo realizar buscas textuais sobre dados de operadoras de planos de saúde.

---

## ✅ O que foi feito

- Backend Python (FastAPI) que carrega o CSV de operadoras e oferece uma rota `/operadoras?q=` para buscas textuais.
- Frontend com Vue 3 (Vite) que possui um campo de busca, um botão de ação e renderiza os resultados.
- Conexão entre frontend e backend usando requisições HTTP.
- Integração direta com o arquivo `Relatorio_cadop.csv` do Teste 3.

---

## 🚀 Como executar o projeto

### 1. Requisitos

- Python 3.10+
- Node.js 18+

---

### 2. Rodar o backend (FastAPI)

```bash
cd teste_4_API/backend
pip install -r ../../requirements.txt
uvicorn main:app --reload
```

A API será disponibilizada em:

```
http://localhost:8000/operadoras
```

> Use o parâmetro `q` para realizar buscas textuais.  
> Exemplo: `?q=amil`, `?q=12345678000195`

---

### 3. Rodar o frontend (Vue.js com Vite)

```bash
cd teste_4_API/frontend
npm install
npm run dev
```

Acesse no navegador:

```
http://localhost:5173
```

---

## 📄 Estrutura do projeto

```
teste_4_API/
  ├── backend/
  │   └── main.py
  ├── frontend/
  │   ├── index.html
  │   ├── vite.config.js
  │   └── src/
  │       ├── App.vue
  │       ├── main.js
  │       └── style.css
  └── postman/
      └── Teste 4 - Busca Operadoras.postman_collection.json
```

---

## 🧪 Testes via Postman

Uma collection Postman está disponível em `teste_4_API/postman/Teste 4 - Busca Operadoras.postman_collection.json`.

Importe no Postman e teste com diferentes valores do parâmetro `q`, como:

- `amil`
- `odontoprev`
- `petro`
- `12345678000195`

---

## 👨‍💻 Desenvolvido por

**Iury Marques**  
[https://github.com/Iurypgm](https://github.com/Iurypgm)
