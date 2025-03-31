import requests
import os
import pdfplumber
import zipfile
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

download_dir = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome()
driver.get("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")

# Verificar se o zip já existe e removê-lo
if os.path.exists(f"{download_dir}/Teste_Lucas.zip"):
    os.remove(f"{download_dir}/Teste_Lucas.zip")
    print("Arquivo zip existente removido.")


# Obter o link de download do arquivo e seu nome
file_link = driver.find_element(By.XPATH, "//a[(text()='Anexo I.')]")
file_url = file_link.get_attribute("href")
file_name = file_url.split("/")[-1]

# Baixar o arquivo
print(f"Baixando {file_name}...")
    
response = requests.get(file_url)

if response.status_code == 200:
    with open(f"{download_dir}/{file_name}", "wb") as file:
        file.write(response.content)
    print(f"{file_name} baixado com sucesso!")
else:
    print(f"Erro ao baixar {file_name}")

driver.close()

# Extrair tabelas do pdf, apagar o pdf e coverter em .csv
tabelas_extraidas = []

with pdfplumber.open(f"{download_dir}/{file_name}") as pdf:
    for page in pdf.pages:
        tabela = page.extract_table()
        if tabela:
            tabelas_extraidas.extend(tabela)

os.remove(f"{download_dir}/{file_name}")

df = pd.DataFrame(tabelas_extraidas[1:], columns=tabelas_extraidas[0])
df.to_csv(f"{download_dir}/tabelas_extraidas.csv", index=False)

# Zipar os arquivos e remover os arquivos originais

with zipfile.ZipFile(f"{download_dir}/Teste_Lucas.zip", "w") as zipf:
    zipf.write(f"{download_dir}/tabelas_extraidas.csv", arcname="tabelas_extraidas.csv")
    os.remove(f"{download_dir}/tabelas_extraidas.csv")
    print(f"Teste_Lucas.zip criado com sucesso!")