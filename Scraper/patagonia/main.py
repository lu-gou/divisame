from bs4 import BeautifulSoup
import requests
import json
import mysql.connector
from patagoniaWriter import Writer

# Solicita el source code de la pagina ingresada y lo retorna como texto en la variable $source
# En este caso se encontro el modulo embebido en la pagina de cotizaciones, diretctamente retorna la tabla con las cotizaciones
source = requests.get('https://ebankpersonas.bancopatagonia.com.ar/eBanking/usuarios/cotizacionMonedaExtranjera.htm').text

# Aplica BeautifulSoup a la variable $source, creando un objeto de BeautifulSoup
s_source = BeautifulSoup(source, 'lxml')

datos = s_source.find_all('td', class_='importe')
datos2 = s_source.find_all('td', class_='tdFinalRight')
#print(datos, datos2)

cotizaciones = []

for item in datos + datos2:
    item = item.text
    item = item[2:]
    item = item.replace(',', '.')
    item = float(item)
    cotizaciones.append(item)

cotiz_final = [cotizaciones[0], cotizaciones[2], cotizaciones[1], cotizaciones[3]]

print("USD C | USD V | EUR C | EUR V")
print(cotiz_final)

# Escribimos en la DB
Writer(cotiz_final)
