"""Handle /start, incharge for register user, inform user about this app
"""
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

from src.models.user import User
from src.models.base import Session
from src.system.database import session_scope

@session_scope
def start(update: Update, context: CallbackContext, session):
    req_user = update.effective_user
    if req_user and not req_user.is_bot:
        user = User.query.get_by_id(req_user.id)
        if user:
            context.bot.send_message(update.message.chat_id, f"Hello {user.name}!")
        else:
            context.bot.send_message(update.message.chat_id, f"Welcome Welcome!")
            user = User(id=req_user.id, name=req_user.name, username=req_user.username)
            session.add(user)
            session.commit()

start_handler = CommandHandler("start", start)
