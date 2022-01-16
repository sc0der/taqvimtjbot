from scrapper import ScraperModule, GlobalMessage
from aiogram.types import Message
from aiogram import Bot, executor, types, Dispatcher

# bot = Bot(token="", validate_token=True, parse_mode="HTML")
# dp = Dispatcher(bot, storage=storage)
globalMessage = GlobalMessage()

# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     msg = globalMessage.get_message("welcome")
#     converted_msg = replacer(msg, 'user_name', message['from']['username'] )
#     await message.answer(converted_msg)

if __name__ == "__main__":
    m = globalMessage.get_message("bomdod")
    print(m)
    # newsc = ScraperModule("http://shuroiulamo.tj/tj/namaz")
    # newsc.scrap_page()
    # executor.start_polling(dp, skip_updates=True)