from aiogram import Bot, Dispatcher, Router
from config.token import TOKEN
import random

frazi1 = ['чооооо атлетаи лошок на',
         '😂🤣👎👎 шдем тепя рапка черес',
         'лееее брадка ну тут мут на',
         'от вашего высира явшоки высриш ищо черес']

frazi2 = ['куда ссылки шлеш балбес',
         'ссылке не кидать ало',
         'чоооо фишинг ссылко бон',
         'эммм брадка тут без этага пон']

frazi3 = ['убрал высир не благодорите',
         'чота на туалет иди рапок',
         'эмммм',
         'беснегативчика ато бан']

router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN)
with open('zapret.txt', 'r', encoding='utf-8') as file:
    text = file.read()
FORBIDDEN_WORDS = text.split()


user_violations = {}
MAX_VIOLATIONS = 3
MUTE_DURATION = 5