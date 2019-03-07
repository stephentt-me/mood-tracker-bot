"""Add new record about user mood today
"""
import re
from collections import namedtuple

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters

from src.system.acl import restrict_admin, must_be_user
from src.system.database import session_scope
from src.domains.record import record_new_mood

Mood = namedtuple("Mood", ["value", "description"])

MOODS = [
    Mood(6, "joyful, happy, relaxed, silly, content, great"),
    Mood(5, "productive, active, energetic, motivated"),
    Mood(4, "average, normal, uneventful, good"),
    Mood(3, "sick, tired, lazy, dull, unmotivated, bored"),
    Mood(2, "sad, lonely, numb, depressed, insecure"),
    Mood(1, "angry, frustrated, anxious, grumpy"),
]

COLOR = [
    "🔴",  # red
    "🟠",  # orange
    "🔵",  # blue
    "🟣",  # purple
    "⚫",  # black
    "⚪",  # white
]

DESC_MOODS = [[f"I feel {x.description}"] for x in MOODS]


@must_be_user
@session_scope
def record(update: Update, context: CallbackContext, session):
    context.bot.send_message(
        update.message.chat_id,
        "Hi, how are you today?",
        reply_markup=ReplyKeyboardMarkup(DESC_MOODS, one_time_keyboard=True),
    )


@must_be_user
@session_scope
def i_feel(update: Update, context: CallbackContext, session):
    user_mood_desc = context.match.groupdict()["desc"]
    value = None
    for mood in MOODS:
        if mood.description == user_mood_desc:
            value = mood.value
    if value:
        record_new_mood(update.effective_user.id, value)
        context.bot.send_message(update.message.chat_id, "Thank you. I got it.")
        return
    context.bot.send_message(
        update.message.chat_id,
        "Can you choose a value from the keyboard please.",
        reply_markup=ReplyKeyboardMarkup(DESC_MOODS, one_time_keyboard=True),
    )


record_handler = CommandHandler("today", record)
i_feel_handler = MessageHandler(
    Filters.regex(re.compile(r"^I feel (?P<desc>.+)", re.IGNORECASE)), i_feel
)
