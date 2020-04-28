from bs4 import BeautifulSoup
from selenium import webdriver
from icbcWriter import Writer

# URL a scrapear
url = "https://www.icbc.com.ar/personas"

# Creamos la instancia de Selenium con Chrome, le pasamos las opciones para que corra headless (sin GUI)
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get(url)

cotiz_final = []

# Con el output que nos da Selenium lo parseamos con BeautifulSoup4
soup = BeautifulSoup(driver.page_source, 'lxml')

valores = soup.find_all("span", class_="moneda--valor")

compra = valores[1].text
venta = valores[0].text

# Damos formato float a los valores scrapeados
compra = compra.replace("vendés a $", "").replace(",", ".")
compra = "{0:.2f}".format(float(compra))
compra = float(compra)
cotiz_final.append(compra)

venta = venta.replace("comprás a $", "").replace(",", ".")
venta = "{0:.2f}".format(float(venta))
venta = float(venta)
cotiz_final.append(venta)

print("USD C | USD V")
print(cotiz_final)

# Cerramos la instancia de Chromium
driver.quit()

# Escribimos en la DB
Writer(cotiz_final)
