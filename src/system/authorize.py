import os
from functools import wraps

from telegram.bot import Bot
from telegram.ext import CallbackContext

def authorize(func):
    @wraps(func)
    def inner(update: Bot, context: CallbackContext):
        user_id = update.effective_user.id
        if user_id != os.getenv("ONWER_ID"):
            return func(update, context)
        # TODO: reply deny message
        return
    return inner
