import allure
import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@allure.epic("SauceDemo Web Application")
@allure.feature("End-to-End Flow")
@allure.story("Полный цикл покупки")
class TestCompletePurchase:
    """
    End-to-end тест полного цикла покупки в SauceDemo.
    Тест проверяет весь процесс от авторизации до оформления заказа.
    """

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """
        Фикстура для настройки и очистки теста.
        """
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

        yield

        self.driver.quit()

    @allure.title("Полный цикл покупки: авторизация, добавление товаров, оформление заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("e2e", "regression", "purchase")
    def test_complete_purchase_flow(self):
        """
        Тест полного цикла покупки в интернет-магазине SauceDemo.

        Шаги:
        1. Авторизация стандартного пользователя
        2. Добавление трех товаров в корзину
        3. Переход в корзину и проверка содержимого
        4. Оформление заказа с заполнением данных
        5. Проверка итоговой суммы
        6. Завершение покупки
        """
        with allure.step("1. Инициализация драйвера и открытие сайта"):
            allure.attach(
                f"🚀 Начало теста полного цикла покупки\n"
                f"Браузер: Edge\n"
                f"URL: https://www.saucedemo.com/",
                name="Начало теста",
                attachment_type=allure.attachment_type.TEXT
            )

        try:
            # Шаг 1: Авторизация
            with allure.step("2. Авторизация пользователя standard_user"):
                login_page = LoginPage(self.driver).open()
                main_page = login_page.login("standard_user", "secret_sauce")

                allure.attach(
                    "✅ Авторизация прошла успешно",
                    name="Результат авторизации",
                    attachment_type=allure.attachment_type.TEXT
                )

            # Шаг 2: Проверка отображения товаров
            with allure.step("3. Проверка отображения товаров на главной странице"):
                products_displayed = main_page.verify_products_displayed()
                assert products_displayed, "Не все товары отображаются на странице"

            # Шаг 3: Добавление товаров в корзину
            with allure.step("4. Добавление товаров в корзину"):
                main_page \
                    .add_backpack_to_cart() \
                    .add_t_shirt_to_cart() \
                    .add_onesie_to_cart()

                # Проверка счетчика корзины
                cart_count = main_page.get_cart_items_count()
                assert cart_count == "3", f"В корзине должно быть 3 товара, а есть {cart_count}"

                allure.attach(
                    f"✅ Добавлено 3 товара в корзину\n"
                    f"Счетчик корзины: {cart_count}",
                    name="Результат добавления",
                    attachment_type=allure.attachment_type.TEXT
                )

            # Шаг 4: Переход в корзину
            with allure.step("5. Переход в корзину покупок"):
                cart_page = main_page.go_to_cart()

                # Проверка содержимого корзины
                cart_items = cart_page.get_cart_items()
                assert len(cart_items) == 3, f"В корзине должно быть 3 товара, а есть {len(cart_items)}"

                allure.attach(
                    f"✅ Корзина содержит {len(cart_items)} товаров",
                    name="Содержимое корзины",
                    attachment_type=allure.attachment_type.TEXT
                )

            # Шаг 5: Оформление заказа
            with allure.step("6. Начало оформления заказа"):
                checkout_page = cart_page.click_checkout()

            with allure.step("7. Заполнение данных для доставки"):
                checkout_page \
                    .fill_shipping_info("Vladimir", "Orlov", "454131") \
                    .click_continue()

                allure.attach(
                    "✅ Данные для доставки заполнены",
                    name="Данные клиента",
                    attachment_type=allure.attachment_type.TEXT
                )

            # Шаг 6: Проверка итоговой суммы
            with allure.step("8. Проверка итоговой суммы заказа"):
                total_price = checkout_page.get_total_price()
                expected_price = "Total: $58.29"

                allure.attach(
                    f"💰 Сумма заказа:\n"
                    f"Ожидаемая: {expected_price}\n"
                    f"Фактическая: {total_price}",
                    name="Сравнение сумм",
                    attachment_type=allure.attachment_type.TEXT
                )

                assert total_price == expected_price, \
                    f"Ожидалась сумма {expected_price}, получена {total_price}"

            # Шаг 7: Завершение покупки
            with allure.step("9. Завершение оформления заказа"):
                checkout_page.finish_checkout()

                # Проверка сообщения об успехе
                success_message = checkout_page.verify_success_message()
                assert "THANK YOU FOR YOUR ORDER" in success_message.upper(), \
                    f"Неверное сообщение об успехе: {success_message}"

                allure.attach(
                    f"✅ Заказ успешно оформлен!\n"
                    f"Сообщение: {success_message}\n"
                    f"Итоговая сумма: {total_price}",
                    name="Итог теста",
                    attachment_type=allure.attachment_type.TEXT
                )

            with allure.step("10. Тест завершен успешно"):
                allure.attach(
                    "🎉 Все шаги теста выполнены успешно!\n"
                    "✅ Авторизация\n"
                    "✅ Добавление товаров\n"
                    "✅ Оформление заказа\n"
                    "✅ Проверка суммы",
                    name="Финальный результат",
                    attachment_type=allure.attachment_type.TEXT
                )

        except Exception as e:
            # В случае ошибки делаем скриншот и логируем
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Ошибка в тесте",
                attachment_type=allure.attachment_type.PNG
            )

            allure.attach(
                f"❌ Тест завершился с ошибкой:\n"
                f"Ошибка: {str(e)}\n"
                f"URL: {self.driver.current_url}\n"
                f"Заголовок: {self.driver.title}",
                name="Детали ошибки",
                attachment_type=allure.attachment_type.TEXT
            )

            raise

    @allure.title("Негативный тест: авторизация с неверными данными")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("negative", "auth")
    def test_invalid_login(self):
        """
        Тест авторизации с неверными учетными данными.
        Ожидается сообщение об ошибке.
        """
        with allure.step("Попытка авторизации с неверными данными"):
            login_page = LoginPage(self.driver).open()
            login_page.enter_username("invalid_user")
            login_page.enter_password("wrong_password")
            login_page.click_login()

            error_message = login_page.get_error_message()

            allure.attach(
                f"🔐 Результат негативного теста авторизации:\n"
                f"Логин: invalid_user\n"
                f"Ожидается: Сообщение об ошибке\n"
                f"Получено: {error_message if error_message else 'Нет сообщения'}",
                name="Негативная авторизация",
                attachment_type=allure.attachment_type.TEXT
            )

            assert error_message, "Ожидалось сообщение об ошибке при неверной авторизации"