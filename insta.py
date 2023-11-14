import random
import threading
import select
import sys
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup



def main():

    print(" ")
    
main()
    
print("Carregando...")

# Configura as opções para modo headless
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Modifica o User-Agent para se parecer mais com um navegador real
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

# Inicializa o navegador Chrome em modo headless
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)

# Atraso antes de acessar o site
time.sleep(random.uniform(1, 3))

# Acessa a URL
navegador.get('https://saveinsta.app/pt')

# Atraso antes de realizar a próxima ação
time.sleep(random.uniform(2, 3))
print("   ")
print("   ")
link = input("Cole o link do vídeo aqui: ")
print("   ")
print("Aguarde...")

# Obtém o HTML da página
html = navegador.page_source

# Localiza o elemento com o ID s_input e insere texto
# Localiza o campo de texto de entrada
campo_texto = navegador.find_element(By.ID, "s_input")

# Insere o link do vídeo no campo de texto
campo_texto.send_keys(link)


botao_download = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-form"]/div/div/button')))
botao_download.click()



# Atraso antes de realizar a próxima ação
time.sleep(random.uniform(8, 15))

html = navegador.page_source


# Seu padrão atual
padrao = re.compile(r'(https://d\.rapidcdn\.app/snapi e[^\s"]*|https://download\.i[^\s"]*|https://ig76\.snap[^\s"]*)')

# Encontra todas as correspondências no HTML da página
urls_encontradas = padrao.findall(html)

if urls_encontradas:
    # Procura por índices das ocorrências que começam com "https://d.rapidcdn.app/snapi e"
    indices_d_rapidcdn = [i for i, url in enumerate(urls_encontradas) if 'https://d.rapidcdn.app/snapi e' in url]

    if indices_d_rapidcdn:
        # Encontra o segundo link após cada ocorrência de "https://download.i-4"
        for indice in indices_d_rapidcdn:
            if indice + 2 < len(urls_encontradas):
                # Encontra o segundo link com início "https://download.i-4"
                segundo_link = next((url for url in urls_encontradas[indice + 1:] if url.startswith('https://download.i-4')), None)
                if segundo_link:
                    print("Link para Download:", segundo_link)
                else:
                    print("   ")
                    print("   ")
                    print("TENTE NOVAMENTE")
            else:
                print("   ")
                print("   ")
                print("TENTE NOVAMENTE")
    else:
        # Exibe apenas a primeira URL encontrada se não houver "https://d.rapidcdn.app/snapi e"
        print("Link de Download:", urls_encontradas[0])
else:
    print("TENTE NOVAMENTE")

time.sleep(random.uniform(1, 3))




   

time.sleep(random.uniform(1, 3))
  
navegador.quit()

