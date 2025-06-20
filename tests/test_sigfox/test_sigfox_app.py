import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@mark.sigfox
def test_scrapping_sigfox():
    driver = webdriver.Chrome()
    driver.get("https://backend.sigfox.com/auth/login")
    wait = WebDriverWait(driver, 10)  # Espera máximo 10 segundos
    logging = wait.until(EC.presence_of_element_located((By.ID, "username")))
    logging.send_keys("mlr@fciencias.uaslp.mx")
    password = driver.find_element(By.ID,"password")
    password.send_keys("Corregidora#35")
    password.send_keys(Keys.ENTER)
    wait = WebDriverWait(driver, 10)  # Espera máximo 10 segundos
    devices = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "DEVICE")))
    devices.click()
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@id="data"]/tbody/tr[2]/td[3]').click()
    time.sleep(3)
    driver.save_screenshot("devices.png")
    driver.quit()
