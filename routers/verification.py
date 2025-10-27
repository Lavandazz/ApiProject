from fastapi import Depends, HTTPException

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from database.models_db import User
from services.userservice import UserService
from utils.auth import verify_token
from utils.logger_config import admin_logger

security = HTTPBearer()


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Проверка токена"""
    # берем токен из заголовка
    token = credentials.credentials

    try:
        token_data = await verify_token(token)  # получаем данные из токена
        user_id = token_data["user_id"]

        user = await User.get_or_none(id=user_id)
        if user:
            return user

    except HTTPException:
        raise HTTPException(status_code=401, detail="Неверный токен")


async def require_admin(user: User = Depends(get_current_user)):
    """
    Проверяет права пользователя через данные из токена (user.email)
    :param user:
    :return:
    """
    # Получаем объект роли пользователя из БД
    user_role = await UserService.get_role_user(user.email)

    if user_role.role != "admin":
        raise HTTPException(status_code=403, detail="Требуются права администратора")

    admin_logger.info(f"Роль пользователя {user.email}: {user_role}")

    return user
