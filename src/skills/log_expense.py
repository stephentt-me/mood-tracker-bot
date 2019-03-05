import logging
from datetime import datetime

from telegram import Update
from telegram.ext import CallbackContext

from telegram.ext import MessageHandler
from telegram.ext.filters import Filters

from src.models.record import Record
from src.system.database import session_scope

MESSAGE_PATTERN = r"^(?P<amount>\d+(\.\d)?[kKmM]?) (?P<tag>\w+)(?P<time> \@\d[dw]+)?(?P<note> [\w ]+)?$"

@session_scope
def log_expense(update: Update, context: CallbackContext, session):
    data = context.match.groupdict()
    # Handle the 'k' or 'm' sufix in amount
    if data["amount"].endswith(("k", "K")):
        amount = float(data["amount"][:-1]) * 1_000
    elif data["amount"].endswith(("m", "M")):
        amount = float(data["amount"][:-1]) * 1_000_000
    else:
        amount = float(data["amount"])
    tag = data["tag"]
    timestamp = datetime.now()  # XXX
    note = data.get("note")

    logging.debug(f"Got {amount} {tag} {timestamp} {note}.")
    record = Record(
        user_id=update.effective_user.id,
        message_id=update.message.message_id,
        amount=amount,
        tag=tag,
        timestamp=timestamp,
        note=note,
    )
    session.add(record)
    session.commit()
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=f"👌",
        disable_notification=True,
        # reply_to_message_id=update.message.message_id,
    )

log_expense_handler = MessageHandler(Filters.regex(MESSAGE_PATTERN), log_expense)
