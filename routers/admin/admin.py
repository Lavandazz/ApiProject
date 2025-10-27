from fastapi import Depends, Form, APIRouter

from database.models_db import User
from routers.verification import require_admin
from services.adminservice import AdminService
from utils.logger_config import admin_logger

router = APIRouter()


@router.get("/admin/users", tags=["admin"])
async def get_all_users(current_user: User = Depends(require_admin)):
    """
    Получение списка всех пользователей (только для админов)
    """
    users = await AdminService.get_all_users()
    admin_logger.info(f"{current_user.username} запросил данные о пользователях")
    return {"users": users}


@router.put("/admin/users/{user_id}/role", tags=["admin"])
async def change_user_role(
    user_id: int,
    role: str = Form(...),
    current_user: User = Depends(require_admin)
):
    """Изменить роль пользователя"""
    updated_user = await AdminService.change_user_role_by_id(user_id, role)
    admin_logger.info(f"{current_user.username} изменил роль пользователя {updated_user.email} на {role}")
    return {"message": f"Роль изменена на {role}", "user": updated_user}


@router.put("/admin/users/{user_id}/activate", tags=["admin"])
async def activate_user(
    user_id: int,
    current_user: User = Depends(require_admin)
):
    """Активация/восстановление пользователя по ID"""
    user = await AdminService.activate_user_by_id(user_id)
    admin_logger.info(f"{current_user.username} изменил восстановил пользователя {user.email}")
    return {"message": "Пользователь активирован", "user": user}
