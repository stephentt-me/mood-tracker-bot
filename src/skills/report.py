
from sqlalchemy.sql import func
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from src.models.record import Record
from src.system.database import session_scope

@session_scope
def report(update: Update, context: CallbackContext, session):
    user_id = update.effective_user.id

    result = session.query(
        func.sum(Record.amount).label("amount"),
        func.count(Record.id).label("number"),
    ) \
        .filter_by(user_id=user_id) \
        .first()
    context.bot.send_message(update.message.chat_id, f"You have {result.amount} in the balance. Recorded from {result.number} records.")

report_handler = CommandHandler("report", report)
