from aiogram import types, Router, F
from keyboards.default.menu import main_menu, dua_categories

router = Router()

DUAS = {
    "☀️ Tonggi duolar": "🌅 **Tonggi azkorlar**\n\n1. `Alhamdulillahillazi ahyana ba'da ma amatana va ilayhin nushur.`\n(Bizni o'ldirgandan keyin qayta tiriltirgan Allohga hamd bo'lsin. Qayta tirilish Unung huzurigadir.)\n\n2. `Oyatul Kursiy`ni o'qish tavsiya etiladi.",
    "🌙 Kechki duolar": "🌌 **Kechki azkorlar**\n\n1. `Bismillahi-llazi la yadurru ma'as-mihi shay'un fil-ardi va la fis-sama'i va huvas-sami'ul-'alim.` (3 marta)\n(Shunday Allohning ismi bilan boshlaymanki, Uning ismi bilan na yerda va na ko'kda biror narsa zarar yetkaza olmaydi. U eshituvchi va biluvchidir.)",
    "🍽 Ovqatdan so'ng": "🍲 **Ovqatdan so'ng o'qiladigan duo**\n\n`Alhamdulillahillazi at'amana va saqona va ja'alana minal muslimin.`\n(Bizni taomlantirgan, sug'organ va musulmonlardan qilgan Allohga hamd bo'lsin.)",
    "🚗 Safar duosi": "🛤 **Safar duosi**\n\n`Subhanallazi sakh-khara lana hazava ma kunna lahu muqrinina va inna ila rabbina lamunqalibun.`\n(Bizga buni bo'ysundirib qo'ygan Zot pokdir. Biz o'zimiz buni bo'ysundiruvchi emas edik. Albatta, biz Robbimizga qaytuvchilarmiz.)"
}

@router.message(F.text == "📖 Duolar")
async def show_dua_categories(message: types.Message):
    await message.answer("Duolar bo'limi. Kerakli kategoriyani tanlang:", reply_markup=dua_categories)

@router.message(F.text.in_(DUAS.keys()))
async def send_dua(message: types.Message):
    content = DUAS[message.text]
    await message.answer(content, parse_mode="Markdown")
