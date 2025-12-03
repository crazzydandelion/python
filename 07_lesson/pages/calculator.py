from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    # Локаторы элементов
    DELAY_FIELD = (By.ID, 'delay')
    BUTTON_7 = (By.CLASS_NAME, "btn-outline-primary")
    BUTTON_PLUS = (By.CLASS_NAME, "btn-outline-success")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_EXECUTE = (By.CLASS_NAME, "btn-outline-warning")
    RESULT_SCREEN = (By.CLASS_NAME, "screen")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open_calculator(self, url: str):
        self.driver.get(url)

    def set_delay(self, delay: int):
        delay_field = self.driver.find_element(*self.DELAY_FIELD)
        delay_field.clear()
        delay_field.send_keys(str(delay))

    def click_button(self, button_locator):
        button = self.driver.find_element(*button_locator)
        button.click()

    def get_result(self):
        # Сначала ждем появления текста
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT_SCREEN, "15")
        )
        # Затем получаем текст из элемента
        result_element = self.driver.find_element(*self.RESULT_SCREEN)
        return result_element.text
