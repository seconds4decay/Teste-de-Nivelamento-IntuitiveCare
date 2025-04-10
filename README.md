# Teste de Nivelamento - IntuitiveCare

Este repositório contém os desafios do teste de nivelamento da IntuitiveCare.

A seguir, estão as instruções detalhadas para configurar o ambiente, instalar as dependências necessárias e executar cada um dos testes.

---

## Pré-requisitos

Antes de iniciar, certifique-se de que os seguintes softwares estão instalados em seu sistema:

- [Python 3.9+](https://www.python.org/downloads/)
- [Node.js 16.1.0+](https://nodejs.org/)
- [Git](https://git-scm.com/)
- [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatível com a versão do seu Chrome
- (Opcional) [Docker Compose](https://docs.docker.com/desktop/setup/install/)

---

## Clonando o Repositório

Para obter uma cópia local do projeto, execute:

```bash
git clone https://github.com/seconds4decay/Teste-de-Nivelamento-IntuitiveCare.git
cd Teste-de-Nivelamento-IntuitiveCare
```

---

## 1. Teste de Webscraping

### Instalação das Dependências

Navegue até o diretório do desafio e instale as dependências:

```bash
cd Webscraping
pip install -r requirements.txt
```

### Executando o Script

Para executar o script de webscraping:

```bash
python main.py
```

---

## 2. Teste de Transformação de Dados

### Instalação das Dependências

Navegue até o diretório correspondente e instale as dependências:

```bash
pip install -r requirements.txt
```

### Executando o Script

Para executar o script de transformação de dados:

```bash
python main.py
```

---

## 3. Teste de Banco de Dados

Este desafio envolve a configuração e manipulação de um banco de dados.

### Requisitos

- [MySQL](https://www.mysql.com/downloads/)

### Configuração do Banco de Dados

1. Inicie uma conexão com o servidor do MySQL.
2. Crie uma database nova
3. Importe os scripts em `Banco de Dados/` e rode na ordem:
    1. `criar_tabelas.sql`
    2. `inserir_dados_demonstracoes.sql`
    3. `inserir_dados_operadoras.sql`

### Executando Consultas

Em seguida você pode executar `analises.sql` para realizar as seguintes consultas:

- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

---

## 4. Teste API

### Coleção do Postman para Demonstrar a API

A coleção está disponivel em: [Teste de API IntuitiveCare]([https://teste-de-api-8297.postman.co/workspace/Team-Workspace~711bfd1e-3df6-4cb2-811d-8d05a4bf31ab/collection/40423840-9713d935-3035-4cde-a19c-e8939e645efe?action=share&creator=40423840](https://documenter.getpostman.com/view/40423840/2sB2cX9MYU))

---
### Opção 1: Iniciar com Docker 

#### 1. Navegue até a pasta raiz da API

Navegue até o diretório principal da API 

```bash
cd ../API
```

#### 2. Construir e iniciar os contêineres:

Execute o comando abaixo para iniciar os contáiners:

```bash
docker-compose up --build
```

#### 3. Encerrar a aplicação

Para parar e remover os contêineres, pressione Ctrl+C no terminal onde os contêineres estão rodando ou execute:

```bash
docker-compose down
```
---
### Opção 2: Iniciar Localmente

#### Backend

##### Instalação das Dependências

Navegue até o diretório da API e instale as dependências:

```bash
cd ../API/backend
pip install -r requirements.txt
```


##### Executando o Servidor

Para iniciar o servidor FastAPI:

```bash
uvicorn main:app --reload
```

O servidor estará disponível em `http://127.0.0.1:8000`.

#### Frontend

##### Instalação das Dependências

Navegue até o diretório do frontend e instale as dependências:

```bash
cd ../frontend
npm install --force
```

##### Executando o Frontend

Para iniciar o servidor de desenvolvimento:

```bash
npm run serve
```

O frontend estará disponível em `http://localhost:3000`.

---

## Contato

Para dúvidas ou sugestões, entre em contato pelo e-mail: [lfta@cesar.school](mailto:lfta@cesar.school).


