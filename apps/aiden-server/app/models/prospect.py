from sqlalchemy import Column, Integer, String, DateTime, Text, JSON
from sqlalchemy.sql import func

from app.models.base import Base


class Prospect(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)
    company_name = Column(String, nullable=True)

    # Research data
    research_summary = Column(Text, nullable=True)
    research_data = Column(JSON, nullable=True)  # Store structured data from LinkedIn, News, etc.
    icp_score = Column(Integer, default=0)

    # Status
    status = Column(String, default="NEW")  # NEW, RESEARCHED, DRAFTED, IN_SEQUENCE, REPLIED

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
