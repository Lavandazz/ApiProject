from database.models_db import User, Role, UserRole
from utils.logger_config import db_logger


class UserService:
    @staticmethod
    async def create_user(username, name, surname, patronymic, email, password, role_name="user") -> User | None:
        try:
            user = await User.create(
                username=username,
                name=name,
                surname=surname,
                patronymic=patronymic,
                email=email,
                password=password
            )
            # создаем роль если не существует
            role = await Role.get_or_none(role=role_name)

            if not role:
                role = await Role.create(role=role_name)

            # Связываем пользователя с ролью
            await UserRole.create(user=user, role=role)
            if user:
                return user

        except Exception as e:
            db_logger.error(f"Ошибка при регистрации нового пользователя: {e}")

    @staticmethod
    async def get_user(email: str) -> User | None:
        """
        Проверяем есть ли юзер в базе по уникальному полю email
        :param email:
        :return:
        """
        try:
            if email:
                user = await User.get_or_none(email=email)
                if user:
                    return user

        except Exception as e:
            db_logger.error(f"Пользователя нет в базе {e}")

    @staticmethod
    async def get_username(username: str) -> User | None:
        """
        Проверяем есть ли юзер в базе по уникальному полю username

        """
        try:
            if username:
                user = await User.get_or_none(username=username)
                if user:
                    return user

        except Exception as e:
            db_logger.error(f"Пользователя нет в базе {e}")

    @staticmethod
    async def get_role_user(email: str) -> Role:
        """
        Отображение роли пользователя
        :param email:
        :return: role: объект модели Role
        """
        try:
            user = await User.get_or_none(email=email)
            if user:
                user_role = await UserRole.filter(user=user).prefetch_related('role').first()
                return user_role.role

        except Exception as e:
            db_logger.error(f"Не удалось получить роль пользователя {e}")

    @staticmethod
    async def delete_user(email):
        """
        Мягкое удаление. Помечает пользователя как неактивный
        :param email:
        :return:
        """
        try:
            await User.filter(email=email).update(is_active=False)

        except Exception as e:
            db_logger.error(f"Неудачная попытка удалить аккаунт: {email}. {e}")
