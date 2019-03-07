import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from src.system.database_uuid import UUID
from src.models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String)
    
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
