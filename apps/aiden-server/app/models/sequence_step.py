from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base


class SequenceStep(Base):
    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaign.id"), nullable=False)
    step_number = Column(Integer, nullable=False)
    delay_days = Column(Integer, default=2)  # Days to wait after previous step
    template_type = Column(String, default="AIDA")  # Template type for this step
    prompt_template = Column(Text, nullable=True)   # Custom prompt for the LLM

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    campaign = relationship("Campaign", back_populates="steps")
