import logging
from datetime import datetime

from telegram.bot import Bot
from telegram.ext import CallbackContext

from telegram.ext import MessageHandler
from telegram.ext.filters import Filters

MESSAGE_PATTERN = r"^(?P<amount>\d+(\.\d)?k) (?P<tag>\w+)(?P<time> \@\d[dw]+)?(?P<comment> [\w ]+)?$"

def log_expense(update: Bot, context: CallbackContext):
    data = context.match.groupdict()
    amount = data["amount"]
    tag = data["tag"]
    now = datetime.now()
    comment = data.get("comment")
    logging.debug(f"Got {amount} {tag} {now} {comment}.")
    context.bot.send_message(
        chat_id=update.message.chat_id, 
        text=f"Roger that.",
        disable_notification=True, 
        reply_to_message_id=update.message.message_id
    )

log_expense_handler = MessageHandler(Filters.regex(MESSAGE_PATTERN), log_expense)
