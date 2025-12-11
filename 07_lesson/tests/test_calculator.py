import pytest
from selenium import webdriver
from pages.calculator import CalculatorPage  # Проверяем путь


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_addition(driver):
    calculator = CalculatorPage(driver)
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    calculator.open_calculator(url)
    calculator.set_delay(45)

    calculator.click_button(calculator.BUTTON_7)
    calculator.click_button(calculator.BUTTON_PLUS)
    calculator.click_button(calculator.BUTTON_8)
    calculator.click_button(calculator.BUTTON_EXECUTE)

    result = calculator.get_result()
    assert result == "15"