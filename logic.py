from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
import time

def iniciar(driver):
    carrera = "ingenieria quimica"
    ciudad = "Bogotá, dc"
    driver.get("https://co.computrabajo.com/")

    search = driver.find_element(By.ID,"prof-cat-search-input")
    search.send_keys(carrera)
    search = driver.find_element(By.ID,"place-search-input")
    search.send_keys(ciudad)
    search.send_keys(Keys.RETURN)

# print(driver.page_source)
# this prints out the source code of the whooole page
def buscar(driver):
    try:
        trabajosDisponibles = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"box_offer "))
        )
        trabajosDisponibles = driver.find_elements(By.CLASS_NAME,"box_offer ")
        for trabajo in trabajosDisponibles:
            checkForNotifications(driver)
            trabajo.click()
            wholeBox = driver.find_element(By.CLASS_NAME,"box_detail")
            # print(driver.current_url)
            my_element_id = "/html/body/main/div[6]/div/div[2]/div[2]/div[5]/div/div[1]/div/span"
            ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
            your_element = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions)\
                            .until(expected_conditions.presence_of_element_located((By.XPATH, my_element_id)))

            your_elements = driver.find_elements(By.XPATH,my_element_id)

            #! estoy seguro que esto se puede hacer más lindo
            #! y estético, pero no supe xd
            time.sleep(0.1)
            
            if (len(your_elements)>0):
                for id in range(len(your_elements)-1):
                    pathChiquito = my_element_id+"["+str(id+1)+"]"
                    try:
                        your_element = WebDriverWait(driver, 5,ignored_exceptions=ignored_exceptions)\
                                        .until(expected_conditions.presence_of_element_located((By.XPATH, pathChiquito)))
                        
                        texto = your_element.text
                        if (("$" in texto) or ("0" in texto)):
                            print(texto)
                    except Exception as e:
                        print("me dañé")
        # cuando se acaben los trabajos vamos a cargar la siguiente página y así
    except Exception as e:
        driver.quit()
    
def siguientePagina(driver):
    checkForNotifications(driver)
    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
    my_element_id = '//*[@id="offersGridOfferContainer"]/div[8]/span[2]'

    your_element = WebDriverWait(driver,10,ignored_exceptions=ignored_exceptions)\
                    .until(expected_conditions.presence_of_element_located((By.XPATH, my_element_id)))
    your_element.click()
    time.sleep(2)
    checkForNotifications(driver)
    print("-- pasamos de pagina --")
    
def checkForNotifications(driver):
    try:
            pathRaro = '//*[@id="pop-up-webpush-sub"]/div[2]/div/button[1]'
            ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
            your_element = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions)\
                    .until(expected_conditions.presence_of_element_located((By.XPATH, pathRaro)))
            your_element.click()
    except:
        pass
    time.sleep(0.5)

def explotarData(driver):
    buscar(driver)
    siguientePagina(driver)
    buscar(driver)
    siguientePagina(driver)
    buscar(driver)
    siguientePagina(driver)
    buscar(driver)
    siguientePagina(driver)

