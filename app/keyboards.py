from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню.",
    keyboard=[
    [KeyboardButton(text="Товары"), KeyboardButton(text="Купить")],
    [KeyboardButton(text="Личный кабинет"), KeyboardButton(text="Пополнить баланс")],
    [KeyboardButton(text="Помощь"), KeyboardButton(text="Отзывы")],
])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить", url="https://google.com")],
])