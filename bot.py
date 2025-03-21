import logging
import handlers.start
import handlers.moderator
import asyncio
from loader import *

async def main():
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())