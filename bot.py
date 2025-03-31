import asyncio
from aiogram import Bot, Dispatcher
from handlers import router  # Импортируем router из handlers.py
from config import BOT_TOKEN

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)  # Подключаем маршрутизатор

    await bot.delete_webhook(drop_pending_updates=True)  # Чистим старые апдейты
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())  # Этот способ может вызвать ошибку на Windows
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
