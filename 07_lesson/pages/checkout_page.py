from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutPage(BasePage):
    # Локаторы формы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")

    # Локаторы итоговой страницы
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")

    def fill_shipping_info(self, first_name, last_name, postal_code):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.POSTAL_CODE_INPUT, postal_code)
        return self

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)
        return self

    def get_total_price(self):
        element = self.find_element(self.TOTAL_LABEL)
        return element.text

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)