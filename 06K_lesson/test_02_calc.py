import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def test_calc():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay = driver.find_element(By.ID, 'delay')
    delay.clear()
    delay.send_keys(45)
    button_7 = driver.find_element(By.CLASS_NAME, "btn-outline-primary")
    button_7.click()
    button_plus = driver.find_element(By.CLASS_NAME, "btn-outline-success")
    button_plus.click()
    button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()
    button_execute = driver.find_element(By.CLASS_NAME, "btn-outline-warning")
    button_execute.click()
    wait = WebDriverWait(driver, timeout=45)
    wait.until(
        EC.text_to_be_present_in_element( (By.CLASS_NAME, "screen"), "15")
    )
    txt = driver.find_element(By.CLASS_NAME, "screen").text
    assert txt == "15"
    driver.quit()



