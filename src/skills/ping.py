from datetime import datetime

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from src.system.acl import restrict_admin, must_be_user
from src.system.database import session_scope


@restrict_admin
@must_be_user
@session_scope
def ping(update: Update, context: CallbackContext, session):
    context.bot.send_message(update.message.chat_id, "pong")


ping_handler = CommandHandler("ping", ping)
