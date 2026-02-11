from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_redirect() -> None:
    """Тест корневого эндпоинта."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check() -> None:
    """Тест эндпоинта проверки работоспособности."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "1.0.0"


def test_create_and_read_item() -> None:
    """Тест создания и чтения элемента."""
    # Создание элемента
    item_data = {
        "name": "Test Item",
        "description": "Test description",
        "price": 9.99,
        "tax": 1.5,
    }
    create_response = client.post("/items/", json=item_data)
    assert create_response.status_code == 201
    created_item = create_response.json()
    assert created_item["name"] == "Test Item"
    assert created_item["price"] == 9.99
    item_id = created_item["id"]

    # Чтение созданного элемента
    read_response = client.get(f"/items/{item_id}")
    assert read_response.status_code == 200
    assert read_response.json()["id"] == item_id


def test_create_user() -> None:
    """Тест создания пользователя."""
    user_data = {"email": "test@example.com", "password": "strongpassword123"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"


def test_get_all_items() -> None:
    """Тест получения всех элементов."""
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_not_found_item() -> None:
    """Тест получения несуществующего элемента."""
    response = client.get("/items/999999")
    assert response.status_code == 404
