from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    # Create an inline keyboard with a URL button
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Open Mini App", url="https://t.me/testmaksatbot?startapp")]
        ]
    )
    await message.answer('Привет, я HR-BOT. Запусти меня и узри всю мою мощь!', reply_markup=keyboard)


@start_router.message(F.text)
async def cmd_unclear_question(message: Message):
    await message.answer('Я не понимаю этой команды')

