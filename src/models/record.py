import datetime
import uuid

from sqlalchemy import Column, Integer, DateTime, String, ForeignKey

from src.models.base import Base
from src.system.database_uuid import UUID

class Record(Base):
    __tablename__ = "records"
    
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    message_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    amount = Column(Integer, nullable=False)
    tag = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    note = Column(String)

    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    def __init__(self, **kwargs):
        self.id = uuid.uuid4()
        super(Record, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.amount} {self.tag} at {self.timestamp}"
