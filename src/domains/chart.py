import logging
import uuid
from typing import Tuple, Iterable

from sqlalchemy import func
import matplotlib.pyplot as plt

from src.models.record import Record


def load_user_expense(user_id: int, session) -> Tuple[Iterable, Iterable]:
    result = (
        session.query(Record.timestamp, func.sum(Record.amount))
        .group_by(Record.timestamp)
        .filter_by(user_id=user_id)
        .all()
    )
    return zip(*result)


def visualize_user_expense(user_id: int, session) -> str:
    timestamp, amount = load_user_expense(user_id, session)
    plt.plot(timestamp, amount)
    filename = f"/tmp/{str(uuid.uuid4())}.png"
    plt.savefig(filename)
    logging.info(f"A figure saved as {filename}.")
    return filename
