from aiogram import types, Router, F
from loader import dp
import math

router = Router()

def calculate_qibla_angle(lat, lon):
    # Kaaba coordinates
    kaaba_lat = 21.4225
    kaaba_lon = 39.8262
    
    phi1 = math.radians(lat)
    phi2 = math.radians(kaaba_lat)
    d_lambda = math.radians(kaaba_lon - lon)
    
    y = math.sin(d_lambda)
    x = math.cos(phi1) * math.tan(phi2) - math.sin(phi1) * math.cos(d_lambda)
    
    angle = math.degrees(math.atan2(y, x))
    return (angle + 360) % 360

@router.message(F.text == "🕌 Qibla")
async def ask_location(message: types.Message):
    await message.answer("Qibla yo'nalishini aniqlash uchun iltimos, joylashuvingizni (location) yuboring:", 
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[[types.KeyboardButton(text="📍 Joylashuvni yuborish", request_location=True)],
                                       [types.KeyboardButton(text="⬅️ Orqaga")]],
                             resize_keyboard=True
                         ))

@router.message(F.location)
async def get_qibla(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    
    angle = calculate_qibla_angle(lat, lon)
    
    # Generate visual indicator
    from utils.qibla_image import generate_qibla_compass
    from aiogram.types import FSInputFile
    photo_path = generate_qibla_compass(angle)
    photo = FSInputFile(photo_path)
    
    # Map angle to compass direction
    directions = ["Shimol", "Shimoliy-Sharq", "Sharq", "Janubiy-Sharq", "Janub", "Janubiy-G'arb", "G'arb", "Shimoliy-G'arb"]
    idx = int((angle + 22.5) / 45) % 8
    direction_name = directions[idx]
    
    await message.answer_photo(photo, caption=f"Sizning joylashuvingiz bo'yicha Qibla yo'nalishi:\n\n"
                         f"🧭 Azimut: **{angle:.2f}°**\n"
                         f"📍 Yo'nalish: **{direction_name}**\n\n"
                         f"Rasmda oltin rangli o'q Ka'ba tomonga yo'nalgan (N - Shimol).")
