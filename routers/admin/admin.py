from fastapi import Depends, Form, HTTPException, APIRouter

from database.models_db import User
from routers.verification import get_current_user, require_admin
from services.userservice import UserService, AdminService
from utils.auth import verify_password

router = APIRouter()


@router.get("/admin/users", tags=["admin"])
async def get_all_users(
    current_user: User = Depends(require_admin)
):
    """
    Получение списка всех пользователей (только для админов)
    """
    users = await User.all()
    return {"users": users}


@router.put("/admin/profile", tags=["admin"])
async def change_user_role(email: str = Form(...),
                           role: str = Form(..., description="Новая роль пользователя"),
                           current_user: User = Depends(require_admin)):
    """

    :param
    :return:
    """
    update_user_role = await AdminService.change_role(email, role)
    return {"message": "Роль пользователя назначена", "user": update_user_role}

