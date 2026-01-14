import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


@allure.epic("SauceDemo Web Application")
@allure.feature("Checkout Process")
@allure.story("Оформление заказа")
class CheckoutPage(BasePage):
    """
    Page Object для страницы оформления заказа.
    Содержит методы для заполнения данных и завершения покупки.
    """

    # Локаторы формы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")

    # Локаторы итоговой страницы
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    @allure.step("Заполнение информации о доставке")
    def fill_shipping_info(self, first_name, last_name, postal_code):
        """
        Заполняет форму данными для доставки.

        Args:
            first_name: Имя
            last_name: Фамилия
            postal_code: Почтовый индекс

        Returns:
            CheckoutPage: Текущий экземпляр страницы
        """
        with allure.step("Заполнение формы доставки"):
            allure.attach(
                f"📝 Данные для доставки:\n"
                f"Имя: {first_name}\n"
                f"Фамилия: {last_name}\n"
                f"Индекс: {postal_code}",
                name="Данные клиента",
                attachment_type=allure.attachment_type.TEXT
            )

            self.send_keys(self.FIRST_NAME_INPUT, first_name)
            self.send_keys(self.LAST_NAME_INPUT, last_name)
            self.send_keys(self.POSTAL_CODE_INPUT, postal_code)

            self._attach_screenshot("shipping_info_filled")

        return self

    @allure.step("Клик по кнопке Continue")
    def click_continue(self):
        """
        Переходит к следующему шагу оформления.

        Returns:
            CheckoutPage: Текущий экземпляр страницы
        """
        self.click(self.CONTINUE_BUTTON)
        self._attach_screenshot("after_continue_click")
        return self

    @allure.step("Получение итоговой суммы")
    def get_total_price(self):
        """
        Получает итоговую сумму заказа.

        Returns:
            str: Итоговая сумма или сообщение об ошибке
        """
        try:
            element = self.find_element(self.TOTAL_LABEL)
            total_text = element.text

            allure.attach(
                f"💰 Итоговая сумма: {total_text}",
                name="Итоговая сумма",
                attachment_type=allure.attachment_type.TEXT
            )

            return total_text

        except Exception as e:
            allure.attach(
                f"⚠️ Не удалось получить итоговую сумму: {str(e)}",
                name="Ошибка",
                attachment_type=allure.attachment_type.TEXT
            )
            return "Не удалось получить сумму"

    @allure.step("Завершение оформления заказа")
    def finish_checkout(self):
        """
        Завершает оформление заказа.

        Returns:
            CheckoutPage: Текущий экземпляр страницы
        """
        total_price = self.get_total_price()
        self.click(self.FINISH_BUTTON)

        allure.attach(
            f"✅ Заказ оформлен\n"
            f"Итоговая сумма: {total_price}",
            name="Завершение заказа",
            attachment_type=allure.attachment_type.TEXT
        )

        self._attach_screenshot("order_completed")
        return self

    @allure.step("Проверка успешного оформления")
    def verify_success_message(self):
        """
        Проверяет сообщение об успешном оформлении заказа.

        Returns:
            str: Текст сообщения или пустая строка
        """
        try:
            element = self.find_element(self.SUCCESS_MESSAGE, timeout=5)
            message = element.text

            allure.attach(
                f"🎉 Сообщение об успехе: {message}",
                name="Сообщение",
                attachment_type=allure.attachment_type.TEXT
            )

            return message

        except:
            allure.attach(
                "⚠️ Сообщение об успехе не найдено",
                name="Предупреждение",
                attachment_type=allure.attachment_type.TEXT
            )
            return ""

    @allure.step("Отмена оформления заказа")
    def cancel_checkout(self):
        """
        Отменяет оформление заказа.

        Returns:
            CartPage: Страница корзины
        """
        self.click(self.CANCEL_BUTTON)

        allure.attach(
            "❌ Оформление заказа отменено",
            name="Отмена заказа",
            attachment_type=allure.attachment_type.TEXT
        )

        from .cart_page import CartPage
        return CartPage(self.driver)