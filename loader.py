from aiogram import Bot, Dispatcher, Router
from config.token import TOKEN

router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN)
with open('zapret.txt', 'r', encoding='utf-8') as file:
    text = file.read()
FORBIDDEN_WORDS = text.split()


user_violations = {}
MAX_VIOLATIONS = 3
MUTE_DURATION = 10