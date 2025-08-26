from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")
input_field = "input"
input = driver.find_element(By.CSS_SELECTOR, input_field)
input.send_keys("Sky")
sleep(2)
input.clear()
input.send_keys("Pro")
sleep(2)
driver.quit()