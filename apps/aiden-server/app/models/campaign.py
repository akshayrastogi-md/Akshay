from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func

from app.models.base import Base


class Campaign(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String, default="DRAFT")  # DRAFT, ACTIVE, PAUSED, COMPLETED

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
