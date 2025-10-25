from fastapi import HTTPException, Form, Depends, APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from database.models_db import User
from routers.verification import get_current_user
from services.token_service import TokenService
from services.userservice import UserService
from utils.auth import verify_password, create_tokens, hash_password
from utils.logger_config import reg_logger
from utils.permissions import ROLE_PERMISSIONS
from utils.valid_email import is_valid_email

router = APIRouter()


@router.post("/register", tags=["auth"])
async def register_user(
        username: str = Form(...),
        name: str = Form(...),
        surname: str = Form(...),
        patronymic: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        second_password: str = Form(...)):
    """Регистрация пользователя"""

    if not is_valid_email(email):
        raise HTTPException(status_code=400, detail="Проверьте email")

    if password != second_password:
        raise HTTPException(status_code=400, detail="Пароли не совпадают")

    user = await UserService.get_user(email)
    if user:
        raise HTTPException(status_code=400, detail="Пользователь с таким именем уже существует")

    else:
        hashed_password = hash_password(password)  # хешируем пароль

        # Сохраняем в бд
        await UserService.create_user(
            username=username, name=name, surname=surname, patronymic=patronymic, email=email, password=hashed_password
        )

        return {"message": "Пользователь зарегистрирован"}


@router.post("/login", tags=["auth"])
async def login(
        email: str = Form(...),
        password: str = Form(...)):
    """Авторизация пользователя.
    Проверяем заполнение всех полей, правильность пароля, активен ли аккаунт"""

    if not email or not password:
        raise HTTPException(status_code=400, detail="Заполните все поля")

    user = await UserService.get_user(email=email)

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Неверно введены логин или пароль")

    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="Аккаунт неактивен. Обратитесь в поддержку"
        )
    # Получаем роль пользователя
    user_role = await UserService.get_role_user(email=email)
    user_permissions = ROLE_PERMISSIONS.get(user_role, [])

    # Создаем токен
    tokens = create_tokens(user_id=user.id, email=email, permissions=user_permissions)

    return {
        "access_token": tokens["main_token"],
        "token_type": "bearer",
        "role": user_role,
        "permissions": user_permissions
    }


@router.post("/logout", tags=["auth"])
async def logout(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
                 user: User = Depends(get_current_user)):
    """Выход из системы - инвалидация токена"""
    token = credentials.credentials
    # добавляем токен в блеклист
    await TokenService.blacklist_token_saver(token=token)

    return {"message": "Успешный выход из системы"}
