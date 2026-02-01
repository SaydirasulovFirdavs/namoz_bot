from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from states.zakat import ZakatStates
from keyboards.default.menu import main_menu

router = Router()

NISAB_SUM = 40000000 # Taxminiy nisob miqdori (so'mda)

@router.message(F.text == "💰 Zakat")
async def start_zakat(message: types.Message, state: FSMContext):
    await message.answer(f"Zakat kalkulyatoriga xush kelibsiz!\n\n"
                         f"Zakat berish uchun mablag'ingiz nisobga (kamida {NISAB_SUM:,} so'm) yetgan bo'lishi va bir yil sizda turgan bo'lishi kerak.\n\n"
                         f"Iltimos, zakat beriladigan jami mablag'ingizni kiriting (faqat raqamlarda):")
    await state.set_state(ZakatStates.asking_amount)

@router.message(ZakatStates.asking_amount)
async def calculate_zakat(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Iltimos, faqat raqamlardan foydalanib mablag'ni kiriting:")
        return
    
    amount = int(message.text)
    
    if amount < NISAB_SUM:
        await message.answer(f"Sizning mablag'ingiz ({amount:,} so'm) nisobdan kam. Zakat farz emas.\n"
                             f"Nisob miqdori: {NISAB_SUM:,} so'm.", reply_markup=main_menu)
    else:
        zakat_amount = amount * 0.025
        await message.answer(f"Sizning zakat miqdoringiz: **{zakat_amount:,.0f} so'm**.\n\n"
                             f"(Bu jami mablag'ning 1/40 qismi yoki 2.5% dir.)", 
                             parse_mode="Markdown", reply_markup=main_menu)
    
    await state.clear()
