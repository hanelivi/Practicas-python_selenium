#from selecciona el modulo instalado 
#import importa el driver del chrome
from selenium import webdriver
from ctypes.wintypes import SERVICE_STATUS_HANDLE
from lib2to3.pgen2 import driver

#Abre el driver chrome
service = SERVICE_STATUS_HANDLE(executable_path="C:\dchrome\chromedriver")
driver = webdriver.Chrome(service=service)

#se le dice que con .get abra google
driver.get("http://google.com")

#se le dice que con .close cierre la ventana
driver.close()
