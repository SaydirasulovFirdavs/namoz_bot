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
    await message.answer(f"🌙 {region} shahri uchun Ramazon taqvimi tayyorlanmoqda, iltimos kuting...")
    
    prayer_api = PrayerTimes()
    from data.config import HIJRI_OFFSET
    
    # Aladhan API supports 'adjustment' param for Hijri
    data = prayer_api.get_calendar_times(region, month=3, year=2026, adjustment=HIJRI_OFFSET) # Ramadan 2026 is mostly in March
    
    if data:
        # If there's an offset, we might need to shift the data or use Aladhan's built-in support if possible
        # For now, we take the 30-day block corresponding to Ramadan
        ramadan_data = []
        for day in data:
            hijri_month = int(day['date']['hijri']['month']['number'])
            if hijri_month == 9:
                ramadan_data.append(day)
        
        if not ramadan_data:
            # Fallback if March doesn't have Ramadan
            ramadan_data = data[:30]

        photo_path = generate_ramadan_calendar(region, ramadan_data)
        from aiogram.types import FSInputFile
        photo = FSInputFile(photo_path)
        await message.answer_photo(photo, caption=f"🌙 {region} shahri uchun 2026-yil (1447-hijriy) Ramazon taqvimi.\n\n"
                                               f"⚠️ *Eslatma:* Rasmiy sana e'lon qilinishi bilan taqvim o'zgarishi mumkin.",
                                 parse_mode="Markdown")
    else:
        await message.answer("Taqvimni yuklashda xatolik yuz berdi. Keyinroq qayta urinib ko'ring.")
