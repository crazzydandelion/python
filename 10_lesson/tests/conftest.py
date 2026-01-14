import pytest
import allure


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для прикрепления скриншотов при падении теста.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            for fixture_name in item.fixturenames:
                if "driver" in fixture_name:
                    driver = item.funcargs[fixture_name]
                    if hasattr(driver, "get_screenshot_as_png"):
                        allure.attach(
                            driver.get_screenshot_as_png(),
                            name="Screenshot on failure",
                            attachment_type=allure.attachment_type.PNG
                        )
                    break
        except:
            pass  # Игнорируем ошибки при создании скриншотов


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для создания WebDriver.
    """
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver

    driver.quit()