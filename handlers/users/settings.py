from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from loader import dp
from states.register import Register
from keyboards.default.menu import main_menu

router = Router()

@router.message(F.text == "⚙️ Sozlamalar")
async def show_settings(message: types.Message):
    await message.answer("Sozlamalar bo'limi.\n\nHozircha siz hududingizni o'zgartirishingiz mumkin:", 
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [types.KeyboardButton(text="📍 Hududni o'zgartirish")],
                                 [types.KeyboardButton(text="⬅️ Orqaga")]
                             ],
                             resize_keyboard=True
                         ))

@router.message(F.text == "📍 Hududni o'zgartirish")
async def change_region(message: types.Message, state: FSMContext):
    await message.answer("Yangi hududni kiriting (masalan: Toshkent, Samarqand, Andijon):")
    await state.set_state(Register.region)

# This router should be included in the users_router
