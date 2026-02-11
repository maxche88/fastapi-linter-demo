"""Роутер для работы с пользователями."""
from typing import List

from fastapi import APIRouter, HTTPException

from ..models import User, UserCreate

router = APIRouter(prefix="/users", tags=["users"])

# Имитация базы данных в памяти
fake_users_db: List[User] = []


@router.get("/", response_model=List[User])
async def read_users() -> List[User]:
    """Получить всех пользователей."""
    return fake_users_db


@router.post("/", response_model=User, status_code=201)
async def create_user(user: UserCreate) -> User:
    """Создать нового пользователя."""
    # Простая проверка уникальности email
    for db_user in fake_users_db:
        if db_user.email == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")

    new_id = len(fake_users_db) + 1
    db_user = User(id=new_id, email=user.email)
    fake_users_db.append(db_user)
    return db_user
