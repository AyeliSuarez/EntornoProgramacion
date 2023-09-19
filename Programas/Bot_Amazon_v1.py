import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

a = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size= 700, 620")

navegador = webdriver.Chrome(service=a, options=opc)
navegador.get("https://www.amazon.com.mx/")

product = input("Introduce el producto que deseas buscar:")

search = navegador.find_element(By.NAME, "field-keywords")
search.send_keys(product)

# enter
search.send_keys(Keys.RETURN)

time.sleep(12)
navegador.save_screenshot("captura.png")

navegador.quit()
