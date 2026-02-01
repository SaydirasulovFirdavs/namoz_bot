from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from utils.db_api.sqlite import Database
from states.register import Register
from keyboards.default.menu import main_menu


router = Router()

@router.message(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    db = Database()
    user_id = message.from_user.id
    name = message.from_user.full_name
    
    # Check if user already exists
    user = db.execute("SELECT region FROM users WHERE id=?", (user_id,), fetchone=True)
    
    if user and user[0]:
        await message.answer(f"Xush kelibsiz, {name}!", reply_markup=main_menu)
        return

    db.add_user(id=user_id, full_name=name)
    await message.answer(f"Assalomu alaykum, {name}!\n"
                         f"Namoz vaqtlari botiga xush kelibsiz.\n"
                         f"Iltimos, hududingizni kiriting (masalan: Toshkent, Samarqand, Andijon):")
    await state.set_state(Register.region)
