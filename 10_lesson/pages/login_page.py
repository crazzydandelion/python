import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


@allure.epic("SauceDemo Web Application")
@allure.feature("Authentication")
@allure.story("Страница авторизации")
class LoginPage(BasePage):
    """
    Page Object для страницы авторизации SauceDemo.
    Содержит методы для работы с формой логина.
    """

    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    @allure.step("Открытие страницы авторизации")
    def open(self):
        """
        Открывает страницу авторизации.

        Returns:
            LoginPage: Текущий экземпляр страницы
        """
        self.driver.get("https://www.saucedemo.com/")
        allure.attach(
            f"🌐 Открыта страница авторизации\nURL: https://www.saucedemo.com/",
            name="Открытие страницы",
            attachment_type=allure.attachment_type.TEXT
        )
        self._attach_screenshot("login_page_opened")
        return self

    @allure.step("Ввод логина: {username}")
    def enter_username(self, username):
        """
        Вводит логин пользователя.

        Args:
            username: Логин пользователя
        """
        self.send_keys(self.USERNAME_INPUT, username)
        return self

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        """
        Вводит пароль пользователя.

        Args:
            password: Пароль пользователя
        """
        self.send_keys(self.PASSWORD_INPUT, password)
        return self

    @allure.step("Клик по кнопке Login")
    def click_login(self):
        """Кликает по кнопке входа."""
        self.click(self.LOGIN_BUTTON)
        self._attach_screenshot("after_login_click")

    @allure.step("Полная процедура авторизации")
    def login(self, username, password):
        """
        Выполняет полную процедуру авторизации.

        Args:
            username: Логин пользователя
            password: Пароль пользователя

        Returns:
            MainPage: Страница после успешной авторизации
        """
        with allure.step("Заполнение формы авторизации"):
            allure.attach(
                f"🔐 Данные для авторизации:\n"
                f"Логин: {username}\n"
                f"Пароль: {'*' * len(password)}",
                name="Учетные данные",
                attachment_type=allure.attachment_type.TEXT
            )

            self.enter_username(username)
            self.enter_password(password)
            self.click_login()

        # Проверяем успешность авторизации
        from .main_page import MainPage
        try:
            # Проверяем, что мы на главной странице
            if "inventory" in self.driver.current_url:
                allure.attach(
                    f"✅ Авторизация успешна\n"
                    f"Пользователь: {username}\n"
                    f"Перенаправлен на: {self.driver.current_url}",
                    name="Результат авторизации",
                    attachment_type=allure.attachment_type.TEXT
                )
                return MainPage(self.driver)
            else:
                # Проверяем наличие ошибки
                error_element = self.find_element(self.ERROR_MESSAGE, timeout=2)
                error_text = error_element.text
                allure.attach(
                    f"❌ Ошибка авторизации: {error_text}",
                    name="Ошибка авторизации",
                    attachment_type=allure.attachment_type.TEXT
                )
                raise Exception(f"Авторизация не удалась: {error_text}")

        except TimeoutException:
            # Если нет ошибки и мы не на главной - что-то пошло не так
            self._attach_screenshot("auth_unknown_state")
            raise Exception("Неизвестное состояние после авторизации")

    @allure.step("Получение сообщения об ошибке")
    def get_error_message(self):
        """
        Получает текст сообщения об ошибке.

        Returns:
            str: Текст ошибки или пустая строка
        """
        try:
            error_element = self.find_element(self.ERROR_MESSAGE, timeout=2)
            error_text = error_element.text
            allure.attach(
                f"⚠️ Сообщение об ошибке: {error_text}",
                name="Текст ошибки",
                attachment_type=allure.attachment_type.TEXT
            )
            return error_text
        except:
            return ""