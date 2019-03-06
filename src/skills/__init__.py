from .start import start_handler
from .ping import ping_handler
from .report import report_handler
from .log_expense import log_expense_handler

def register_handler(dispatcher):
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(ping_handler)
    dispatcher.add_handler(report_handler)
    dispatcher.add_handler(log_expense_handler)
