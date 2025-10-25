from datetime import timedelta, datetime, timezone
import jwt
import os
import bcrypt
from fastapi import HTTPException

from services.token_service import TokenService
from utils.logger_config import reg_logger

secret_key = os.getenv("SECRET_KEY")
refresh_secret_key = os.getenv("REFRESH_SECRET_KEY")
algorithm = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def hash_password(password: str):
    """
    Хэш пароля перед сохранением в БД
    """
    user_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    reg_logger.info(f"хэширую пароль: {user_pass.decode('utf-8')}")
    return user_pass.decode('utf-8')  # Преобразуем хеш в строку для хранения в бд


def verify_password(plain_password, hashed_password):
    """
    Проверка пароля с бд (хэш)
    :param plain_password:
    :param hashed_password:
    :return:
    """
    print(f'Проверка хэша пароля {plain_password.encode()}, {hashed_password.encode()}')
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())


def create_all_token(data: dict, secret_key: str):
    """
    Создание JSON Web Token
    """
    data_to_encode = data.copy()
    live_time = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data_to_encode.update({"exp": live_time})  # Добавляем в словарь время жизни токена
    encoded = jwt.encode(data_to_encode, secret_key, algorithm=algorithm)  # Кодируем токен

    return encoded


def create_tokens(user_id: int, email: str, permissions: list):
    """
    Создание основного токена и рефреш
    """
    main_token = create_all_token({
        "user_id": user_id,
        "email": email,
        "permissions": permissions
    }, secret_key)

    refresh_token = create_all_token({
        "user_id": user_id,
        "email": email
    }, refresh_secret_key)

    return {"main_token": main_token, "refresh_token": refresh_token}


async def verify_token(token: str):
    """
    Проверяем JWT-токен и извлекаем пользователя
    """
    # проверяем находится ли токен в черном списке
    if await TokenService.is_token_black(token=token):
        raise HTTPException(status_code=401, detail='Токен недействителен')

    try:
        decoded = jwt.decode(token, secret_key, algorithms=[algorithm])
        user_id = decoded.get('user_id')
        email = decoded.get('email')
        permissions = decoded.get('permissions', [])

        if email is None:
            raise HTTPException(status_code=401, detail='Неверный токен')

        # Возвращаем айди, email пользователя и его права
        return {
            "user_id": user_id,
            "email": email,
            "permissions": permissions
        }

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Токен истёк")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Неверный токен")

# from database.models_db import AdminModel
# async def create_admin():
#     admin = await AdminModel.create(admin='admin', password=hash_password("aprilia89"))
#     print("Админ зарегистрирован!")