import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

opc = Options()
opc.add_argument("--window-size=1020,1200")

# Utiliza ChromeDriverManager para obtener la ruta del controlador de Chrome
driver_path = ChromeDriverManager().install()

# Crea el controlador de Chrome utilizando la ruta del controlador
navegador = webdriver.Chrome(executable_path=driver_path, options=opc)

navegador.get("https://es-la.facebook.com/")

txtEmail = navegador.find_element(By.NAME, "email")
txtEmail.send_keys("usuario@gmail.com")
time.sleep(2)

txtPassword = navegador.find_element(By.NAME, "pass")
txtPassword.send_keys("***************")
time.sleep(2)

navegador.save_screenshot("img_test.png")

btnLogin = navegador.find_element(By.NAME, "login")
btnLogin.click()

print(navegador.title)

time.sleep(5)

navegador.quit()  # No olvides cerrar el navegador cuando hayas terminado

# Utiliza ChromeDriverManager para obtener la ruta del controlador de Chrome nuevamente
driver_path = ChromeDriverManager().install()

# Crea un segundo controlador de Chrome utilizando la nueva ruta del controlador
navegador2 = webdriver.Chrome(executable_path=driver_path, options=opc)

# Realiza las operaciones que necesites en el segundo navegador (navegador2)
# Por ejemplo, puedes abrir una nueva URL y realizar otras acciones aquí

# No olvides cerrar el segundo navegador cuando hayas terminado
navegador2.quit()
