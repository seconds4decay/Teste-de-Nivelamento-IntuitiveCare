import requests
import os
import zipfile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

download_dir = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome()
driver.get("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")

# Verificar se o zip já existe e removê-lo
if os.path.exists(f"{download_dir}/anexos.zip"):
    os.remove(f"{download_dir}/anexos.zip")
    print("Arquivo zip existente removido.")

# Obter os links de download dos arquivos e seus nomes
files_link = driver.find_elements(By.XPATH, "//a[(text()='Anexo I.' or text()='Anexo II.')]")
files_urls = [link.get_attribute("href") for link in files_link]
file_names = [link.split("/")[-1] for link in files_urls]

# Baixar os arquivos
for i, files in enumerate(files_urls):
    print(f"Baixando {file_names[i]}...")
    
    response = requests.get(files)

    if response.status_code == 200:
        with open(f"{download_dir}/{file_names[i]}", "wb") as file:
            file.write(response.content)
        print(f"{file_names[i]} baixado com sucesso!")
    else:
        print(f"Erro ao baixar {file_names[i]}")

driver.close()

# Zipar os arquivos e remover os arquivos originais
with zipfile.ZipFile(f"{download_dir}/anexos.zip", "w") as zipf:
    for file in file_names:
        zipf.write(f"{download_dir}/{file}", arcname=file)
        os.remove(f"{download_dir}/{file}")
        print(f"{file} zipado com sucesso!")