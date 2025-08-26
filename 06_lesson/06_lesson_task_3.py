from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.implicitly_wait(5)
src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")

print(src)

driver.quit()