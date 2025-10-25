import re

from utils.logger_config import reg_logger

STRICT_EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


def is_valid_email(email: str) -> bool:
    """Проверяет валидность email адреса"""
    return bool(re.match(STRICT_EMAIL_PATTERN, email))
