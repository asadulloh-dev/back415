import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards import *

API_TOKEN = '6251436063:AAHrF5-3rQLWYI7Fv9Q3MofYIGLW7m2WXkU'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom!\nBu BACK-447 gruppaning boti!",
                        reply_markup=glavniy_menu)


@dp.message_handler(text = "CONTACT")
async def echo(message: types.Message):
    await message.answer_contact("+998 90 824 44 48", "01.saidakhmedovv")

@dp.message_handler(text = "BACK-415 haqida")
async def echo(message: types.Message):
    await message.answer("""Bu jamoa o'quvchilari juda ahil!
                         Bu jamoa xonasining raqami A3""")
    
@dp.message_handler(text = "Mars haqida")
async def echo(message: types.Message):
    await message.answer("""Bu yerda IT Starter
                          kursidan boshlanadi""")
    
@dp.message_handler(text = "Mars mini narxi")
async def echo(message: types.Message):
    await message.answer("30 coin")
                          
    
@dp.message_handler(text = "Mars shokolad narxi")
async def echo(message: types.Message):
    await message.answer("50 coin")
    
@dp.message_handler(text = "Mars haqida")
async def echo(message: types.Message):
    await message.answer("""Bu yerda IT Starter
                          kursidan boshlanadi""")
    
@dp.message_handler(text = "Mars haqida")
async def echo(message: types.Message):
    await message.answer("""Bu yerda IT Starter
                          kursidan boshlanadi""")
    
@dp.message_handler(text = "Mars haqida")
async def echo(message: types.Message):
    await message.answer("""Bu yerda IT Starter
                          kursidan boshlanadi""")
    
@dp.message_handler(text = "Mars haqida")
async def echo(message: types.Message):
    await message.answer("""Bu yerda IT Starter
                          kursidan boshlanadi""")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




