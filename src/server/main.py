from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
import logging
logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.INFO
)

from telegram.ext import Updater

from src.skills import register_handler

def create_bot():
    updater = Updater(token=os.getenv("TELEGRAM_BOT_TOKEN"), use_context=True)  # use_context is must for v.11
    register_handler(updater.dispatcher)
    return updater


if __name__ == "__main__":
    app = create_bot()
    logging.info("Server is running!")
    app.start_polling()
