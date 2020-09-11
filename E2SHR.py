import os
import sys
try:
    import requests
except ImportError:
    os.system('pip install requests')
    print('Installing requests...')
    print('Ejecuta de nuevo tu script...')
    exit()

try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    os.system('pip install BeautifulSoup4')
    print('Installing BeautifulSoup4...')
    print('Ejecuta de nuevo tu script...')
    exit()

try:
    import webbrowser
except ImportError:
    os.system('pip install webbrowser')
    print('Installing webbrowser...')
    print('Ejecuta de nuevo tu script...')
    exit()

#  Sofia Hernandez Rodriguez.
"""This program searches for news towards a specific main page
from a range and acronyms requested to show the urls of the news
found at the end and at the same time open them in the browser"""

print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango, finRango = finRango, inicioRango
for i in range(inicioRango, finRango, 1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get(url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content, "html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content, "html.parser")
                parrafos = soup2.select("p")
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo", url2)
                        webbrowser.open(url2)
                        break
                        