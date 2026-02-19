from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class EmailDraftBase(BaseModel):
    subject: Optional[str] = None
    body_text: str
    template_type: str = "AIDA"
    status: str = "DRAFT"

class EmailDraftCreate(EmailDraftBase):
    prospect_id: int
    campaign_id: Optional[int] = None

class EmailDraftUpdate(EmailDraftBase):
    body_text: Optional[str] = None
    status: Optional[str] = None

class EmailDraftInDBBase(EmailDraftBase):
    id: int
    prospect_id: int
    campaign_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

class EmailDraft(EmailDraftInDBBase):
    pass
