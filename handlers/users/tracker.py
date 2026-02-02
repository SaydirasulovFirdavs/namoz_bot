from aiogram import types, Router, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import bot
from utils.db_api.sqlite import Database
from datetime import datetime

router = Router()

def get_tracker_keyboard(user_id, date, data):
    builder = InlineKeyboardBuilder()
    
    prayers = [
        ("fajr", "Bomdod"),
        ("dhuhr", "Peshin"),
        ("asr", "Asr"),
        ("maghrib", "Shom"),
        ("isha", "Xufton")
    ]
    
    if not data:
        data = (0, 0, 0, 0, 0)
        
    for i, (key, label) in enumerate(prayers):
        status = "✅" if data[i] else "❌"
        builder.button(text=f"{label} {status}", callback_data=f"track:{key}:{1 if not data[i] else 0}")
    
    builder.adjust(2)
    return builder.as_markup()

import pytz
TASHKENT = pytz.timezone('Asia/Tashkent')

@router.message(F.text == "✅ Reja")
async def show_tracker(message: types.Message):
    db = Database()
    today = datetime.now(TASHKENT).strftime("%Y-%m-%d")
    data = db.get_daily_tracker(message.from_user.id, today)
    
    await message.answer(f"📅 **Bugungi namozlar rejasi ({today})**\n\nQaysi namozni ado etgan bo'lsangiz, ustiga bosing:", 
                         reply_markup=get_tracker_keyboard(message.from_user.id, today, data),
                         parse_mode="Markdown")

@router.callback_query(F.data.startswith("track:"))
async def track_prayer(call: types.CallbackQuery):
    _, prayer, status = call.data.split(":")
    status = int(status)
    
    db = Database()
    today = datetime.now(TASHKENT).strftime("%Y-%m-%d")
    db.update_prayer_status(call.from_user.id, today, prayer, status)
    
    # Refresh keyboard
    data = db.get_daily_tracker(call.from_user.id, today)
    await call.message.edit_reply_markup(reply_markup=get_tracker_keyboard(call.from_user.id, today, data))
    await call.answer("Holat yangilandi!")
