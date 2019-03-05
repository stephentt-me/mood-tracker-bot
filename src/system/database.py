from functools import wraps

from sqlalchemy.exc import SQLAlchemyError, DBAPIError

from src.models.base import Session

def session_scope(func):
    @wraps(func)
    def inner(update, context):
        session = Session()
        try:
            func(update, context, session)
        except (SQLAlchemyError, DBAPIError) as e:
            session.rollback()
            raise e
        session.close()
        return
    return inner
