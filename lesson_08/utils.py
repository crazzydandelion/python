import json
from typing import Dict, Any, Optional


def validate_response_schema(response_data: Dict[str, Any], required_fields: list) -> bool:
    """
    Проверяет, что ответ содержит обязательные поля.
    """
    if not isinstance(response_data, dict):
        return False

    return all(field in response_data for field in required_fields)


def get_error_message(response) -> str:
    """
    Извлекает сообщение об ошибке из ответа.
    """
    try:
        error_data = response.json()
        return error_data.get("message", str(error_data))
    except:
        return response.text