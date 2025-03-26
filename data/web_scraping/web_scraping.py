#Bibliotecas utilizadas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import json
import time

# Caminho para o seu WebDriver (Lembrando que este caminho deve ser diacordo onde o chromedriver foi instalado na máquina)
driver_path = "C:/chromedriver/chromedriver.exe"

# Inicializando o navegador
options = webdriver.ChromeOptions()
# Caso queira que o navedaor não abra utilize esta linha --> options.add_argument("--headless")

# Criando o serviço do ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# URL do site
URL = "https://www.vaticannews.va/pt/feriados-liturgicos.html"
driver.get(URL)

# Esperar um tempo para o site carregar
time.sleep(10)

# Encontrar o select de meses
select_element = driver.find_element(By.ID, "month") 

# Criar objeto Select
select = Select(select_element)

# Lista para armazenar os dados das festas
festas = []

# Percorrer todos os meses disponíveis no select
for option in select.options:
    mes = option.text.strip()
    option.click()  # Selecionar o mês
    time.sleep(10)  # Esperar o site carregar os novos dados

    # Capturar HTML atualizado
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Encontrar as solenidades do mês
    celebracoes = soup.find_all("section", class_="section section--evidence section--isStatic flItem")

    for celebracao in celebracoes:
        nome_solenidade = celebracao.find("h2").text.strip() if celebracao.find("h2") else "Sem nome"
        data_solenidade = celebracao.find("span", class_="flDate").text.strip() if celebracao.find("span", class_="flDate") else "Sem data"
        descricao = " ".join([p.text.strip() for p in celebracao.find_all("p")]) if celebracao.find_all("p") else "Sem descrição"

        festas.append({
            "Mês": mes,
            "Data": data_solenidade,
            "Solenidade": nome_solenidade,
            "Descrição": descricao
        })

# Fechar o navegador
driver.quit()

# Salvando os dados em um arquivo JSON
with open("solenidades_liturgicas.json", "w", encoding="utf-8") as f:
    json.dump(festas, f, ensure_ascii=False, indent=4)

print("Dados coletados e salvos com sucesso!")
