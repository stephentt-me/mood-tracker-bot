from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
import logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

from telegram.ext import Updater

from src.skills import register_handler

def create_app():
    updater = Updater(token=os.getenv("TELEGRAM_BOT_TOKEN"), use_context=True)  # use_context is must for v.11
    register_handler(updater.dispatcher)
    return updater


if __name__ == "__main__":
    app = create_app()
    print("App started!")
    app.start_polling()
