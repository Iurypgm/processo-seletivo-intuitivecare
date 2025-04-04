# Teste 3 — Banco de Dados (MySQL 8)

## 🎯 Objetivo

Realizar o tratamento e análise de dados públicos da ANS para avaliar habilidades com:

- Manipulação de arquivos
- Estruturação de banco de dados relacional (MySQL)
- Importação e normalização de dados
- Criação de queries analíticas

---

## 📁 Estrutura

```
teste_3_banco_de_dados/
│
├── 01_create_tables.sql            # Criação do banco, tabelas principais e auxiliares
├── 02_import_data.sql  # Script completo de importação (com limpeza e validação)
├── 03_consultas_analiticas.sql     # Queries finais para análise
├── README.md                       # Este arquivo
└── Arquivos/                       # Pasta (excluída do zip) com todos os CSVs da ANS
```

---

## 🧱 Banco de Dados

### Banco: `intuitivecare_db`

### Tabelas principais:

- `operadoras`: dados cadastrais das operadoras
- `demonstrativos`: dados financeiros das operadoras, filtrados por registros válidos
- `demonstrativos_nao_importados`: registros com `REG_ANS` sem correspondência

---

## ⚙️ Importação dos dados

Utilize o script `02_import_data.sql` para importar os dados automaticamente.

> 🔔 Altere o caminho da variável `INFILE` no script para refletir a pasta onde estão seus arquivos `.csv`.

Durante o processo:

- É feita a limpeza da descrição (`DESCRICAO`) para remover espaços duplicados e quebras.
- Registros inválidos vão para uma tabela separada (`demonstrativos_nao_importados`).
- A tabela temporária `demonstrativos_stage` é descartada após uso.

### 💻 Execução (exemplo)

```bash
mysql -u seu_usuario -p < 01_create_tables.sql
mysql -u seu_usuario -p < 02_import_data.sql
mysql -u seu_usuario -p < 03_consultas_analiticas.sql
```

---

## 📊 Queries Analíticas

Arquivo: `03_consultas_analiticas.sql`

Contém:

1. **TOP 10 operadoras com maiores despesas na categoria**  
   `"EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"`  
   no último **trimestre** disponível

2. **TOP 10 operadoras com maiores despesas** nessa mesma categoria considerando os **últimos 4 trimestres**

Ambas as queries:

- Calculam a despesa líquida com `SUM(VL_SALDO_INICIAL) - SUM(VL_SALDO_FINAL)`
- Excluem operadoras com `Total_Despesas = 0` (para garantir relevância)

---

## 👨‍💻 Desenvolvido por

**Iury Marques**  
[https://github.com/Iurypgm](https://github.com/Iurypgm)
