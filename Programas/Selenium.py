# import time
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

a = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size= 700, 620")

navegador = webdriver.Chrome(service=a, options=opc)
navegador.get("https://es-la.facebook.com/")

txtEmail = navegador.find_element(By.NAME, "email")
txtEmail.send_keys("ayeyeye@gmail.com")

txtPassword = navegador.find_element(By.NAME, "pass")
txtPassword.send_keys("password")
print(txtEmail)
print(txtPassword)
print(navegador.title)
time.sleep(10)
