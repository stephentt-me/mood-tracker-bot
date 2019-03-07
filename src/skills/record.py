"""Add new record about user mood today
"""
import re

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters

from src.system.acl import restrict_admin, must_be_user
from src.system.database import session_scope

MOODS = [
    "joyful, happy, relaxed, silly, content, great",
    "productive, active, energetic, motivated",
    "average, normal, uneventful, good",
    "sick, tired, lazy, dull, unmotivated, bored",
    "sad, lonely, numb, depressed, insecure",
    "angry, frustrated, anxious, grumpy",
]

COLOR = [
    "🔴",  # red
    "🟠",  # orange
    "🔵",  # blue
    "🟣",  # purple
    "⚫",  # black
    "⚪",  # white
]


@must_be_user
@session_scope
def record(update: Update, context: CallbackContext, session):
    user_moods = [[f"I feel {x}."] for x in MOODS]
    context.bot.send_message(
        update.message.chat_id,
        "Hi, how are you today?",
        reply_markup=ReplyKeyboardMarkup(user_moods, one_time_keyboard=True),
    )


@must_be_user
@session_scope
def i_feel(update: Update, context: CallbackContext, session):
    context.bot.send_message(update.message.chat_id, "Thank you. I got it.")


record_handler = CommandHandler("today", record)
i_feel_handler = MessageHandler(
    Filters.regex(re.compile(r"^i feel", re.IGNORECASE)), i_feel
)
