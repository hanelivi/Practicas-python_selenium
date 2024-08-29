#from selecciona el modulo instalado 
#import importa el driver del chrome
from selenium import webdriver
from ctypes.wintypes import SERVICE_STATUS_HANDLE
from lib2to3.pgen2 import driver
import time
# Configura las opciones de Chrome para usar un perfil específico
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/FM/AppData/Local/Google/Chrome/User Data/Default")

# Configura el servicio de ChromeDriver con la ruta adecuada
service = SERVICE_STATUS_HANDLE(executable_path="C:\dchrome\chromedriver")

# Inicia el WebDriver con el servicio y las opciones configuradas
driver = webdriver.Chrome(service=service, options=options)

# Abre WhatsApp Web
driver.get("https://web.whatsapp.com/")


time.sleep(15)
