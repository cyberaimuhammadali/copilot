from fastapi import FastAPI, Depends, HTTPException
from .database import get_db, Base, engine
from . import crud, schemas
import asyncio

app = FastAPI(title="Kafe API")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/menu", response_model=list[schemas.ItemOut])
async def read_menu(db=Depends(get_db)):
    return await crud.get_menu(db)

@app.post("/order", response_model=schemas.OrderOut)
async def create_order(order: schemas.OrderCreate, db=Depends(get_db)):
    data = order.dict()
    created = await crud.create_order(db, data)
    # TODO: notify bot via webhook or DB polling
    return created

@app.post("/order/{order_id}/status")
async def set_status(order_id: int, status: str, db=Depends(get_db)):
    updated = await crud.update_order_status(db, order_id, status)
    if not updated:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"ok": True}
