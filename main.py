from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.create_db import connect_db, close_db, init_db
from routers import index_page, login_router, user
from routers.admin import admin
from routers.user import profile, articles


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Код для старта приложения
    await connect_db()
    yield  # Приложение работает
    # Код для завершения работы приложения
    await close_db()

app = FastAPI(lifespan=lifespan)
init_db(app)
app.include_router(index_page.router)
app.include_router(login_router.router)
app.include_router(profile.router)
app.include_router(admin.router)
app.include_router(articles.router)


