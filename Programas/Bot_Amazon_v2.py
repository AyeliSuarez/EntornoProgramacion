import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

a = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size=700,620")
navegador = webdriver.Chrome(service=a, options=opc)
navegador.get("https://www.amazon.com.mx/")

amount_products = int(input("Cuantos productos desea comparar: "))
data = {"Nombre": [], "Rating": [], "Precio": [], "Fecha entrega": []}
product = input("Introduce el producto que deseas buscar:")

search = navegador.find_element(By.NAME, "field-keywords")
search.send_keys(product)
search.send_keys(Keys.RETURN) #enter

time.sleep(12)
soup = BeautifulSoup(navegador.page_source, "html.parser")
# info
results = soup.find_all("div", {"data-component-type": "s-search-result"})

for i, results in enumerate(results):
    if i == amount_products:
        break

    name = results.find("h2", attrs={"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-4"})
    rating = results.find("span", attrs={"class": "a-icon-alt"})
    price = results.find("span", attrs={"class": "a-offscreen"})
    deliver_date = results.find("div", attrs={"class": "a-row s-align-children-center"})

    # Verificar los elementos
    name_text = name.text if name else " "
    rating_text = rating.text if rating else " "
    price_text = price.text if price else " "
    deliver_date_text = deliver_date.text if deliver_date else " "
    data["Nombre"].append(name_text)
    data["Rating"].append(rating_text)
    data["Precio"].append(price_text)
    data["Fecha entrega"].append(deliver_date_text)

df = pd.DataFrame(data)
df.to_csv('datasets/productos_amazon.csv', index=False)
print(f"{amount_products} productos guardados en 'productos_amazon.csv'")

navegador.quit()
