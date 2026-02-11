from fastapi import FastAPI

from .routers import items, users
from .schemas import HealthCheck

app = FastAPI(
    title="FastAPI Linter Demo",
    description="Демонстрационное приложение с настроенными линтерами и CI/CD",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Подключение роутеров
app.include_router(items.router)
app.include_router(users.router)


@app.get("/", include_in_schema=False)
async def root() -> dict[str, str]:
    """Корневой эндпоинт."""
    return {"message": "Welcome to FastAPI Linter Demo!"}


@app.get("/health", response_model=HealthCheck)
async def health_check() -> HealthCheck:
    """Проверка работоспособности сервиса."""
    return HealthCheck(status="healthy", version="1.0.0")
