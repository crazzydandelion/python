import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


@allure.epic("SauceDemo Web Application")
@allure.feature("Shopping Cart")
@allure.story("Страница корзины покупок")
class CartPage(BasePage):
    """
    Page Object для страницы корзины покупок.
    Содержит методы для работы с корзиной и оформления заказа.
    """

    # Локаторы
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")

    # Локаторы элементов в корзине
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button.cart_button")

    @allure.step("Получение количества товаров в корзине")
    def get_cart_items_count(self):
        """
        Получает количество товаров в корзине.

        Returns:
            int: Количество товаров
        """
        items = self.driver.find_elements(*self.CART_ITEMS)
        count = len(items)

        allure.attach(
            f"📦 Товаров в корзине: {count}",
            name="Количество товаров",
            attachment_type=allure.attachment_type.TEXT
        )

        return count

    @allure.step("Получение списка товаров в корзине")
    def get_cart_items(self):
        """
        Получает список товаров в корзине.

        Returns:
            list: Список словарей с информацией о товарах
        """
        items = []
        try:
            names = self.driver.find_elements(*self.ITEM_NAMES)
            prices = self.driver.find_elements(*self.ITEM_PRICES)

            for i, (name_element, price_element) in enumerate(zip(names, prices)):
                item = {
                    "index": i + 1,
                    "name": name_element.text,
                    "price": price_element.text
                }
                items.append(item)

            # Логируем содержимое корзины
            if items:
                items_text = "\n".join([f"{i['index']}. {i['name']} - {i['price']}" for i in items])
                allure.attach(
                    f"🛒 Содержимое корзины:\n{items_text}\n"
                    f"Итого товаров: {len(items)}",
                    name="Содержимое корзины",
                    attachment_type=allure.attachment_type.TEXT
                )
            else:
                allure.attach(
                    "🛒 Корзина пуста",
                    name="Содержимое корзины",
                    attachment_type=allure.attachment_type.TEXT
                )

        except Exception as e:
            allure.attach(
                f"⚠️ Ошибка при получении списка товаров: {str(e)}",
                name="Ошибка",
                attachment_type=allure.attachment_type.TEXT
            )

        return items

    @allure.step("Клик по кнопке Checkout")
    def click_checkout(self):
        """
        Переходит к оформлению заказа.

        Returns:
            CheckoutPage: Страница оформления заказа
        """
        cart_items = self.get_cart_items()
        self.click(self.CHECKOUT_BUTTON)

        allure.attach(
            f"➡️ Переход к оформлению заказа\n"
            f"Товаров для оформления: {len(cart_items)}",
            name="Начало оформления",
            attachment_type=allure.attachment_type.TEXT
        )

        from .checkout_page import CheckoutPage
        return CheckoutPage(self.driver)

    @allure.step("Клик по кнопке Continue Shopping")
    def click_continue_shopping(self):
        """
        Возвращается к покупкам.

        Returns:
            MainPage: Главная страница магазина
        """
        self.click(self.CONTINUE_SHOPPING_BTN)

        allure.attach(
            "↩️ Возврат к покупкам",
            name="Продолжение покупок",
            attachment_type=allure.attachment_type.TEXT
        )

        from .main_page import MainPage
        return MainPage(self.driver)

    @allure.step("Удаление товара из корзины")
    def remove_item(self, item_index=0):
        """
        Удаляет товар из корзины.

        Args:
            item_index: Индекс товара (начиная с 0)

        Returns:
            CartPage: Текущий экземпляр страницы
        """
        try:
            remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
            if item_index < len(remove_buttons):
                item_name = self.driver.find_elements(*self.ITEM_NAMES)[item_index].text
                remove_buttons[item_index].click()

                allure.attach(
                    f"🗑️ Удален товар: {item_name}\n"
                    f"Индекс: {item_index + 1}",
                    name="Удаление товара",
                    attachment_type=allure.attachment_type.TEXT
                )

                self._attach_screenshot(f"after_removing_item_{item_index}")
            else:
                allure.attach(
                    f"⚠️ Товар с индексом {item_index} не найден",
                    name="Ошибка удаления",
                    attachment_type=allure.attachment_type.TEXT
                )
        except Exception as e:
            self._attach_screenshot("remove_item_error")
            allure.attach(
                f"❌ Ошибка при удалении товара: {str(e)}",
                name="Ошибка",
                attachment_type=allure.attachment_type.TEXT
            )

        return self