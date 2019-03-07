import logging

from src.models.base import Session
from src.models.record import Record

def record_new_mood(user_id, value, session=None):
    if not session:
        session = Session()
    record = Record(user_id=user_id, value=value)
    session.add(record)
    session.commit()
    return record
