from selenium import webdriver
from os import remove
import time
import pandas as pd


# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

## Cargar la url y el patch
url = "https://canarycloud.quickconnect.to/?launchApp=SYNO.SDS.Drive.Application"
## Ruta de acceso del patch
patch = "C:\\Users\\alterEgo91\\Proyectos\\Bots\\chromedriver.exe"


driver = webdriver.Chrome(patch, chrome_options=options) # Iniciar web con las opciones
driver.get(url)
time.sleep(5)
## Crear las variables de los selectores 
user = '//input[@name="username"]'
siguiente_user = '//div[@class="login-btn"]'
psr = '//input[@name="current-password"]'
psr2 = '(3L3na@22)'
login = '//div[@class="login-btn"]'
new_document = '//em[@class="syno-d-create-btn syno-d-text-button x-btn-noicon"]'


## Iniciar las acciones 
driver.find_element_by_xpath(user).send_keys("OutsideTranding")
driver.find_element_by_xpath(siguiente_user).click()
time.sleep(1)
driver.find_element_by_xpath(psr).send_keys(psr2)
driver.find_element_by_xpath(login).click()
time.sleep(1)
driver.find_element_by_xpath(new_document).click()
time.sleep(2)



driver.quit()
