from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.sql import func

from app.models.base import Base


class Prospect(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)
    company_name = Column(String, nullable=True)

    # Research data (stored as JSON string or text for now, could be JSONB)
    research_summary = Column(Text, nullable=True)

    # Status
    status = Column(String, default="NEW")  # NEW, RESEARCHED, IN_SEQUENCE, REPLIED

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
