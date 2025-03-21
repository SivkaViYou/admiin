from aiogram.filters import Command
from aiogram.types import Message
from loader import *

@router.message(Command('start'))
async def fun_start(message: Message):
    await message.answer(text='лее прив')