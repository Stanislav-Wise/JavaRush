from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.random_fox import fox
from keyboards.keyboards import kb1, kb2
from keyboards.inline_kb import inline_keyboard
import random
from .inline_handlers import router as inline_router


router = Router()

router.include_routers(inline_router)



# /start
@router.message(Command('start'))
async def command_start(message: types.Message):
    await message.answer(f'Привет, {message.chat.first_name}! я бот JavaRush!!!', reply_markup=kb1)
    await message.answer(f'{message.chat.first_name} нажми и задай вопрос!', reply_markup=inline_keyboard)

#
# @router.callback_query(F.data == 'ask_gpt')
# async def callback_ask_gpt(callback: types.CallbackQuery):
#     await callback.message.answer('Ты нажал на кнопку GPT')
#     await callback.answer()
#
#
# @router.callback_query(F.data == 'ask_yandex')
# async def callback_ask_yandex(callback: types.CallbackQuery):
#     await callback.message.answer('Ты нажал на кнопку Yandex')
#     await callback.answer()

@router.message(Command('ура'))
async def command_ura(message: types.Message):
    # print(message.chat.first_name)
    await message.answer('Ура, я бот JavaRush!!!', reply_markup=kb2)


@router.message(Command('fox'))
@router.message(Command('лиса'))
async def command_fox(message: types.Message):
    image_fox = fox()
    await message.answer_photo(image_fox)


@router.message(F.text.lower() == 'num')
async def send_number(message: types.Message):
    number = random.randint(1, 100)
    await message.answer(f'Хорошо, твоё число {number}')


# @router.message(F.text)
# async def echo(message: types.Message):
#     print(message.text)
#
#     if message.text == "/stop":
#         image_fox = fox()
#         print(image_fox)
#         await message.answer('Хорошо, заканчиваем! Держи лису')
#         await bot.send_photo(message.chat.id, image_fox)
#
#     elif 'stop' in message.text:
#         await message.answer('Хорошо, заканчиваем!')
#
#     else:
#         await message.answer(message.text)