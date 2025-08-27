from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://uitestingplayground.com/textinput")
input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input.send_keys("Skypro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
updatingButton = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
print(updatingButton.text)
driver.quit()