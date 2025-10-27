from database.models_db import Role
from utils.logger_config import db_logger


async def create_initial_roles():
    """Создает базовые роли при старте приложения"""
    initial_roles = ["user", "admin"]
    cnt = 0
    try:
        for role_name in initial_roles:
            role, created = await Role.get_or_create(role=role_name)
            if created:
                cnt += 1
        if cnt == 2:
            db_logger.info(f"Роли: {initial_roles} добавлены")
    except Exception as e:
        db_logger.error(f"Ошибка при добалении ролей {initial_roles} в базу: {e}")