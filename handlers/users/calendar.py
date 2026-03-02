from aiogram import types, Router, F
from loader import bot
from utils.db_api.sqlite import Database
from utils.image_generator import generate_ramadan_calendar
from data.ramadan_constants import RAMADAN_2026_TASHKENT, REGIONAL_OFFSETS
from datetime import datetime, timedelta
import os

router = Router()

def adjust_time(time_str, minutes):
    """Helper to add/subtract minutes from HH:MM string"""
    t = datetime.strptime(time_str, "%H:%M")
    new_t = t + timedelta(minutes=minutes)
    return new_t.strftime("%H:%M")

@router.message(F.text == "📅 Taqvim")
async def send_calendar_image(message: types.Message):
    db = Database()
    user_id = message.from_user.id
    user = db.execute("SELECT region FROM users WHERE id=?", (user_id,), fetchone=True)
    
    if not user or not user[0]:
        await message.answer("Siz hali hududni tanlamagansiz. Iltimos /start buyrug'ini bosing.")
        return
    
    region = user[0]
    await message.answer(f"🌙 {region} shahri uchun 100% aniq Ramazon taqvimi tayyorlanmoqda, iltimos kuting...")
    
    # Get accurate offsets
    offset = REGIONAL_OFFSETS.get(region, {"sahar": 0, "iftor": 0})
    if isinstance(offset, int): # Handle cases like Samarqand: 10
        offset = {"sahar": offset, "iftor": offset}
        
    # Generate regional data from Tashkent baseline
    regional_data = []
    for day in RAMADAN_2026_TASHKENT:
        new_day = day.copy()
        new_day['sahar'] = adjust_time(day['sahar'], offset['sahar'])
        new_day['iftor'] = adjust_time(day['iftor'], offset['iftor'])
        regional_data.append(new_day)

    photo_path = generate_ramadan_calendar(region, regional_data)
    from aiogram.types import FSInputFile
    photo = FSInputFile(photo_path)
    await message.answer_photo(photo, caption=f"🌙 {region} shahri uchun 2026-yil (1447-hijriy) Ramazon taqvimi.\n\n"
                                           f"✅ **Manba:** O'zbekiston Musulmonlari idorasi (gazeta.uz)\n"
                                           f"🙏 Duolarni **Duolar** bo'limidan topishingiz mumkin.",
                             parse_mode="Markdown")
