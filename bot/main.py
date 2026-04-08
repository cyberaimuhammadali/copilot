import asyncio, os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo
import aiohttp

API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")  # e.g. https://your-domain.com

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(text="🍔 Menyu", web_app=WebAppInfo(url=f"{WEBAPP_URL}/menu")))
    kb.add(types.KeyboardButton(text="📦 Buyurtma statusi"))
    await message.answer("Salom! Kafega xush kelibsiz.", reply_markup=kb)

@dp.message()
async def handle_text(message: types.Message):
    if message.text == "📦 Buyurtma statusi":
        await message.answer("Buyurtma ID ni yuboring:")
    else:
        await message.answer("Menyu uchun tugmani bosing yoki /start yozing.")

# WebApp data handler (when WebApp posts order back to bot)
@dp.message()
async def webapp_data(message: types.Message):
    # If WebApp sends a JSON payload via Telegram WebApp, it arrives as message.web_app_data
    if message.web_app_data:
        data = message.web_app_data.data  # stringified JSON
        # forward to backend
        async with aiohttp.ClientSession() as session:
            resp = await session.post(f"{os.getenv('BACKEND_URL')}/order", json=data)
            if resp.status == 200:
                order = await resp.json()
                await message.answer(f"Buyurtma qabul qilindi. ID: {order['id']}")
            else:
                await message.answer("Buyurtma yuborishda xatolik yuz berdi.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
