from datetime import datetime
from tortoise import fields
from tortoise.models import Model


class User(Model):
    """
    Модель пользователя
    """
    id: int = fields.IntField(pk=True)
    username: str = fields.CharField(max_length=50, unique=True)
    name: str = fields.CharField(max_length=50)
    surname: str = fields.CharField(max_length=70)
    patronymic: str = fields.CharField(max_length=70)
    email: str = fields.CharField(max_length=25, unique=True)
    password: str = fields.CharField(max_length=100)
    is_active: str = fields.BooleanField(default=True)

    def __str__(self):
        return self.username


class Role(Model):
    """
    Модель роли (Админ, Пользователь)
    """
    id = fields.IntField(pk=True)
    role = fields.CharField(max_length=100, unique=True)  # "admin", "user"

    def __str__(self):
        return self.role


class UserRole(Model):
    """
    Связь пользователя и роли
    """
    user = fields.ForeignKeyField('models.User', related_name='roles')
    role = fields.ForeignKeyField('models.Role', related_name='users')


class Article(Model):
    id: int = fields.IntField(pk=True)
    title: str = fields.CharField(max_length=150)
    description: str = fields.TextField()
    created_at: datetime = fields.DatetimeField(auto_now_add=True)

    def __repr__(self):
        return f'{self.title} created {self.created_at}'


class BlacklistedToken(Model):
    """
    Модель для сохранения токена в черный лист токенов для дальнейшей проверки валидности токенов при входе
    """
    id: int = fields.IntField(pk=True)
    token: str = fields.TextField(max_length=600)
