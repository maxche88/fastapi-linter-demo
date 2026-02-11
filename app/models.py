from typing import Optional

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    """Базовая модель элемента."""

    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    tax: Optional[float] = Field(None, ge=0)


class ItemCreate(ItemBase):
    """Модель для создания элемента."""

    pass


class Item(ItemBase):
    """Полная модель элемента с ID."""

    id: int

    model_config = {"from_attributes": True}


class UserBase(BaseModel):
    """Базовая модель пользователя."""

    email: str = Field(..., pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")


class UserCreate(UserBase):
    """Модель для создания пользователя."""

    password: str = Field(..., min_length=8)


class User(UserBase):
    """Полная модель пользователя с ID."""

    id: int

    model_config = {"from_attributes": True}
