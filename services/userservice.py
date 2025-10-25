from database.models_db import User, Role, UserRole
from utils.logger_config import reg_logger, db_logger


class UserService:
    @staticmethod
    async def create_user(username, name, surname, patronymic, email, password, role_name="user"):
        try:
            db_logger.info(f"начинаю регистрацию {name, surname}")

            user = await User.create(
                username=username,
                name=name,
                surname=surname,
                patronymic=patronymic,
                email=email,
                password=password
            )
            db_logger.info(f"Новый пользователь зарегистрирован {user}")
            # создаем роль если не существует
            role = await Role.get_or_none(role=role_name)

            if not role:
                role = await Role.create(role=role_name)
                db_logger.info(f"Создана новая роль: {role_name}")

            db_logger.info(f"регистрирую пользователя с ролью: {role}")

            # Связываем пользователя с ролью
            await UserRole.create(user=user, role=role)

            db_logger.info(f"Пользователь {name} создан с ролью {role_name}")
            return user

        except Exception as e:
            db_logger.error(e)

    @staticmethod
    async def get_user(email) -> User | None:
        """
        Проверяем есть ли юзер в базе по полю email
        :param email:
        :return:
        """
        try:
            user = await User.get_or_none(email=email)
            if user:
                return user

        except Exception as e:
            reg_logger.error(f"Пользователя нет в базе {e}")

    @staticmethod
    async def get_role_user(email: str) -> str:
        """
        Возврат роли пользователя
        :param email:
        :return: role: str
        """
        try:
            user = await User.get_or_none(email=email)
            if user:
                user_role = await UserRole.filter(user=user).prefetch_related('role').first()
                return user_role.role

        except Exception as e:
            reg_logger.error(f"Не удалось получить роль пользователя {e}")

    @staticmethod
    async def delete_user(email):
        """
        Пометка на удаление
        :param email:
        :return:
        """
        try:
            await User.filter(email=email).update(is_active=False)
            db_logger.info(f"Пользователь {email} удалил аккаунт")
        except Exception as e:
            db_logger.error(f"Неудачная попытка удалить аккаунт: {email}. {e}")


class AdminService(UserService):
    @staticmethod
    async def change_role(email: str, new_role: str):
        role = await Role.get_or_none(role=new_role)
        user = await User.filter(email=email).first()

        user_role, created = await UserRole.update_or_create(
            user_id=user.id,
            defaults={'role_id': role.id}
        )
        action = "назначена" if created else "изменена на"
        db_logger.info(f"Пользователю {user.email} {action} роль {new_role}")

        return user

