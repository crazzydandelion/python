from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    # Локаторы
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        from .checkout_page import CheckoutPage
        return CheckoutPage(self.driver)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)
        from .main_page import MainPage
        return MainPage(self.driver)