from pydantic import BaseModel


class Message(BaseModel):
    """Схема сообщения."""

    message: str


class HealthCheck(BaseModel):
    """Схема проверки работоспособности."""

    status: str
    version: str
