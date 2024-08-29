#from selecciona el modulo instalado 
#import importa el driver del chrome
from selenium import webdriver
from ctypes.wintypes import SERVICE_STATUS_HANDLE
from lib2to3.pgen2 import driver
#importa el webdriver para ingresar datos
from selenium.webdriver.common.keys import Keys
#importa el tiempo de ejecucion de prueba
import time
from selenium.webdriver.common.by import By

#Abre el driver chrome
service = SERVICE_STATUS_HANDLE(executable_path="C:\dchrome\chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://gmail.com")


#INGRESA CORREO
usuario = driver.find_element("id","identifierId") #Se le indica que debe buscar un elemento por un id
usuario.send_keys("hiramelivi@gmail.com") #Se le indica que debe ingresar un texto
usuario.send_keys(Keys.ENTER) #Se le indica que debe hacer clic en tecla enter
time.sleep(3)

#INGRESA CONTRASEÑA
clave = driver.find_element("name","Passwd")#Se le indica que debe buscar un elemento por un nombre
clave.send_keys("H@nielv1llafranca")
clave.send_keys(Keys.ENTER)
time.sleep(5)




