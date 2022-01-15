from scrapper import ScraperModule
from aiogram.types import Message
from aiogram import Bot, executor, types, Dispatcher, executor
from aiogram_dialog import DialogManager, StartMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

bot = Bot(token=TOKEN, validate_token=True, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    msg = globalMessage.get_message("welcome")
    converted_msg = replacer(msg, 'user_name', message['from']['username'] )
    await message.answer(converted_msg)

if __name__ == "__main__":
    newsc = ScraperModule("http://shuroiulamo.tj/tj/namaz")
    newsc.scrap_page()
    executor.start_polling(dp, skip_updates=True)