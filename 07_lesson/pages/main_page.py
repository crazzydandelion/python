from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    # Локаторы товаров
    BACKPACK_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    T_SHIRT_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-onesie")

    # Локаторы корзины
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD_BTN)
        return self

    def add_t_shirt_to_cart(self):
        self.click(self.T_SHIRT_ADD_BTN)
        return self

    def add_onesie_to_cart(self):
        self.click(self.ONESIE_ADD_BTN)
        return self

    def get_cart_items_count(self):
        try:
            return self.find_element(self.CART_BADGE).text
        except:
            return "0"

    def go_to_cart(self):
        self.click(self.CART_LINK)
        from .cart_page import CartPage
        return CartPage(self.driver)