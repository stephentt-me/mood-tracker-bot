import os
from functools import wraps
import logging

from telegram.bot import Bot
from telegram.ext import CallbackContext

def restrict_admin(func):
    @wraps(func)
    def inner(update: Bot, context: CallbackContext, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id != os.getenv("ONWER_ID"):
            return func(update, context, *args, **kwargs)
        logging.info(f"A request from {user_id} not belong to owner has been denied.")
        return
    return inner

def must_be_user(func):
    @wraps(func)
    def inner(update: Bot, context: CallbackContext, *args, **kwargs):
        return func(update, context, *args, **kwargs)
    return inner
