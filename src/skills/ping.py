from telegram.bot import Bot
from telegram.ext import CallbackContext

from telegram.ext import CommandHandler

def ping(update: Bot, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id, text="pong")

ping_handler = CommandHandler("ping", ping)
