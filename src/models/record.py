import uuid
import datetime

from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String

from src.system.database_uuid import UUID
from src.models.base import Base

class Record(Base):
    __tablename__ = "records"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    value = Column(Integer, nullable=False)

    created_at = Column(Date, default=datetime.date.today, nullable=False)

    def __init__(self, **kwargs):
        super(Record, self).__init__(**kwargs)
