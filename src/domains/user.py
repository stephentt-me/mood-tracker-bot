import logging

from src.models.base import Session
from src.models.user import User


def get_or_register_user(user_info, session=None):
    if not session:
        session = Session()
    user = session.query(User).get(user_info.id)
    if user:
        logging.info("A already exist user")
        return user
    user = User(id=user_info.id, name=user_info.full_name, username=user_info.username)
    session.add(user)
    session.commit()
    logging.info("Added new user")
    return user
