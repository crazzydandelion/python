from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
def test_form():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(10)
    first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
    first_name.send_keys("Иван")
    first_name.click()
    last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
    last_name.send_keys("Петров")
    last_name.click()
    address_input = driver.find_element(By.CSS_SELECTOR, "[name='address']")
    address_input.send_keys("Ленина, 55-3")
    address_input.click()
    email_address = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
    email_address.send_keys("test@skypro.com")
    email_address.click()
    phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
    phone_number.send_keys("+7985899998787")
    phone_number.click()
    city_name = driver.find_element(By.CSS_SELECTOR, "[name='city']")
    city_name.send_keys("Москва")
    city_name.click()
    country_name = driver.find_element(By.CSS_SELECTOR, "[name='country']")
    country_name.send_keys("Россия")
    country_name.click()
    job_position = driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
    job_position.send_keys("QA")
    job_position.click()
    company_name = driver.find_element(By.CSS_SELECTOR, "[name='company']")
    company_name.send_keys("SkyPro")
    company_name.click()
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary")
    submit_button.click()
    zip_field = driver.find_element(By.ID, "zip-code")
    zip_color = zip_field.value_of_css_property("background-color")
    assert zip_color == "rgba(248, 215, 218, 1)"

    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field_id in fields:
        field = driver.find_element(By.ID, field_id)
        field_color = field.value_of_css_property("background-color")
        assert field_color == "rgba(209, 231, 221, 1)"

    driver.quit()

