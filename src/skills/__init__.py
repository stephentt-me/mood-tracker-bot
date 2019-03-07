from .start import start_handler
from .ping import ping_handler
from .record import record_handler, i_feel_handler

def register_handler(dispatcher):
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(ping_handler)
    dispatcher.add_handler(record_handler)
    dispatcher.add_handler(i_feel_handler)
