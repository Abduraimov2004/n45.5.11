from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_keyboard = InlineKeyboardMarkup()
inline_keyboard.add(
    InlineKeyboardButton(text="➖", callback_data="minus"),
    InlineKeyboardButton(text="Count", callback_data="count"),
    InlineKeyboardButton(text="➕", callback_data="plus")
)