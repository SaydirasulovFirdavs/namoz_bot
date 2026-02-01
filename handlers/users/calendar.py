from aiogram import types, Router, F
from loader import bot
from utils.db_api.sqlite import Database
from utils.prayer_api.api import PrayerTimes
from utils.image_generator import generate_ramadan_calendar
import os

router = Router()

@router.message(F.text == "📅 Taqvim")
async def send_calendar_image(message: types.Message):
    db = Database()
    user_id = message.from_user.id
    user = db.execute("SELECT region FROM users WHERE id=?", (user_id,), fetchone=True)
    
    if not user or not user[0]:
        await message.answer("Siz hali hududni tanlamagansiz. Iltimos /start buyrug'ini bosing.")
        return
    
    region = user[0]
    await message.answer(f"{region} uchun Ramazon taqvimi tayyorlanmoqda, iltimos kuting...")
    
    prayer_api = PrayerTimes()
    data = prayer_api.get_calendar_times(region, month=3, year=2026)
    
    if data:
        photo_path = generate_ramadan_calendar(region, data)
        from aiogram.types import FSInputFile
        photo = FSInputFile(photo_path)
        await message.answer_photo(photo, caption=f"🌙 {region} shahri uchun 2026-yil Ramazon taqvimi.")
    else:
        await message.answer("Taqvimni yuklashda xatolik yuz berdi. Keyinroq qayta urinib ko'ring.")
