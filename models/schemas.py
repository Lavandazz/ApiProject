from typing import Optional

from pydantic import BaseModel
# from tortoise.contrib.pydantic import pydantic_model_creator


class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    patronymic: Optional[str] = None


class UserProfileSchema(BaseModel):
    username: str
    name: str
    surname: str
    patronymic: str
    email: str


class UserResponseSchema(BaseModel):
    """
    Модель для возврата объекта user и сообщения после редактирования профиля
    """
    message: str
    user: UserProfileSchema


class ArticleUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
