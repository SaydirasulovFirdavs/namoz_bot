from aiogram import types, Router, F
from keyboards.default.menu import main_menu, tasbih_menu
from utils.db_api.sqlite import Database

router = Router()

@router.message(F.text == "📿 Tasbeh")
async def show_tasbih(message: types.Message):
    db = Database()
    count = db.get_tasbih(message.from_user.id)
    await message.answer(f"Tasbeh bo'limiga xush kelibsiz!\n\nUmumiy zikrlar soni: {count}", 
                         reply_markup=tasbih_menu)

@router.message(F.text == "⬅️ Orqaga")
async def back_to_menu(message: types.Message):
    await message.answer("Asosiy menyu", reply_markup=main_menu)

@router.message(F.text == "🔄 Nolga tushirish")
async def reset_tasbih(message: types.Message):
    db = Database()
    db.update_tasbih(message.from_user.id, 0)
    await message.answer("Tasbeh hisobi nolga tushirildi.", reply_markup=tasbih_menu)

@router.message(F.text.startswith("📿 "))
async def count_zikr(message: types.Message):
    db = Database()
    user_id = message.from_user.id
    current_count = db.get_tasbih(user_id)
    new_count = current_count + 1
    db.update_tasbih(user_id, new_count)
    
    zikr_name = message.text.replace("📿 ", "")
    await message.answer(f"{zikr_name}\n\nSizni zikrlaringiz soni: {new_count}", 
                         reply_markup=tasbih_menu)
