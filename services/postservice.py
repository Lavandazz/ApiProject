from database.models_db import Article, User
from utils.logger_config import db_logger


class ArticleService:
    @staticmethod
    async def get_articles():
        try:
            articles = await Article.all()
            return articles
        except Exception as e:
            db_logger.error(f"Ошибка получения всех постов: {e}")

    @staticmethod
    async def get_article_by_user_id(author: User):
        try:
            articles = await Article.filter(author=author).all()
            if not articles:
                return None
            return articles
        except Exception as e:
            db_logger.error(f"Ошибка получения всех постов пользователя: {e}")

    @staticmethod
    async def get_article_by_id(article_id: int):
        """Получение поста по ID"""
        try:
            article = await Article.get_or_none(id=article_id)
            return article
        except Exception as e:
            db_logger.error(f"Ошибка получения поста {article_id}: {e}")

    @staticmethod
    async def add_article(title: str, description: str, author: User):
        """
        Добавление поста
        :return:
        """
        try:
            article = await Article.create(title=title,
                                           description=description,
                                           author=author)
            return article
        except Exception as e:
            db_logger.error(f"Ошибка сохранения поста: {e}")

    @staticmethod
    async def update_post(article_id: int, **kwargs):
        """
        Редактирование поста. Передаем id поста и поля, которые необходимо редактировать
        # :param article_id:
        # :param title:
        # :param description:
        :return:
        """
        try:
            article = await Article.get_or_none(id=article_id)

            # Сохраняем переданные значения
            for key, value in kwargs.items():
                if value is not None and hasattr(article, key):
                    setattr(article, key, value)

            await article.save()
            return article

        except Exception as e:
            db_logger.error(f"Ошибка изменения поста: {e}")

    @staticmethod
    async def delete_article(article_id: int):
        try:
            article = await Article.get_or_none(id=article_id)
            await article.delete()
            return True

        except Exception as e:
            db_logger.error(f"Ошибка удаления поста: {e}")
            return False
