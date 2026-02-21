from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base


class EmailDraft(Base):
    id = Column(Integer, primary_key=True, index=True)
    prospect_id = Column(Integer, ForeignKey("prospect.id"), nullable=False)
    campaign_id = Column(Integer, ForeignKey("campaign.id"), nullable=True)  # Optional association

    subject = Column(String, nullable=True)
    body_text = Column(Text, nullable=False)
    template_type = Column(String, default="AIDA")  # AIDA, PAS, etc.

    status = Column(String, default="DRAFT")  # DRAFT, APPROVED, SENT

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    prospect = relationship("Prospect")
    campaign = relationship("Campaign")
