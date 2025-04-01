drop database bd_teste

create database bd_teste

drop table demonstracoes_contabeis

create table demonstracoes_contabeis (
	DATA date,
	REG_ANS varchar(6), 
	CD_CONTA_CONTABIL varchar(9),
	DESCRICAO varchar(152),
	VL_SALDO_INICIAL DECIMAL(15,2),
	VL_SALDO_FINAL DECIMAL(15,2)
);

drop table operadoras

create table operadoras (
	Registro_ANS varchar(8),
	CNPJ varchar(20),
	Razao_Social varchar(150),
	Nome_Fantasia varchar(70),
	Modalidade varchar(40),
	Logradouro varchar(50),
	Numero varchar(30),
	Complemento varchar(50),
	Bairro varchar(40),
	Cidade varchar(50),
	UF varchar(4),
	CEP varchar(20),
	DDD varchar(10),
	Telefone varchar(20),
	Fax varchar(20),
	Endereco_eletronico varchar(50),
	Representante varchar(60),
	Cargo_Representante varchar(50),
	Regiao_de_Comercializacao int,
	Data_Registro_ANS varchar(20)
);