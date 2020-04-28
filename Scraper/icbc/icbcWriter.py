import os
import sys
import json
import mysql.connector

# Funcion para escribir directamente en la base de datos los valores scrapeados
def Writer(lista):

    print("Iniciando proceso de carga de datos en DB")

    # Creamos variables para almacenar los valores de la tupla, ya que por seguridad vamos a inputear en SQL con string substitution y una tupla
    usdc, usdv = lista[0], lista[1]

    # Creamos el directorio relativo para el archivo con las credenciales de la DB:
    parentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    credentials = parentDir + '/conf.json'

    # Levanta los datos de conexion de la database de config.json en un objeto de Python
    with open(credentials) as data_file:
        settings = json.load(data_file)

    # Nos conectamos a la DB con el objeto creado para no hardcodear las PW (casihackeeeer)
    mydb = mysql.connector.connect(
        host = settings["db_host"],
        user = settings["db_user"],
        passwd = settings["db_pass"],
        database = settings["database"]
        )
    print("Conexión con DB exitosa.")

    # Inicializamos el escribidor (?) de databases
    mycursor = mydb.cursor()

    print("Insertando datos...")
    # Formula de SQL
    sqlFormula = """
        INSERT INTO icbc VALUES (
        CURDATE(),
        %s, %s
        );
    """

    # Tupla que acepta la formula
    datos = (usdc, usdv)

    # Inserta en la databases
    mycursor.execute(sqlFormula, datos) # SIEMPRE separar por ',' y feedear tupla, nunca con '%'
    mydb.commit()
    print('Proceso finalizado')

# DB Schema:
#
# MariaDB [cotizame]> describe icbc;
# +---------+--------------+------+-----+---------+-------+
# | Field   | Type         | Null | Key | Default | Extra |
# +---------+--------------+------+-----+---------+-------+
# | fecha   | date         | NO   | PRI | NULL    |       |
# | usd_com | decimal(4,2) | YES  |     | NULL    |       |
# | usd_ven | decimal(4,2) | YES  |     | NULL    |       |
# +---------+--------------+------+-----+---------+-------+
# 5 rows in set (0.000 sec)
