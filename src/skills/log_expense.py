import logging
from datetime import datetime, timedelta

from telegram import Update
from telegram.ext import CallbackContext

from telegram.ext import MessageHandler
from telegram.ext.filters import Filters

from src.models.record import Record
from src.system.database import session_scope
from src.system.acl import must_be_user

AMOUNT_PATTERN = r"^(?P<amount>[\+-]?\d+(\.\d)?[kKmM]?) (?P<tag>\w+)(?P<time> \@\d)?(?P<note> [\w ]+)?$"

@must_be_user
@session_scope
def log_expense(update: Update, context: CallbackContext, session):
    data = context.match.groupdict()

    # Handle the 'k' or 'm' sufix in amount
    # The prefix +/- is comply with the float() function, no need handle
    if data["amount"].endswith(("k", "K")):
        amount = float(data["amount"][:-1]) * 1_000
    elif data["amount"].endswith(("m", "M")):
        amount = float(data["amount"][:-1]) * 1_000_000
    else:
        amount = float(data["amount"])

    timestamp = datetime.now()
    if data.get("time"):
        day = int(data["time"].strip()[1:])
        timestamp -= timedelta(days=day)

    tag = data["tag"]
    note = data["note"].strip() if data.get("note") else None

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
    )

log_expense_handler = MessageHandler(Filters.regex(AMOUNT_PATTERN), log_expense)
