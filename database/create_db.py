from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from dotenv import load_dotenv

from database.tortoise_config import TORTOISE_ORM
from utils.create_roles import create_initial_roles
from utils.logger_config import db_logger

load_dotenv()


def init_db(app: FastAPI):
    register_tortoise(
        app,
        config=TORTOISE_ORM,  # передаем конфиг
        modules={"models": ["database.models_db"]},
        add_exception_handlers=True,
    )


async def connect_db():
    await Tortoise.init(config=TORTOISE_ORM)
    db_logger.info(f'Подклчючился к базе')
    await Tortoise.generate_schemas()
    await create_initial_roles()


async def close_db():
    await Tortoise.close_connections()
