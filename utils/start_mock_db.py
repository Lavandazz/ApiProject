import asyncio
import random

from database.mock_base import MOCK_USERS, MOCK_ARTICLES
from database.models_db import Article, User, UserRole, Role
from utils.auth import hash_password
from utils.logger_config import db_logger

list_users = [user.get("username") for user in MOCK_USERS]
USERS = dict(enumerate(list_users, 1))


async def save_admin():
    """
    Регистрация админа
    """
    try:
        hashed_password = hash_password("judgment_day")

        if await User.get_or_none(username="skynet_admin"):
            return

        user = await User.create(
            username="skynet_admin",
            name="Скайнет",
            surname="Система",
            patronymic="Админович",
            email="admin@skynet.com",
            password=hashed_password
        )
        role, created = await Role.get_or_create(role="admin")
        await UserRole.create(user=user, role=role)
        db_logger.info(f"Админ создан")
        return user

    except Exception as e:
        db_logger.error(e)


async def register_mock_users():
    """
    Регистрация мок юзеров
    """
    async def create_user(user_data: dict, role: str):
        user = await User.create(
            username=user_data["username"],
            name=user_data["name"],
            surname=user_data["surname"],
            patronymic=user_data["patronymic"],
            email=user_data["email"],
            password=hash_password(user_data["password"]),
            is_active=user_data.get("is_active", True)
        )
        role, created = await Role.get_or_create(role=role)

        await UserRole.create(user=user, role=role)
        db_logger.info(f"Пользователь {user_data['username']} создан")

        return user

        # Создаем задачи для регистрации всех пользователей
    tasks = []
    for user_data in MOCK_USERS:
        user_in_db = await User.get_or_none(username=user_data.get("username"))
        if not user_in_db:
            tasks.append(create_user(user_data, "user"))

    results = await asyncio.gather(*tasks)
    created_users = [user for user in results if user is not None]
    db_logger.info(f"Создано {len(created_users)}")
    return created_users


async def create_mock_post():
    """
    Создание мок базы постов
    """
    users = await User.all()
    for article in MOCK_ARTICLES:
        post = await Article.get_or_none(title=article.get("title"))
        if not post:
            await Article.create(title=article.get("title"),
                                 description=article.get("description"),
                                 author=random.choice(users))


async def create_mock_base():
    """
    Создание мок базы.
    Если админ создан, то база существует.
    """

    await save_admin()
    await register_mock_users()
    await create_mock_post()



