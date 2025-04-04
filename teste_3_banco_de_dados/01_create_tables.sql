-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS intuitivecare_db;
USE intuitivecare_db;

-- Criação da tabela de operadoras com todas as colunas reais
CREATE TABLE operadoras (
    Registro_ANS INT PRIMARY KEY,
    CNPJ VARCHAR(18),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(100),
    Logradouro VARCHAR(255),
    Numero VARCHAR(20),
    Complemento VARCHAR(100),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP VARCHAR(20),
    DDD VARCHAR(5),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(100),
    Regiao_de_Comercializacao VARCHAR(255),
    Data_Registro_ANS DATE
);

-- Criação da tabela de demonstrativos conforme estrutura correta
CREATE TABLE demonstrativos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    DATA DATE,
    REG_ANS INT,
    CD_CONTA_CONTABIL VARCHAR(50),
    DESCRICAO TEXT,
    VL_SALDO_INICIAL DECIMAL(18,2),
    VL_SALDO_FINAL DECIMAL(18,2),
    FOREIGN KEY (REG_ANS) REFERENCES operadoras(Registro_ANS)
);
