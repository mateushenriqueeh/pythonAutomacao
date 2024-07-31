import pandas as pd

import time

from selenium import webdriver  # Importando navegador
from selenium.webdriver.common.by import By  # Encontrar os elementos
from selenium.webdriver.common.keys import Keys  # Para digitar no teclado na web
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

nome_do_arquivo = "dados.xlsx"
url_do_site = "https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAO__SXtR9RUNEpVUlNBSU1CTVdaTkhDN1A1S1BaSEsxNS4u"
df = pd.read_excel(nome_do_arquivo)

service = Service("chromedriver.exe")
options = Options()
options.add_argument("--disable-gpu")



for index, row in df.iterrows():
    print("Index: " + str(index) + " nome " + row["NOME"])

    # Iniciar o navegador
    chrome = webdriver.Chrome(service=service, options=options)
    chrome.get(url_do_site)

    time.sleep(2)

    elemento_texto_nome=chrome.find_element(By.XPATH,'//*[@id="question-list"]/div[1]/div[2]/div/span/input')

    elemento_texto_telefone=chrome.find_element(By.XPATH,'//*[@id="question-list"]/div[2]/div[2]/div/span/input')

    elemento_texto_nome.send_keys(row["NOME"])
    time.sleep(1)
    elemento_texto_telefone.send_keys(row["TELEFONE"])
    time.sleep(1)

    # Fechar o navegador
    chrome.quit()


