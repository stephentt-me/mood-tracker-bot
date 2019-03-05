from .start import start_hanlder
from .ping import ping_handler
from .log_expense import log_expense_handler

def register_handler(dispatcher):
    dispatcher.add_handler(start_hanlder)
    dispatcher.add_handler(ping_handler)
    dispatcher.add_handler(log_expense_handler)
