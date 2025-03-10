from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inline_button_1 = InlineKeyboardButton(text='Спросить у GPT', callback_data='ask_gpt')
inline_button_2 = InlineKeyboardButton(text='Спросить у Yandex', callback_data='ask_yandex')

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[inline_button_1, inline_button_2]])