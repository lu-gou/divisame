from bs4 import BeautifulSoup
from selenium import webdriver
from provinciaWriter import Writer

# URL a scrapear
url = "https://www.bancoprovincia.com.ar/Productos/inversiones/dolares_bip/dolares_bip_info_gral"

# Creamos la instancia de Selenium con Chrome, le pasamos las opciones para que corra headless (sin GUI)
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get(url)

valores_scrapeados = []
cotiz_final = []

# Con el output que nos da Selenium lo parseamos con BeautifulSoup4
soup = BeautifulSoup(driver.page_source, 'lxml')

tabla = soup.find("div", id="cyvDolar_inc")
cotizaciones = tabla.find_all("div", class_="w3-col")

# Hay una banda de divs de esa clase en $tabla, pero solo 2 con numeros, así que es facil de filtrar:
for item in cotizaciones:
    item = item.text
    if "." in item:
        try:
            item = "{0:.2f}".format(float(item))
            item = float(item)
            cotiz_final.append(item)
        except ValueError:
            pass

# Imprimimos en pantalla los valores scrapeados de type float
print("USD C | USD V")
print(cotiz_final)

# Cerramos la instancia de Chromium
driver.quit()

# Escribimos en la DB
Writer(cotiz_final)
