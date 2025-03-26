# Importação das bibliotecas necessárias
from selenium import webdriver  # Automação de navegação na web
from selenium.webdriver.chrome.service import Service  # Gerenciamento do ChromeDriver
from selenium.webdriver.common.by import By  # Localizador de elementos no DOM
from selenium.webdriver.support.ui import Select  # Manipulação de elementos <select>
from bs4 import BeautifulSoup  # Parsing de HTML
import json  # Manipulação de dados em formato JSON
import time  # Manipulação de tempo (espera)

# Definição do caminho do ChromeDriver (substitua pelo local correto na sua máquina)
driver_path = "C:/chromedriver/chromedriver.exe"

# Configurações do navegador
options = webdriver.ChromeOptions()
# Se quiser rodar sem abrir o navegador, descomente a linha abaixo:
# options.add_argument("--headless")

# Inicializando o serviço do ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# URL do site a ser acessado
URL = "https://www.vaticannews.va/pt/feriados-liturgicos.html"
driver.get(URL)

# Tempo de espera para garantir o carregamento da página
time.sleep(10)

# Encontrar o elemento <select> que contém os meses
select_element = driver.find_element(By.ID, "month") 

# Criar um objeto Select para interagir com o dropdown de meses
select = Select(select_element)

# Lista para armazenar as solenidades coletadas
festas = []

# Percorrer todas as opções (meses) dentro do <select>
for option in select.options:
    mes = option.text.strip()  # Extrai o nome do mês
    option.click()  # Seleciona o mês no site
    time.sleep(10)  # Aguarda o carregamento dos novos dados

    # Captura o HTML atualizado da página
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Localiza as seções contendo as solenidades do mês
    celebracoes = soup.find_all("section", class_="section section--evidence section--isStatic flItem")

    # Itera sobre as solenidades encontradas
    for celebracao in celebracoes:
        nome_solenidade = celebracao.find("h2").text.strip() if celebracao.find("h2") else "Sem nome"
        data_solenidade = celebracao.find("span", class_="flDate").text.strip() if celebracao.find("span", class_="flDate") else "Sem data"
        descricao = " ".join([p.text.strip() for p in celebracao.find_all("p")]) if celebracao.find_all("p") else "Sem descrição"

        # Adiciona os dados à lista de festas
        festas.append({
            "Mês": mes,
            "Data": data_solenidade,
            "Solenidade": nome_solenidade,
            "Descrição": descricao
        })

# Fecha o navegador após a coleta dos dados
driver.quit()

# Salva os dados em um arquivo JSON
with open("solenidades_liturgicas.json", "w", encoding="utf-8") as f:
    json.dump(festas, f, ensure_ascii=False, indent=4)

# Confirmação de que o processo foi concluído
print("Dados coletados e salvos com sucesso!")