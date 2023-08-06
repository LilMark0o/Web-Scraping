import logic
from selenium import webdriver
import time

carrera = "Analisis de Datos"
ciudad = "Bogotá, DC"


def run():

    driver = webdriver.Chrome()

    logic.iniciar(driver, carrera, ciudad)
    logic.explotarData(driver, carrera, ciudad)
    # ? ya explota los datos solicitados
    # ? ya los limpia y mete a la base de datos
    #! - organizarlos y consultarlos

    time.sleep(5)
    driver.quit()


run()
