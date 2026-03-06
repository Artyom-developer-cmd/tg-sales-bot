from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router

from app.keyboards import main, settings

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('''
✋ Привет, дорогой гость!
Добро пожаловать в нашу <b>Lavka</b> — место, где собраны самые вкусные предложения.

Ты у нас впервые? Это прекрасно! Чтобы ты чувствовал себя как дома и ничего не упустил, сохрани нашу небольшую шпаргалку:

🍃 <b>Как тут всё устроено:</b>
➖ <a href='https://teletype.in/@/'>Инструкция: Как пополнить и купить</a>
➖ <a href='https://teletype.in/@/'>Поиск секретов: Где лежит инструкция к товару</a>
➖ <a href='https://teletype.in/@/'>Связь с хранителем лавки (Поддержка)</a>
➖ <a href='https://teletype.in/@/'>Лайфхаки: Как экономить с нами?</a>

📌 <b>Особый ингредиент для новичков:</b>
Обязательно загляни сюда, чтобы получить промокод к первому заказу 👇
https://.in

• Техподдержка: @

А теперь — скорее смотри, что у нас есть вкусненького в меню ниже! 👇''', reply_markup=main, parse_mode="HTML")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Это команда help")

@router.message(F.text == "Как дела?")
async def how_are_you(message: Message):
    await message.answer("Привет все норм")

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID фото: {message.photo[-1].file_id}")
