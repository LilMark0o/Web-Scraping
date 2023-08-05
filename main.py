import logic
from selenium import webdriver
import time

carrera = "Ingeniero Quimico"
ciudad = "Bogotá, DC"


def run():

    driver = webdriver.Chrome()

    logic.iniciar(driver, carrera, ciudad)
    logic.explotarData(driver, carrera, ciudad)
    #! ya explota los datos solicitados, ahora debemos:
    #! ya los limpia y mete a la base de datos
    # - organizarlos y consultarlos

    time.sleep(5)
    driver.quit()


run()
