import logging  # эта библиотека идет вместе с python
import os

from aiogram import Bot, Dispatcher, executor, types  # импортируем aiogram


logging.basicConfig(level=logging.INFO)  # Initialize bot and dispatcher
bot = Bot(token=os.getenv('TOKEN_BOT'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Это простейший бот на aiogram")  # отвечает на сообщение


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


# base_url = URL + TOKEN
# parametrs['text'] = 'Привет второй'
# send_message(base_url, parametrs)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
