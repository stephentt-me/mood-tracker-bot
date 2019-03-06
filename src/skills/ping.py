from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from src.system.acl import restrict_admin

@restrict_admin
def ping(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id, text="pong")

ping_handler = CommandHandler("ping", ping)
