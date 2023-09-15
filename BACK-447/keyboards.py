from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
    
glavniy_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="CONTACT"),
            KeyboardButton(text="AUDIO"),
        ],
        [
            KeyboardButton(text="VIDEO"),
            KeyboardButton(text="LOCATION"),
        ],
        [
            KeyboardButton(text="STICKER"),
            KeyboardButton(text="PHOTO")
        ],
    ],
    resize_keyboard=True
)