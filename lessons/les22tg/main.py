import config
import logging
from aiogram import Bot, Dispatcher
import asyncio
from handlers import common, career_choice


async def main():
    TOKEN_API = config.TOKEN_TG

    # Включаем логирование
    logging.basicConfig(level=logging.INFO)

    # Инициализируем бота и диспечера
    bot = Bot(token=TOKEN_API)
    dp = Dispatcher()

    dp.include_router(career_choice.router)
    dp.include_router(common.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

