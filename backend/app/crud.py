from sqlalchemy import select
from .models import Item, Order

async def get_menu(db):
    result = await db.execute(select(Item))
    return result.scalars().all()

async def create_order(db, order_data):
    order = Order(**order_data)
    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order

async def update_order_status(db, order_id, status):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if order:
        order.status = status
        await db.commit()
        await db.refresh(order)
    return order
