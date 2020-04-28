from bs4 import BeautifulSoup
from selenium import webdriver
from galiciaWriter import Writer

# URL a scrapear
url = "https://www.bancogalicia.com/banca/online/web/Personas/ProductosyServicios/Cotizador"

# Creamos la instancia de Selenium con Chrome, le pasamos las opciones para que corra headless (sin GUI)
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get(url)

# Con el output que nos da Selenium lo parseamos con BeautifulSoup4
soup = BeautifulSoup(driver.page_source, 'lxml')
tabla = soup.find("ul", class_="tabla")

# Parseamos los div que contienen los valores de las cotizaciones
cotizaciones = tabla.find_all("div")

# Creamos lista vacía para alojar valores parseados
cotiz_final = []

# Parseamos cada item para convertirlos en float con los valores necesarios para despues inputear en la funcion
for item in cotizaciones:
    item = item.text

    if item.isalpha() or item.isspace():
        pass
    else:
        item = item.replace(',', '.')
        try:
            item = float(item)
        except ValueError:
            continue
        cotiz_final.append(item)

print("USD C | USD V | EUR C | EUR V")
print(cotiz_final)

# Cerramos la instancia de Chromium
driver.quit()

# Escribimos en la DB
Writer(cotiz_final)
