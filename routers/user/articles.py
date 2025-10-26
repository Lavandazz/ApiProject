from fastapi import Depends, Form, HTTPException, APIRouter
from database.models_db import User
from models.schemas import ArticleUpdateSchema
from routers.verification import get_current_user
from services.postservice import ArticleService
from services.userservice import UserService
from utils.logger_config import post_logger
from utils.permissions import get_role_permissions

router = APIRouter()


@router.get("/articles", tags=["articles"])
async def get_articles():
    """
    Открытое отображение всех постов пользователей
    """
    # Получаем данные из токена
    articles = await ArticleService.get_articles()
    if not articles:
        raise HTTPException(status_code=404, detail="Нет данных")

    return {"articles": articles}


@router.get("/user/articles", tags=["articles"])
async def get_articles_by_user(user: User = Depends(get_current_user)):
    """
    Фильтрация постов пользователя.
    Доступна только автору.
    """
    # Получаем автора из токена
    articles = await ArticleService.get_article_by_user_id(author=user)
    msg = "Посты пользователя:" if articles else "Постов еще нет"
    return {"message": msg, "articles": articles}


@router.post("/create_article", tags=["articles"])
async def create_article(title: str = Form(...),
                         description: str = Form(...),
                         user: User = Depends(get_current_user)):
    """
    Добавление поста
    """
    article = await ArticleService.add_article(title=title,
                                               description=description,
                                               author=user)
    post_logger.info(f"Пользователь {user.name} создал пост {article.title}")
    return {"message": "Пост создан"}


@router.put("/article/{article_id}", tags=["articles"])
async def update_article(article_id: int,
                         update_data: ArticleUpdateSchema,
                         user: User = Depends(get_current_user)):
    """
    Редактирование поста.
    Для редактирования необходимо передать id поста. Редактировать может автор или админ.
    """
    # проверяем наличие поста и прав
    await get_role_permissions(article_id, user)

    update_dict = update_data.model_dump()  # преобразуем в словарь
    update_article_data = await ArticleService.update_post(article_id=article_id,
                                                           **update_dict)

    post_logger.info(f"Пользователь {user.name} отредактировал пост {update_data}")
    return {"message": "Данные сохранены", "update_article": update_article_data}


@router.delete("/article/{article_id}", tags=["articles"])
async def delete_article(article_id: int,
                         user: User = Depends(get_current_user)):
    """
    Удаление поста.
    Удалить пост может пользователь или админ
    """
    # проверяем наличие поста и прав
    await get_role_permissions(article_id, user)

    result = await ArticleService.delete_article(article_id=article_id)
    if result:
        return {"message": "Пост удален"}
    else:
        raise HTTPException(status_code=500, detail="Не удалось удалить пост")
