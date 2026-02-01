from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from states.register import Register
from utils.db_api.sqlite import Database
from utils.prayer_api.api import PrayerTimes
from keyboards.default.menu import main_menu

router = Router()

@router.message(Register.region)
async def bot_region(message: types.Message, state: FSMContext):
    region = message.text
    db = Database()
    prayer_api = PrayerTimes()
    
    # Check if region is valid by trying to fetch times
    data = prayer_api.get_prayer_times(region)
    
    if data:
        times = data['timings']
        db.update_user_region(id=message.from_user.id, region=region)
        await message.answer(f"Rahmat! Hududingiz {region} ga o'zgartirildi.\n"
                             f"Endi sizga namoz vaqtlarida eslatma boradi.",
                             reply_markup=main_menu)
        await state.clear()
        
        # Show today's times
        msg = "Bugungi namoz vaqtlari:\n"
        prayers_uz = {
            'Fajr': 'Bomdod',
            'Sunrise': 'Quyosh chiqishi',
            'Dhuhr': 'Peshin',
            'Asr': 'Asr',
            'Maghrib': 'Shom',
            'Isha': 'Xufton'
        }
        for prayer_en, prayer_uz in prayers_uz.items():
            if prayer_en in times:
                 msg += f"{prayer_uz}: {times[prayer_en]}\n"
        await message.answer(msg)
    else:
        await message.answer("Uzur, bunday hudud topilmadi yoki xatolik yuz berdi. Iltimos qaytadan to'g'ri yozing:")
