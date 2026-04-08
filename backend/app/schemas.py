from pydantic import BaseModel
from typing import List, Any

class ItemOut(BaseModel):
    id: int
    name: str
    price: float
    photo: str | None
    category: str | None

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    user_id: str
    items: List[Any]
    total: float
    phone: str
    address: str | None

class OrderOut(BaseModel):
    id: int
    user_id: str
    items: List[Any]
    total: float
    phone: str
    address: str | None
    status: str
