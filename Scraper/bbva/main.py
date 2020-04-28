from bs4 import BeautifulSoup
import requests
import json
import mysql.connector
from bbvaWriter import Writer

# Solicita el source code de la pagina ingresada y lo retorna como texto en la variable $source
# En este caso se encontro el modulo embebido en la pagina de cotizaciones, diretctamente retorna la tabla con las cotizaciones
source = requests.get('https://hb.bbv.com.ar/fnet/mod/inversiones/NL-dolareuro.jsp?origen=net').text

# Aplica BeautifulSoup a la variable $source, creando un objeto de BeautifulSoup
s_source = BeautifulSoup(source, 'lxml')

# Creamos una lista vacía para alojar todos los valores parseados
today_list = []

# En este caso, BBVA aloja todos los valores de las cotizaciones en un span cada una, así que se hace un loop con el find y se descartan los span que pueda haber y que no coincidan con lo que buscamos:
for i in s_source.find_all('span'):
    spans = i.text

    if len(spans) < 10: # Descartamos los span que sean mas largos
        today_list.append(spans)

#print(today_list) # Desmarcar para verificar el valor de la lista con las cotizaciones, por cualquier cambio

# Formateo y cambio de tipo de data
cotiz_final = []

# Perdón por esto
for i in today_list:

    i = i.replace(',', '.') # BBVA muestra decimales con ",", reemplazamos por "."

    if i.isalpha():
        print(i, 'compra/venta') # Un output lindo nada más
    else:
        i = "{0:.2f}".format(float(i))
        i = float(i)
        cotiz_final.append(i)
        print(i)

#print(cotiz_final) # Sacar comment para verificar la lista final

# Escribimos en la DB
Writer(cotiz_final)
