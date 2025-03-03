import config
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import asyncio
from random_fox import fox


TOKEN_API = config.TOKEN_TG

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспечера
bot = Bot(token=TOKEN_API)
dp = Dispatcher()


# /start
@dp.message(Command('start'))
async def command_start(message: types.Message):
    await message.answer(f'Привет, {message.chat.first_name}! я бот JavaRush!!!')


@dp.message(Command('ура'))
async def command_ura(message: types.Message):
    # print(message.chat.first_name)
    await message.answer('Ура, я бот JavaRush!!!')


@dp.message(Command('fox'))
@dp.message(Command('лиса'))
async def command_fox(message: types.Message):
    image_fox = fox()
    await bot.send_photo(message.chat.id, image_fox)


@dp.message(F.text)
async def echo(message: types.Message):
    print(message.text)

    if message.text == "/stop":
        image_fox = fox()
        print(image_fox)
        await message.answer('Хорошо, заканчиваем! Держи лису')
        await bot.send_photo(message.chat.id, image_fox)

    elif 'stop' in message.text:
        await message.answer('Хорошо, заканчиваем!')

    else:
        await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

