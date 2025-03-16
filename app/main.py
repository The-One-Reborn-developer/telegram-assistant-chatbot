import logging
import os
import asyncio

from aiogram import Bot, Dispatcher

from app.routes.start import start_router


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    try:
        logging.info('Starting bot...')
        bot = Bot(token=os.environ.get('BOT_TOKEN'))
        dispatcher = Dispatcher()

        dispatcher.include_routers(
            start_router
        )

        await dispatcher.start_polling(bot)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    try:
        asyncio.run(main)
    except (KeyboardInterrupt, SystemExit):
        logging.info('Bot stopped.')
