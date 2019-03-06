from datetime import datetime

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from src.system.acl import restrict_admin, must_be_user
from src.domains.chart import visualize_user_expense
from src.system.database import session_scope

@restrict_admin
@must_be_user
@session_scope
def ping(update: Update, context: CallbackContext, session):
    user_id = update.effective_user.id
    chartpath = visualize_user_expense(user_id, session)
    context.bot.send_photo(
        update.message.chat_id, 
        open(chartpath, "rb"), 
        caption=f"Generate at {str(datetime.now())}",
    )

ping_handler = CommandHandler("ping", ping)
