from scrapper import ScraperModule, GlobalMessage, TgGroupsModule
from aiogram.types import Message
from aiogram import Bot, executor, types, Dispatcher
from config import *

bot = Bot(token=TOKEN, validate_token=True, parse_mode="HTML")
dp = Dispatcher(bot)

globalMessage = GlobalMessage()
timer = TgGroupsModule()


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery):
    input_content = types.InputTextMessageContent(message_text="salom", parse_mode="Markdown")

    results = [types.InlineQueryResultArticle(
            id='0',
            title="Введите имя: ",
            input_message_content=input_content
        )]
    await bot.answer_inline_query(inline_query.id, results=results, cache_time=120, is_personal=True)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    globalMessage.send_text("salom", TOKEN)
    await message.answer(message.chat.id)

@dp.message_handler(commands=['subh'])
async def send_welcome(message: types.Message):
    msg = globalMessage.message('subh')
    await message.answer(msg, parse_mode='Markdown')

@dp.message_handler(commands=['zukhr'])
async def send_welcome(message: types.Message):
    msg = globalMessage.message('zukhr')
    await message.answer(msg, parse_mode='Markdown')

@dp.message_handler(commands=['asr'])
async def send_welcome(message: types.Message):
    msg = globalMessage.message('asr')
    await message.answer(msg, parse_mode='Markdown')

@dp.message_handler(commands=['maghrib'])
async def send_welcome(message: types.Message):
    msg = globalMessage.message('maghrib')
    await message.answer(msg, parse_mode='Markdown')

@dp.message_handler(commands=['isha'])
async def send_welcome(message: types.Message):
    msg = globalMessage.message('isha')
    await message.answer(msg, parse_mode='Markdown')

if __name__ == "__main__":
    # timer.is_Time("zukhr")
    executor.start_polling(dp, skip_updates=True)