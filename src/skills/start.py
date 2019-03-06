"""Handle /start, incharge for register user, inform user about this app
"""
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

from src.models.user import User
from src.models.base import Session
from src.system.database import session_scope
from src.system.acl import must_be_user

@must_be_user
@session_scope
def start(update: Update, context: CallbackContext, session):
    context.bot.send_message(update.message.chat_id, f"Welcome Welcome!")

start_handler = CommandHandler("start", start)
