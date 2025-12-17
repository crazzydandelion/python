import os
import pytest
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Базовые настройки
BASE_URL = "https://ru.yougile.com/api-v2"


@pytest.fixture(scope="session")
def auth_token():
    """
    Фикстура для получения токена авторизации.
    Использует данные из переменных окружения.
    """
    login = os.getenv("YOUGILE_LOGIN")
    password = os.getenv("YOUGILE_PASSWORD")
    company_id = os.getenv("YOUGILE_COMPANY_ID")

    # Проверяем наличие необходимых данных
    if not all([login, password, company_id]):
        pytest.skip("Не заданы учетные данные в .env файле")

    creds = {
        'login': login,
        'password': password,
        'companyId': company_id
    }

    try:
        response = requests.post(f"{BASE_URL}/auth/keys", json=creds, timeout=10)
        response.raise_for_status()

        token_data = response.json()
        token = token_data.get("key")

        if not token:
            pytest.fail(f"Токен не найден в ответе. Ответ: {token_data}")

        print(f"✓ Токен получен (первые 10 символов): {token[:10]}...")
        return token

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Ошибка при получении токена: {e}")


@pytest.fixture(scope="session")
def api_headers(auth_token):
    """
    Фикстура для заголовков запросов с Bearer токеном.
    """
    return {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


@pytest.fixture
def cleanup_project_ids():
    """
    Фикстура для сбора ID проектов для последующей очистки.
    """
    project_ids = []
    yield project_ids

    # Очистка после всех тестов (опционально, можно закомментировать)
    # Для тестов, где нужна стабильность, лучше не чистить
    # print(f"\nОчистка {len(project_ids)} тестовых проектов...")
    # for project_id in project_ids:
    #     try:
    #         requests.delete(f"{BASE_URL}/projects/{project_id}", headers=api_headers)
    #     except:
    #         pass


@pytest.fixture
def unique_project_title():
    """
    Генерирует уникальное название проекта для каждого теста.
    """
    import uuid
    return f"Test Project {uuid.uuid4().hex[:8]}"