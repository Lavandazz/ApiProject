from typing import Optional

from fastapi import Depends, Form, HTTPException, APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from database.models_db import User
from models.schemas import UserUpdateSchema, UserProfileSchema, UserResponseSchema
from routers.verification import get_current_user
from services.token_service import TokenService
from services.userservice import UserService
from utils.auth import verify_password
from utils.logger_config import profile_logger

router = APIRouter()


@router.get("/user/profile", tags=["profile"])
async def get_profile(user: User = Depends(get_current_user)):
    """
    Отображение данных пользователя
    :param user: данные берутся из data токена
    :return:
    """
    # Получаем данные из токена
    user_role = await UserService.get_role_user(email=user.email)
    return {"username": user.username,
            "name": user.name,
            "surname": user.surname,
            "patronymic": user.patronymic,
            "email": user.email,
            "role": user_role}


@router.put("/user/profile", tags=["profile"], response_model=UserResponseSchema)
async def update_profile(update_data: UserUpdateSchema,
                         password: str,
                         user: User = Depends(get_current_user)):
    """
    Изменение данных в профиле
    """
    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Неверный пароль")

    # преобразуем в словарь
    update_dict = update_data.model_dump()
    # проходимся по данным
    for key, value in update_dict.items():
        if value not in ("string", None):
            setattr(user, key, value)

    await user.save()
    profile_logger.info(f"Данные в лк обновлены")

    return {"message": "Данные сохранены",
            "user": user}


@router.delete("/user/profile", tags=["profile"])
async def delete_profile(password: str,
                         user: User = Depends(get_current_user),
                         credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Неверный пароль")

    await UserService.delete_user(email=user.email)

    # Удаляем сессию и добавляем токен в черный лист
    token = credentials.credentials
    await TokenService.blacklist_token_saver(token=token)

    return {"message": "Аккаунт удалён"}
