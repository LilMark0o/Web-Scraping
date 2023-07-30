import logic
from selenium import webdriver
import time


def run():
    driver = webdriver.Chrome()

    logic.iniciar(driver)
    logic.explotarData(driver)

    #! ya explota los datos solicitados, ahora debemos:
    # - limpiarlos
    # - almacenarlos
    # - organizarlos

    time.sleep(5)
    driver.quit()
run()