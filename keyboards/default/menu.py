from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📿 Tasbeh"),
            KeyboardButton(text="📅 Taqvim")
        ],
        [
            KeyboardButton(text="📖 Duolar"),
            KeyboardButton(text="🕌 Qibla")
        ],
        [
            KeyboardButton(text="💰 Zakat"),
            KeyboardButton(text="📖 Namoz o'rganish")
        ],
        [
            KeyboardButton(text="✅ Reja"),
            KeyboardButton(text="⚙️ Sozlamalar")
        ]
    ],
    resize_keyboard=True
)

tasbih_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📿 Subhanalloh"),
            KeyboardButton(text="📿 Alhamdulillah")
        ],
        [
            KeyboardButton(text="📿 Allohu Akbar")
        ],
        [
            KeyboardButton(text="🔄 Nolga tushirish"),
            KeyboardButton(text="⬅️ Orqaga")
        ]
    ],
    resize_keyboard=True
)

dua_categories = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="☀️ Tonggi duolar"),
            KeyboardButton(text="🌙 Kechki duolar")
        ],
        [
            KeyboardButton(text="🍽 Ovqatdan so'ng"),
            KeyboardButton(text="🚗 Safar duosi")
        ],
        [
            KeyboardButton(text="🌙 Saharlik va iftorlik duolari")
        ],
        [
            KeyboardButton(text="⬅️ Orqaga")
        ]
    ],
    resize_keyboard=True
)

