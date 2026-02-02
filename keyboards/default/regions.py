from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

regions_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent"),
            KeyboardButton(text="Andijon")
        ],
        [
            KeyboardButton(text="Buxoro"),
            KeyboardButton(text="Farg'ona")
        ],
        [
            KeyboardButton(text="Jizzax"),
            KeyboardButton(text="Xorazm")
        ],
        [
            KeyboardButton(text="Namangan"),
            KeyboardButton(text="Navoiy")
        ],
        [
            KeyboardButton(text="Qashqadaryo"),
            KeyboardButton(text="Qoraqalpog'iston")
        ],
        [
            KeyboardButton(text="Samarqand"),
            KeyboardButton(text="Sirdaryo")
        ],
        [
            KeyboardButton(text="Surxondaryo")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Viloyatingizni tanlang..."
)
