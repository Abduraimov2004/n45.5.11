import logging
from default_keyboard import keyboard
from inline_keyboard import inline_keyboard
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7202294382:AAEqrzzFPIQ3QH8O2ssuZOleRHDamU6U6JE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


class Counter:
    minus_count = 0
    plus_count = 0


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    await message.reply(f" Assalomu alaykum {first_name}", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text.startswith('Menyu'))
async def button_click(message: types.Message):
    await message.answer("Default keyboard", reply_markup=keyboard)
    await message.answer("Inline keyboard:", reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda c: c.data)
async def inline_button_click(callback_query: types.CallbackQuery):
    code = callback_query.data
    await bot.answer_callback_query(callback_query.id)

    if code == "minus":
        Counter.minus_count += 1
        await bot.send_message(callback_query.from_user.id, "Minus")
    elif code == "count":
        await bot.send_message(callback_query.from_user.id, f"Count: Minus {Counter.minus_count}, Plus {Counter.plus_count}")
    elif code == "plus":
        Counter.plus_count += 1
        await bot.send_message(callback_query.from_user.id, "Plus")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
