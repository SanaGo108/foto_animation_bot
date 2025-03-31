from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import ContentType
import aiohttp
from d_id_api import animate_photo
from config import BOT_TOKEN

router = Router()  # Создаем роутер для регистрации хэндлеров


@router.message(Command("start"))  # Используем Command("start") вместо commands=["start"]
async def start_command(message: types.Message):
    await message.answer("Привет! Отправьте мне фотографию, и я её оживлю!")


@router.message(F.photo)  # Новый способ фильтрации фото в aiogram 3.x
async def handle_photo(message: types.Message):
    """
    Получает фото, загружает его на сервер Telegram и отправляет в D-ID API.
    """
    photo = message.photo[-1]  # Берем самое большое фото
    file_info = await message.bot.get_file(photo.file_id)
    file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}"

    animated_video_url = await animate_photo(file_url)

    if animated_video_url:
        await message.answer("Вот ваша анимированная фотография!")
        await message.answer_video(animated_video_url)
    else:
        await message.answer("Ошибка при обработке изображения. Попробуйте снова.")


