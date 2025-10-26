from fastapi import HTTPException

from database.models_db import User
from services.postservice import ArticleService
from services.userservice import UserService

ROLE_PERMISSIONS = {
    "admin": ["article:read", "article:write", "user:delete", "user:unblock", "user:assign_roles", "user:view_users"],
    "user": ["article:read", "article:write", "user:delete", "user:read"]
}


async def get_role_permissions(article_id: int, user: User):
    """
    Проверка наличия поста и прав для изменения
    :param article_id:
    :param user:
    :return:
    """
    article = await ArticleService.get_article_by_id(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Пост не найден")

    user_role = await UserService.get_role_user(user.email)

    if article.author != user.id and user_role.role != "admin":
        raise HTTPException(status_code=403, detail="Недостаточно прав")

    return article
