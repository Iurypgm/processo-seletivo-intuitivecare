-- Query 1: TOP 10 operadoras com maiores despesas "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre
SELECT
    o.Registro_ANS,
    o.CNPJ,
    o.Razao_Social,
    d.DATA,
    SUM(CASE 
            WHEN d.VL_SALDO_INICIAL - d.VL_SALDO_FINAL > 0 
            THEN d.VL_SALDO_INICIAL - d.VL_SALDO_FINAL 
            ELSE 0 
        END
    ) AS Total_Despesas
FROM demonstrativos d
JOIN operadoras o ON o.Registro_ANS = d.REG_ANS
WHERE d.DESCRICAO LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
  AND d.DATA = (SELECT MAX(DATA) FROM demonstrativos)
GROUP BY o.Registro_ANS, o.CNPJ, o.Razao_Social, d.DATA
HAVING Total_Despesas > 0
ORDER BY Total_Despesas DESC
LIMIT 10;


-- Query 2: TOP 10 operadoras com maiores despesas na categoria específica no último ano
SELECT
    o.Registro_ANS,
    o.CNPJ,
    o.Razao_Social,
    SUM(CASE 
            WHEN d.VL_SALDO_INICIAL - d.VL_SALDO_FINAL > 0 
            THEN d.VL_SALDO_INICIAL - d.VL_SALDO_FINAL 
            ELSE 0 
        END
    ) AS Total_Despesas
FROM demonstrativos d
JOIN operadoras o ON o.Registro_ANS = d.REG_ANS
WHERE d.DESCRICAO LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
  AND d.DATA >= (
      SELECT MIN(DATA) FROM (
          SELECT DISTINCT DATA FROM demonstrativos
          ORDER BY DATA DESC
          LIMIT 4
      ) ultimos_quatro
  )
GROUP BY o.Registro_ANS, o.CNPJ, o.Razao_Social
HAVING Total_Despesas > 0
ORDER BY Total_Despesas DESC
LIMIT 10;
