from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
import time

driver = None  # Inicializa driver como None

try:
    # Configuración de las opciones de Firefox
    options = Options()
    options.add_argument('--start-maximized')  # Iniciar el navegador maximizado

    # Especificar la ruta del ejecutable de Firefox
    options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"  # Ajusta la ruta según sea necesario

    # Ruta al GeckoDriver
    service = FirefoxService(executable_path='C:/Users/USER/Desktop/geckodriver/Nueva carpeta/geckodriver.exe')

    # Inicializar el navegador Firefox
    driver = webdriver.Firefox(service=service, options=options)

    # Navegar a una página web
    driver.get('https://accounts.zoho.com/signin?service_language=es&servicename=ZohoHome&signupurl=https://www.zoho.com/es-xl/signup.html&serviceurl=https://www.zoho.com/es-xl/all-products.html&ireft=nhome&src=es-xl-header')
    time.sleep(10)
    username_field = driver.find_element(By.ID, 'login_id')
    username_field.send_keys('manuel.aguilar@i-condor.com')

    btn_iniciar_sesion = driver.find_element(By.ID, 'nextbtn')
    btn_iniciar_sesion.click()
    time.sleep(10)

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    # Cerrar el navegador si driver fue inicializado
    if driver:
        driver.quit()
