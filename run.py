from scrapper import ScraperModule, GlobalMessage
from aiogram.types import Message
from aiogram import Bot, executor, types, Dispatcher
from config import *
bot = Bot(token=TOKEN, validate_token=True, parse_mode="HTML")
dp = Dispatcher(bot)
globalMessage = GlobalMessage()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    globalMessage.send_text("salom", TOKEN)
    await message.answer(message.chat.id)

@dp.message_handler(commands=['subh'])
async def send_welcome(message: types.Message):
    msg = globalMessage.get_message("subh")
    namoz = globalMessage.get_namoz("subh")
    namosMsg = globalMessage.converter(namoz)
    MSG = f"""*{msg} \n{namosMsg}*"""
    
    await message.answer(MSG, parse_mode='Markdown')

@dp.message_handler(commands=['zukhr'])
async def send_welcome(message: types.Message):
    msg = globalMessage.get_message("zukhr")
    await message.answer(msg)

@dp.message_handler(commands=['asr'])
async def send_welcome(message: types.Message):
    msg = globalMessage.get_message("asr")
    await message.answer(msg)

@dp.message_handler(commands=['maghrib'])
async def send_welcome(message: types.Message):
    msg = globalMessage.get_message("maghrib")
    await message.answer(msg)

@dp.message_handler(commands=['isha'])
async def send_welcome(message: types.Message):
    msg = globalMessage.get_message("isha")
    await message.answer(msg)

if __name__ == "__main__":
    # m = globalMessage.get_message("bomdod")
    # print(m)
    newsc = ScraperModule("http://shuroiulamo.tj/tj/namaz")
    newsc.scrap_page()
    executor.start_polling(dp, skip_updates=True)