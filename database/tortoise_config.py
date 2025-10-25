import os
from pathlib import Path

from dotenv import load_dotenv

# Загрузка .env
env_file = ".env"
load_dotenv(env_file)

# подключение к базе
DATABASE_URL = (
    f"postgres://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{int(os.getenv('POSTGRES_PORT'))}/"
    f"{os.getenv('POSTGRES_DB')}"
)

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["database.models_db", "aerich.models"],  # подключаем aerich.models миграции
            "default_connection": "default",
        },
    },
}


