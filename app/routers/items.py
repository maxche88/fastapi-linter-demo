from typing import List

from fastapi import APIRouter, HTTPException

from ..models import Item, ItemCreate

router = APIRouter(prefix="/items", tags=["items"])

# Имитация базы данных в памяти
fake_items_db: List[Item] = []


@router.get("/", response_model=List[Item])
async def read_items() -> List[Item]:
    """Получить все элементы."""
    return fake_items_db


@router.post("/", response_model=Item, status_code=201)
async def create_item(item: ItemCreate) -> Item:
    """Создать новый элемент."""
    new_id = len(fake_items_db) + 1
    db_item = Item(id=new_id, **item.model_dump())
    fake_items_db.append(db_item)
    return db_item


@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int) -> Item:
    """Получить элемент по ID."""
    for item in fake_items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemCreate) -> Item:
    """Обновить элемент по ID."""
    for idx, db_item in enumerate(fake_items_db):
        if db_item.id == item_id:
            updated_item = Item(id=item_id, **item.model_dump())
            fake_items_db[idx] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int) -> None:
    """Удалить элемент по ID."""
    for idx, db_item in enumerate(fake_items_db):
        if db_item.id == item_id:
            del fake_items_db[idx]
            return None
    raise HTTPException(status_code=404, detail="Item not found")
