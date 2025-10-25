from database.models_db import BlacklistedToken
from utils.logger_config import db_logger


class TokenService:

    @staticmethod
    async def blacklist_token_saver(token: str):
        """
        Сохраняет токен в черный список
        :param token:
        :return:
        """
        try:
            db_logger.info(f"token = {token}, type = {type(token)}")
            await BlacklistedToken.create(token=token)
        except Exception as e:
            db_logger.exception(f"не удалось сохранить токен в бд: {e}")

    @staticmethod
    async def is_token_black(token: str) -> bool:
        """
        Проверяет токен в бд
        :param token:
        :return: true/false
        """
        try:
            return await BlacklistedToken.filter(token=token).exists()
        except Exception as e:
            db_logger.exception(f"Ошибка проверки токена: {e}")
