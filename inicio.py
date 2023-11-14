mensagem = '''
_____________________________________________________________________
_____________________________________________________________________
________/_____//_____/_/___________/_/_________|___/____//___/_______
_______/_____//_____/_/____//_____/_/____//____/__/____//___/________
______/_____//_____/_/____//_____/_/____//___/___/____//___/_________
_____/____________/_/____//_____/_/________/____/____//___/__________
____/_____//_____/_/___________/_/____/|___|___/____//___/___________
___/_____//_____/_/_____//____/_/____/_|___|___\________/____________
__/_____//_____/_/_____//____/_/____/__|___|____\______//__//__//__/_
_____________________________________________________________________
'''
for linha in mensagem.split('\n'):
    print(linha)   
  

mensagem = """
    ##########################INFO#######################
    #                        HARVARD                    #
    #                       BETA 0.0.3                  #
    #                        09/11/23                   #
    #                        Sekkin-SK                  #
    # ChatPesquisa (Disable)     | Tiktok      (Disable)#  
    # Docsity      (Disable)     | Instagram   (Enable) #
    # PasseiDireto (Disable)     | Facebook    (Disable)#
    # YouTube      (Enable)      | Scribd      (Enable) #
    #####################################################


"""
for linha in mensagem.split("\n"):
    print(linha)
    
    #PAUSE

def main():
    # Imprime uma mensagem
    print("Antes de continuar, pressione Enter para verificar se todas as bibliotecas estão instaladas.")

    # Pausa o programa
    input()

if __name__ == "__main__":
    main()

libraries_missing = False

try:
    print("  ")
    print("----------------------------------------")
    import requests
    print("  ")
    print("requestS........................Instalada.")
except ImportError:
    print("requests........................NONE")
    libraries_missing = True

try:
    from bs4 import BeautifulSoup
    print("  ")
    print("BeautifulSoup...................Instalada.")
except ImportError:
    print("BeautifulSoup...................NONE")
    libraries_missing = True

try:
    import random
    print("  ")
    print("random..........................Instalada.")
except ImportError:
    print("random..........................NONE")
    libraries_missing = True

try:
    from pytube import YouTube, Playlist
    print("  ")
    print("pytube..........................Instalada.")
except ImportError:
    print("python..........................NONE")
    libraries_missing = True

try:
    from tqdm import tqdm
    print("  ")
    print("tqdm............................Instalada.")
except ImportError:
    print("tqdm............................NONE")
    libraries_missing = True

try:
    import threading
    print("  ")
    print("threading.......................Instalada.")
except ImportError:
    print("threading.......................NONE")
    libraries_missing = True

try:
    import select
    print("  ")
    print("select..........................Instalada.")
except ImportError:
    print("select..........................NONE")
    libraries_missing = True

try:
    import sys
    print("  ")
    print("sys.............................Instalada.")
except ImportError:
    print("sys.............................NONE")
    libraries_missing = True

try:
    import re
    print("  ")
    print("re..............................Instalada")
except ImportError:
    print("re..............................NONE")
    libraries_missing = True

try:
    import time
    print("  ")
    print("time............................Instalada.")
except ImportError:
    print("time............................NONE")
    libraries_missing = True

try:
    import os
    print("  ")
    print("os..............................Instalada.")
except ImportError:
    print("os..............................NONE")
    libraries_missing = True

try:
    import importlib
    print("  ")
    print("importlib.......................Instalada.")
    print("  ")
except ImportError:
    print("importlib.......................NONE")
    libraries_missing = True


try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    print("Selenium........................Instalada.")
    print("  ")
except ImportError:
    print("Seleniun........................NONE")
    libraries_missing = True


if libraries_missing:

    print("Verifique as bibliotecas que faltam antes de continuar.")
else:
    print("  ")
    print("Todas as bibliotecas estão instaladas.")

    print("----------------------------------------")
    # Coloque aqui o restante do seu código


def main():
    # Imprime uma mensagem
    print("Pressione Enter")

    # Pausa o programa
    input()

if __name__ == "__main__":
    main()
    
    import princ
