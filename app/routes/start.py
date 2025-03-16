from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from api.gpt import generate_response


start_router = Router()


@start_router.message(CommandStart())
async def handle_start_command(message: Message):
    response = await generate_response(
        f'New user comes in contact. Their name is {message.from_user.full_name}')
    print(message)
    await message.answer(response, parse_mode='MarkdownV2')
