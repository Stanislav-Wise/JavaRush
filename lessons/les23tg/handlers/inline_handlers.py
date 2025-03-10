from aiogram import Router, types, F


router = Router()


@router.callback_query(F.data == 'ask_gpt')
async def callback_ask_gpt(callback: types.CallbackQuery):
    await callback.message.answer('Ты нажал на кнопку GPT')
    await callback.answer()


@router.callback_query(F.data == 'ask_yandex')
async def callback_ask_yandex(callback: types.CallbackQuery):
    await callback.message.answer('Ты нажал на кнопку Yandex')
    await callback.answer()