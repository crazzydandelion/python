import pytest
from selenium import webdriver
from pages.login_page import LoginPage


def test_complete_purchase():
    # Инициализация драйвера Firefox
    driver = webdriver.Edge()

    try:
        # Шаг 1: Авторизация
        login_page = LoginPage(driver).open()
        main_page = login_page.login("standard_user", "secret_sauce")

        # Шаг 2: Добавление товаров в корзину
        main_page \
            .add_backpack_to_cart() \
            .add_t_shirt_to_cart() \
            .add_onesie_to_cart()

        # Проверка количества товаров в корзине
        assert main_page.get_cart_items_count() == "3"

        # Шаг 3: Переход в корзину
        cart_page = main_page.go_to_cart()

        # Проверка количества товаров на странице корзины
        assert cart_page.get_cart_items_count() == 3

        # Шаг 4: Оформление заказа
        checkout_page = cart_page.click_checkout()

        # Шаг 5: Заполнение данных
        checkout_page \
            .fill_shipping_info("Vladimir", "Orlov", "454131") \
            .click_continue()

        # Шаг 6: Проверка итоговой суммы
        total_price = checkout_page.get_total_price()
        assert total_price == "Total: $58.29", f"Expected 'Total: $58.29', but got '{total_price}'"

        print(f"Тест пройден успешно! Итоговая сумма: {total_price}")

    finally:
        # Закрытие браузера
        driver.quit()
