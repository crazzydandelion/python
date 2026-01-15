import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


@allure.epic("SauceDemo Web Application")
@allure.feature("Product Catalog")
@allure.story("Главная страница с товарами")
class MainPage(BasePage):
    """
    Page Object для главной страницы SauceDemo.
    Содержит методы для работы с товарами и корзиной.
    """

    # Локаторы товаров
    BACKPACK_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    T_SHIRT_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-onesie")

    # Локаторы корзины
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    # Локаторы товаров для проверки
    BACKPACK_TITLE = (By.CSS_SELECTOR, "#item_4_title_link .inventory_item_name")
    T_SHIRT_TITLE = (By.CSS_SELECTOR, "#item_1_title_link .inventory_item_name")
    ONESIE_TITLE = (By.CSS_SELECTOR, "#item_2_title_link .inventory_item_name")

    @allure.step("Добавление рюкзака в корзину")
    def add_backpack_to_cart(self):
        """
        Добавляет товар 'Sauce Labs Backpack' в корзину.

        Returns:
            MainPage: Текущий экземпляр страницы
        """
        self.click(self.BACKPACK_ADD_BTN)
        allure.attach(
            f"🛍️ Добавлен товар: Sauce Labs Backpack\n"
            f"Цена: $29.99",
            name="Добавление товара",
            attachment_type=allure.attachment_type.TEXT
        )
        self._attach_screenshot("backpack_added")
        return self

    @allure.step("Добавление футболки в корзину")
    def add_t_shirt_to_cart(self):
        """
        Добавляет товар 'Sauce Labs Bolt T-Shirt' в корзину.

        Returns:
            MainPage: Текущий экземпляр страницы
        """
        self.click(self.T_SHIRT_ADD_BTN)
        allure.attach(
            f"🛍️ Добавлен товар: Sauce Labs Bolt T-Shirt\n"
            f"Цена: $15.99",
            name="Добавление товара",
            attachment_type=allure.attachment_type.TEXT
        )
        self._attach_screenshot("tshirt_added")
        return self

    @allure.step("Добавление комбинезона в корзину")
    def add_onesie_to_cart(self):
        """
        Добавляет товар 'Sauce Labs Onesie' в корзину.

        Returns:
            MainPage: Текущий экземпляр страницы
        """
        self.click(self.ONESIE_ADD_BTN)
        allure.attach(
            f"🛍️ Добавлен товар: Sauce Labs Onesie\n"
            f"Цена: $7.99",
            name="Добавление товара",
            attachment_type=allure.attachment_type.TEXT
        )
        self._attach_screenshot("onesie_added")
        return self

    @allure.step("Получение количества товаров в корзине")
    def get_cart_items_count(self):
        """
        Получает количество товаров в корзине.

        Returns:
            str: Количество товаров или "0"
        """
        try:
            badge = self.find_element(self.CART_BADGE, timeout=2)
            count = badge.text
            allure.attach(
                f"🛒 Товаров в корзине: {count}",
                name="Счетчик корзины",
                attachment_type=allure.attachment_type.TEXT
            )
            return count
        except:
            return "0"

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """
        Переходит на страницу корзины.

        Returns:
            CartPage: Страница корзины
        """
        cart_count = self.get_cart_items_count()
        self.click(self.CART_LINK)

        allure.attach(
            f"➡️ Переход в корзину\n"
            f"Товаров в корзине: {cart_count}",
            name="Навигация в корзину",
            attachment_type=allure.attachment_type.TEXT
        )

        from .cart_page import CartPage
        return CartPage(self.driver)

    @allure.step("Проверка наличия товаров на странице")
    def verify_products_displayed(self):
        """
        Проверяет, что все основные товары отображаются на странице.

        Returns:
            bool: True если все товары отображаются
        """
        products = [
            ("Sauce Labs Backpack", self.BACKPACK_TITLE),
            ("Sauce Labs Bolt T-Shirt", self.T_SHIRT_TITLE),
            ("Sauce Labs Onesie", self.ONESIE_TITLE)
        ]

        displayed_products = []
        for product_name, locator in products:
            try:
                element = self.find_element(locator, timeout=2)
                if element.is_displayed():
                    displayed_products.append(product_name)
            except:
                pass

        result = len(displayed_products) == len(products)

        allure.attach(
            f"🔍 Проверка отображения товаров:\n"
            f"Ожидалось: {len(products)} товаров\n"
            f"Найдено: {len(displayed_products)} товаров\n"
            f"Отображаются: {', '.join(displayed_products) if displayed_products else 'Нет товаров'}\n"
            f"Результат: {'✅ Успех' if result else '❌ Не все товары отображаются'}",
            name="Проверка товаров",
            attachment_type=allure.attachment_type.TEXT
        )

        return result