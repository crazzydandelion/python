from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")
username_field = "#username"
password_field = "#password"
input = driver.find_element(By.CSS_SELECTOR, username_field)
input.send_keys("tomsmith")
input = driver.find_element(By.CSS_SELECTOR, password_field)
input.send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button").click()
flash = driver.find_element(By.CSS_SELECTOR, "#flash")
print(flash.text)
driver.quit()