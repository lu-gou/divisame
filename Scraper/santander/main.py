from bs4 import BeautifulSoup
import requests
import json
import mysql.connector
from santanderWriter import Writer

# Solicita el source code de la pagina ingresada y lo retorna como texto en la variable $source
# En este caso se encontro el modulo embebido en la pagina de cotizaciones, diretctamente retorna la tabla con las cotizaciones
source = requests.get('https://banco.santanderrio.com.ar/exec/cotizacion/index.jsp').text

# Aplica BeautifulSoup a la variable $source, creando un objeto de BeautifulSoup
s_source = BeautifulSoup(source, 'lxml')

# Comienza el scrapeo
tabla = s_source.find("div", class_="fortable")

cotizaciones = tabla.find_all("td")

# Creamos lista para anexar valores formateados
cotiz_final = []

# Formateamos los valores extraidos
for item in cotizaciones:
    item = item.text
    item = item[2:]
    if item.isalpha():
        pass
    else:
        item = item.replace(',', '.')
        item = float(item)
        cotiz_final.append(item)

print(cotiz_final) # Sacar comment para verificar la lista final

# Escribimos en la DB
Writer(cotiz_final)
