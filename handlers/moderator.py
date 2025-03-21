from aiogram.types import Message
from loader import *
from datetime import datetime, timedelta


async def record_violation(user_id):
    if user_id not in user_violations:
        user_violations[user_id] = {
            'count': 0,
            'last_violation': None
        }
    violations = user_violations[user_id]
    violations['count'] += 1
    violations['last_violation'] = datetime.now()


async def check_user_mute(user_id):
    if user_id in user_violations:
        violations = user_violations[user_id]
        if violations['count'] >= MAX_VIOLATIONS:
            mute_end = violations['last_violation'] + timedelta(minutes=MUTE_DURATION)
            if datetime.now() < mute_end:
                return True
            else:
                user_violations[user_id] = {'count': 0, 'last_violation': None}
    return False

@router.message()
async def handle_message(message: Message):

    user_id = message.from_user.id

    if await check_user_mute(user_id):
        await message.delete()
        await message.answer(
            f"@{message.from_user.username}, атлетай"
            f"в мут на {MUTE_DURATION} нефиг была нарушать")
        return
    if message.entities:
        for entity in message.entities:
            if entity.type in ['url', 'text_link']:
                await message.delete()
                await record_violation(user_id)
                await message.answer(
                    f"@{message.from_user.username}, убрал твои высир"
                    f"не кидай ссылки рапок {user_violations[user_id]['count']}")
                return
    text = message.text.lower()
    for word in FORBIDDEN_WORDS:
        if word in text:
            await message.delete()
            await record_violation(user_id)
            await message.answer(
                f"@{message.from_user.username}, убрал высир"
                f" не материс балбес статья {user_violations[user_id]['count']}")
            return

