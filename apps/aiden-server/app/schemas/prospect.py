from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr

class ProspectBase(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    linkedin_url: Optional[str] = None
    company_name: Optional[str] = None

class ProspectCreate(ProspectBase):
    pass

class ProspectUpdate(ProspectBase):
    email: Optional[EmailStr] = None
    status: Optional[str] = None
    research_summary: Optional[str] = None

class ProspectInDBBase(ProspectBase):
    id: int
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

class Prospect(ProspectInDBBase):
    pass
