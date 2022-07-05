from selenium import webdriver
from os import remove
import time
import pandas as pd


# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

## Cargar la url y el patch
url = "https://pharma.valassis.es/"
## Ruta de acceso del patch
patch = "C:\\Users\\Francis\\Documents\\Savi\\chromedriver.exe" 

driver = webdriver.Chrome(patch, chrome_options=options) # Iniciar web con las opciones
driver.get(url)

## Crear las variables de los selectores 
boton_inicio_sesion = '//button[@class="btn btn-outline-dark"]'
user = '//input[@name="j_username"]'
psr = '//input[@name="j_password"]'
login = '//button[@class="btn btn-valGreen block full-width m-b"]'
list_venta = '//a[@href="/promotion/index"]'
upload_file = '//input[@name="fileUpload"]'
subir_documento = '//button[@class="btn btn-valGreen block  float-right"]'


## Iniciar las acciones 
driver.find_element_by_xpath(boton_inicio_sesion).click()
driver.find_element_by_xpath(user).send_keys("farmaciapz@movistar.es")
driver.find_element_by_xpath(psr).send_keys("Canarias1961")
driver.find_element_by_xpath(login).click()
driver.find_element_by_xpath(list_venta).click()
driver.find_element_by_xpath(upload_file).send_keys("C:\\Users\\Francis\\Documents\\Savi\\Promos\\Ventas.xlsx")

time.sleep(4)

driver.find_element_by_xpath(subir_documento).click()


remove("C:\\Users\\Francis\\Documents\\Savi\\Promos\\Ventas.xlsx")

time.sleep(2)
driver.quit()
