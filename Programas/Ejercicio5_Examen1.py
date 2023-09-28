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
navegador.get("https://pypi.org/account/login/")


user = navegador.find_element(By.ID, "username")
user.send_keys("AyeliSuarez")

password = navegador.find_element(By.ID, "password")
password.send_keys("12345678")

login = navegador.find_element(By.CSS_SELECTOR, "button.button--primary")
login.click()

time.sleep(20)

navegador.save_screenshot("screenshot.png")
navegador.quit()
