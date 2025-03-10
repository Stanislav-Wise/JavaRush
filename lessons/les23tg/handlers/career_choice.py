from zoneinfo import available_timezones

from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from lessons.les22tg.keyboards.prof_keyboards import make_row_keyboard


router = Router()

available_jobs = [
    'Программист',
    'Менеджер',
    'Дизайнер',
    'Маркетолог',
]

available_grades = [
    'Junior',
    'Middle',
    'Senior',
]

class CareerChoice(StatesGroup):
    job = State()
    grade = State()


@router.message(Command('prof'))
async def command_prof(message: types.Message, state: FSMContext):
    await message.answer('Выберите профессию', reply_markup=make_row_keyboard(available_jobs))
    await state.set_state(CareerChoice.job)


@router.message(CareerChoice.job, F.text.in_(available_jobs))
async def prof_chosen(message: types.Message, state: FSMContext):
    await state.update_data(profession=message.text)
    await message.answer('Выберите уровень', reply_markup=make_row_keyboard(available_grades))
    await state.set_state(CareerChoice.grade)


@router.message(CareerChoice.job)
async def prof_incorrect(message: types.Message):
    await message.answer('Выберите профессию', reply_markup=make_row_keyboard(available_jobs))


@router.message(CareerChoice.grade, F.text.in_(available_grades))
async def prof_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f'Профессия: {user_data["profession"]}, уровень: {message.text}',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


@router.message(CareerChoice.grade)
async def prof_incorrect(message: types.Message):
    await message.answer('Выберите уровень', reply_markup=make_row_keyboard(available_grades))