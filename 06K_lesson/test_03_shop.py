import pytest
# from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    username_field = "#user-name"
    password_field = "#password"
    input = driver.find_element(By.CSS_SELECTOR, username_field)
    input.send_keys("standard_user")
    input = driver.find_element(By.CSS_SELECTOR, password_field)
    input.send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    first_name = "#first-name"
    last_name = "#last-name"
    postal = "#postal-code"
    input = driver.find_element(By.CSS_SELECTOR, first_name)
    input.send_keys("Vladimir")
    input = driver.find_element(By.CSS_SELECTOR, last_name)
    input.send_keys("Orlov")
    input = driver.find_element(By.CSS_SELECTOR, postal)
    input.send_keys("454131")
    driver.find_element(By.ID, "continue").click()
    sum = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_price = sum.text
    assert total_price == "Total: $58.29"
    driver.quit()

