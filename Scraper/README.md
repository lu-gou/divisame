# Scrapers

En esta sección están todos los scripts que scrapean las páginas púbicas de cada banco. Si bien las librerías y los métodos utilizados son casi los mismo para todos, hay mucha diferencia en cómo cada banco muestra la información (cada página un mundo diferente), por eso hay básicamente un script para cada banco.

La base de datos en la cual guarda la data scrapeada es propia, por lo pronto local, aunque podrías feedear los datos de la conexión en cada $BANCO$Writer.py para customizarla. Las credenciales de acceso tienen que estar en un .json en el directorio /Scraper.

Hay bastantes cosas hardcodeadas que se podrían hacer más relativas y algunas cosas bastante crudencias, pero hey... it works!

Cualquier sugerencia es bienvenida en nachichuri@gmail.com

### Paquetes requeridos:

- Python 3
<details>
  <summary>Python 3</summary>

</details>

- MariaDB

<details>
  <summary>BeautifulSoup4</summary>
    <p>

    ```console
    pip install beautifulsoup4
    ```

    </p>
  </details>
<details>
  <summary>MySQL Connector</summary>
    <p>

    ```console
    pip install mysql-connector
    ```

    </p>
  </details>
<details>
  <summary>LXML</summary>
    <p>

    ```console
    pip install lxml
    ```

    </p>
  </details>
<details>
  <summary>- chromedriver</summary>
    <p>

    ```console
    ...
    ```

    </p>
  </details>
