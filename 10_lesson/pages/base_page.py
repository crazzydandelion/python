import allure
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


@allure.epic("SauceDemo Web Application")
@allure.feature("Base Page Object")
@allure.story("Базовый класс для всех страниц")
class BasePage:
    """
    Базовый класс Page Object Model для SauceDemo.
    Предоставляет общие методы для работы с веб-элементами.
    Все методы содержат Allure-шаги для подробной отчетности.
    """

    def __init__(self, driver):
        """
        Инициализация базовой страницы.

        Args:
            driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Логируем создание страницы
        with allure.step(f"Инициализация страницы: {self.__class__.__name__}"):
            allure.attach(
                f"Класс страницы: {self.__class__.__name__}\n"
                f"Текущий URL: {driver.current_url}\n"
                f"Заголовок страницы: {driver.title}",
                name="Информация о странице",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.step("Поиск элемента: {locator}")
    def find_element(self, locator, timeout=10):
        """
        Находит элемент с ожиданием.

        Args:
            locator: Кортеж (By, значение)
            timeout: Время ожидания в секундах

        Returns:
            WebElement: Найденный элемент
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(
                EC.presence_of_element_located(locator),
                message=f"Элемент {locator} не найден за {timeout} секунд"
            )

            # Логируем успешный поиск
            element_info = self._get_element_info(element)
            allure.attach(
                element_info,
                name=f"Найден элемент: {locator[1]}",
                attachment_type=allure.attachment_type.TEXT
            )

            return element

        except TimeoutException as e:
            self._attach_screenshot(f"Ошибка поиска элемента {locator[1]}")
            allure.attach(
                f"❌ Не удалось найти элемент\n"
                f"Локатор: {locator}\n"
                f"URL: {self.driver.current_url}\n"
                f"Ошибка: {str(e)}",
                name="Детали ошибки",
                attachment_type=allure.attachment_type.TEXT
            )
            raise

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        """
        Кликает по элементу.

        Args:
            locator: Кортеж (By, значение)
        """
        try:
            element = self.wait.until(
                EC.element_to_be_clickable(locator),
                message=f"Элемент {locator} не кликабелен"
            )

            # Логируем перед кликом
            allure.attach(
                f"🖱️ Выполнение клика\n"
                f"Локатор: {locator[1]}\n"
                f"Текст элемента: {element.text[:50] if element.text else 'Без текста'}",
                name="Предкликовое состояние",
                attachment_type=allure.attachment_type.TEXT
            )

            url_before = self.driver.current_url
            element.click()

            # Логируем после клика
            allure.attach(
                f"✅ Клик выполнен\n"
                f"URL до клика: {url_before}\n"
                f"URL после клика: {self.driver.current_url}",
                name="Результат клика",
                attachment_type=allure.attachment_type.TEXT
            )

        except Exception as e:
            self._attach_screenshot(f"Ошибка клика {locator[1]}")
            raise

    @allure.step("Ввод текста '{text}' в элемент: {locator}")
    def send_keys(self, locator, text):
        """
        Вводит текст в элемент.

        Args:
            locator: Кортеж (By, значение)
            text: Текст для ввода
        """
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)

            # Верифицируем ввод
            entered_text = element.get_attribute("value") or ""
            allure.attach(
                f"✅ Текст введен\n"
                f"Ожидаемый текст: {text}\n"
                f"Фактический текст: {entered_text}\n"
                f"Длина: {len(text)} символов",
                name="Результат ввода",
                attachment_type=allure.attachment_type.TEXT
            )

        except Exception as e:
            self._attach_screenshot(f"Ошибка ввода текста {locator[1]}")
            raise

    @allure.step("Создание скриншота")
    def _attach_screenshot(self, name="screenshot"):
        """Создает и прикрепляет скриншот к отчету Allure."""
        try:
            screenshot = self.driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=name,
                attachment_type=allure.attachment_type.PNG
            )
        except:
            pass

    def _get_element_info(self, element):
        """Возвращает информацию об элементе."""
        try:
            info = f"""
            ✅ Информация об элементе:
            Текст: {element.text[:100] if element.text else 'Нет текста'}
            Тэг: {element.tag_name}
            Отображается: {element.is_displayed()}
            Активен: {element.is_enabled()}
            Размер: {element.size}
            """
            return info
        except:
            return "Информация об элементе недоступна"

    @allure.step("Ожидание {timeout} секунд")
    def wait_time(self, timeout):
        """Ожидание указанного времени."""
        time.sleep(timeout)
        allure.attach(
            f"⏳ Выполнено ожидание: {timeout} секунд",
            name="Таймаут",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        """Возвращает текущий URL."""
        url = self.driver.current_url
        allure.attach(
            f"🌐 Текущий URL: {url}",
            name="URL страницы",
            attachment_type=allure.attachment_type.TEXT
        )
        return url