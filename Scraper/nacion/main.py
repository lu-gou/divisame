from bs4 import BeautifulSoup
import requests
import json
import mysql.connector
from nacionWriter import Writer

source = requests.get('https://www.bna.com.ar/Personas').text

# Aplica BeautifulSoup a la variable $source, creando un objeto de BeautifulSoup
s_source = BeautifulSoup(source, 'lxml')

# Creamos una lista vacía para alojar todos los valores parseados
today_list = []

# Let the magic begin
tabla = s_source.find(id='billetes')
data = tabla.findAll('td')

for i in data:
    i = i.text
    i = i.replace(',', '.')

    try:
        i = "{0:.2f}".format(float(i))
        i = float(i)
    except ValueError:
        pass
    today_list.append(i)

del today_list[0], today_list[2], today_list[4] # Eliminamos los valores de los headers y quedan solo los floats con compra/venta
today_list[4] = today_list[4] / 100
today_list[5] = today_list[5] / 100 # Arreglamos formato porque por algun motivo el Nacion muestra la cotizacion del real *100

# Listo! Lita con cotizaciones lista. Orden de valores:
print("USD C | USD V | EUR C | EUR V | REA C | REA V")
print(today_list)

# Escribimos en la DB
Writer(today_list)
