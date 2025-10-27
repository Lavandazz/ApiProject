from database.models_db import Role, User, UserRole
from services.userservice import UserService
from utils.logger_config import db_logger


class AdminService(UserService):

    @staticmethod
    async def get_all_users():
        try:
            users = await User.all()

            return users

        except Exception as e:
            db_logger.error(f"Ошибка получения пользователей: {e}")

    @staticmethod
    async def change_user_role_by_id(user_id: int, new_role: str):
        """
        Смена роли пользователя.
        Можно назначить admin, user
        :param user_id:
        :param new_role:
        """
        try:
            role = await Role.get_or_none(role=new_role)
            user = await User.filter(id=user_id).first()

            user_role, created = await UserRole.update_or_create(
                user_id=user.id,
                defaults={'role_id': role.id}
            )
            action = "назначена" if created else "изменена на"
            db_logger.info(f"Пользователю {user.email} {action} роль {new_role}")

            return user

        except Exception as e:
            db_logger.error(e)

    @staticmethod
    async def activate_user_by_id(user_id: int):
        """Разблокировка пользователя"""
        try:
            user = await User.filter(id=user_id).first()
            db_logger.info(f"user: {user}")
            user.is_active = True

            await user.save()

            return user

        except Exception as e:
            db_logger.error(f"Не удалось разблокировать {user_id}: {e}")
