from aiogram import types, Router, F
from keyboards.default.menu import main_menu

router = Router()

PRAYER_LEARN_MENU = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="🌞 Bomdod o'qish tartibi")],
        [types.KeyboardButton(text="🕛 Peshin/Asr/Xufton tartibi")],
        [types.KeyboardButton(text="🌇 Shom o'qish tartibi")],
        [types.KeyboardButton(text="⬅️ Orqaga")]
    ],
    resize_keyboard=True
)

@router.message(F.text == "📖 Namoz o'rganish")
async def show_learning_menu(message: types.Message):
    await message.answer("Qaysi namozning o'qilish tartibini o'rganmoqchisiz?", reply_markup=PRAYER_LEARN_MENU)

@router.message(F.text == "🌞 Bomdod o'qish tartibi")
async def learn_bomdod(message: types.Message):
    text = (
        "🌞 **Bomdod namozi o'qilish tartibi**\n\n"
        "Bomdod namozi 2 rakat sunnat va 2 rakat farzdan iborat.\n\n"
        "**1-Rakat:**\n"
        "1. Niyat qilinadi.\n"
        "2. Takbiri tahrima (Allohu Akbar).\n"
        "3. Sano duosi.\n"
        "4. Fotiha surasi va bitta zam sura.\n"
        "5. Ruku va Sajdalar.\n\n"
        "**2-Rakat:**\n"
        "1. Fotiha va zam sura.\n"
        "2. Ruku va Sajdalar.\n"
        "3. Qa'da (Attahiyat, Salovot, Duo).\n"
        "4. Salom.\n\n"
        "Batafsil ma'lumot uchun Islom.uz portali tavsiya etiladi."
    )
    await message.answer(text, parse_mode="Markdown")

@router.message(F.text == "🕛 Peshin/Asr/Xufton tartibi")
async def learn_4_rakat(message: types.Message):
    text = (
        "🕛 **4 rakatli namozlar tartibi**\n\n"
        "Peshin, Asr va Xufton namozlarining farzi 4 rakatdan iborat.\n\n"
        "1. Dastlabki 2 rakatda Fotiha va zam sura o'qiladi.\n"
        "2. 2-rakatdan keyin o'tirib faqat 'Attahiyat' o'qiladi.\n"
        "3. Keyingi 2 rakatda faqat 'Fotiha' surasi o'qiladi (farz namozida).\n"
        "4. Oxirida o'tirib 'Attahiyat', 'Salovot' va 'Duo' o'qib salom beriladi."
    )
    await message.answer(text, parse_mode="Markdown")

@router.message(F.text == "🌇 Shom o'qish tartibi")
async def learn_shom(message: types.Message):
    print(f"DEBUG: Handler hit with text: {message.text}")
    text = (
        "🌇 **Shom namozi o'qilish tartibi**\n\n"
        "Shom namozi 3 rakat farz va 2 rakat sunnatdan iborat.\n\n"
        "**3 rakatli farz tartibi:**\n"
        "1. Dastlabki 2 rakatda Fotiha va zam sura o'qiladi.\n"
        "2. 2-rakatdan keyin o'tirib 'Attahiyat' o'qiladi.\n"
        "3. 3-rakatda faqat 'Fotiha' surasi o'qiladi.\n"
        "4. Oxirida o'tirib 'Attahiyat', 'Salovot' va 'Duo' o'qib salom beriladi."
    )
    await message.answer(text, parse_mode="Markdown")

@router.message(F.text == "⬅️ Orqaga")
async def back_to_main_menu_learn(message: types.Message):
    await message.answer("Asosiy menyu", reply_markup=main_menu)
