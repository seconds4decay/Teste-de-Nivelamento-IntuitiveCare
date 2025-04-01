-- TOP 10 operadoras com maiores despesas no último trimestre
SELECT 
    dc.REG_ANS, 
    op.Nome_Fantasia,
    SUM(dc.VL_SALDO_FINAL - dc.VL_SALDO_INICIAL) AS total_despesas
FROM demonstracoes_contabeis dc
JOIN operadoras op ON dc.REG_ANS = op.Registro_ANS
WHERE dc.DESCRICAO LIKE '%EVENTOS%SINISTROS CONHECIDOS%ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR%'
AND YEAR(dc.DATA) = YEAR(CURDATE())
AND QUARTER(dc.DATA) = QUARTER(CURDATE()) - 1
GROUP BY dc.REG_ANS, op.Nome_Fantasia
ORDER BY total_despesas DESC
LIMIT 10;

-- TOP 10 operadoras com maiores despesas no último ano
SELECT 
    dc.REG_ANS, 
    op.Nome_Fantasia,
    SUM(dc.VL_SALDO_FINAL - dc.VL_SALDO_INICIAL) AS total_despesas_ano
FROM demonstracoes_contabeis dc
JOIN operadoras op ON dc.REG_ANS = op.Registro_ANS
WHERE dc.DESCRICAO LIKE '%EVENTOS%SINISTROS CONHECIDOS%ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR%'
AND YEAR(dc.DATA) = YEAR(CURDATE()) - 1
GROUP BY dc.REG_ANS, op.Nome_Fantasia
ORDER BY total_despesas_ano DESC
LIMIT 10;