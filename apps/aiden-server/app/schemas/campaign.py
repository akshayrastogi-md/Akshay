from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict

# Sequence Step
class SequenceStepBase(BaseModel):
    step_number: int
    delay_days: int = 2
    template_type: str = "AIDA"
    prompt_template: Optional[str] = None

class SequenceStepCreate(SequenceStepBase):
    pass

class SequenceStepUpdate(SequenceStepBase):
    step_number: Optional[int] = None

class SequenceStepInDBBase(SequenceStepBase):
    id: int
    campaign_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

class SequenceStep(SequenceStepInDBBase):
    pass

# Campaign
class CampaignBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: str = "DRAFT"

class CampaignCreate(CampaignBase):
    steps: List[SequenceStepCreate] = []

class CampaignUpdate(CampaignBase):
    name: Optional[str] = None
    status: Optional[str] = None

class CampaignInDBBase(CampaignBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

class Campaign(CampaignInDBBase):
    steps: List[SequenceStep] = []
