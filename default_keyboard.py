from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Menyu 1"), KeyboardButton("Menyu 2"), KeyboardButton("Menyu 3"))
keyboard.add(KeyboardButton("Menyu 4"), KeyboardButton("Menyu 5"), KeyboardButton("Menyu 6"))
keyboard.add(KeyboardButton("Menyu 7"))
keyboard.add(KeyboardButton("Menyu 8"))


