from typing import List, Any, Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.models.prospect import Prospect as ProspectModel
from app.models.email_draft import EmailDraft as EmailDraftModel
from app.schemas.prospect import Prospect, ProspectCreate
from app.schemas.email_draft import EmailDraft
from app.tasks.research import research_prospect
from app.tasks.email_generation import generate_email_draft

router = APIRouter()

@router.get("/", response_model=List[Prospect])
async def read_prospects(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """
    Retrieve prospects.
    """
    result = await db.execute(select(ProspectModel).offset(skip).limit(limit))
    prospects = result.scalars().all()
    return prospects


@router.post("/", response_model=Prospect)
async def create_prospect(
    *,
    db: AsyncSession = Depends(deps.get_db),
    prospect_in: ProspectCreate,
) -> Any:
    """
    Create new prospect.
    """
    # Check if prospect exists
    result = await db.execute(
        select(ProspectModel).where(ProspectModel.email == prospect_in.email)
    )
    existing_prospect = result.scalars().first()
    if existing_prospect:
        raise HTTPException(
            status_code=400,
            detail="The prospect with this email already exists in the system.",
        )

    prospect = ProspectModel(**prospect_in.model_dump())
    db.add(prospect)
    await db.commit()
    await db.refresh(prospect)
    return prospect

@router.post("/{id}/research", response_model=Dict[str, Any])
async def trigger_research(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """
    Trigger research for a prospect.
    """
    result = await db.execute(select(ProspectModel).where(ProspectModel.id == id))
    prospect = result.scalars().first()
    if not prospect:
        raise HTTPException(status_code=404, detail="Prospect not found")

    # Trigger Celery task
    task = research_prospect.delay(id)
    return {"message": "Research started", "task_id": str(task.id)}

@router.post("/{id}/generate-email", response_model=Dict[str, Any])
async def trigger_email_generation(
    id: int,
    template: str = "AIDA",
    db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """
    Trigger email generation for a prospect.
    """
    result = await db.execute(select(ProspectModel).where(ProspectModel.id == id))
    prospect = result.scalars().first()
    if not prospect:
        raise HTTPException(status_code=404, detail="Prospect not found")

    # In a real app we might check status, but for dev flexibility we allow regeneration
    # if prospect.status == "NEW":
    #      raise HTTPException(status_code=400, detail="Prospect must be researched first")

    # Trigger Celery task
    task = generate_email_draft.delay(id, template)
    return {"message": "Email generation started", "task_id": str(task.id)}

@router.get("/{id}/emails", response_model=List[EmailDraft])
async def get_prospect_emails(
    id: int,
    db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """
    Get email drafts for a prospect.
    """
    result = await db.execute(select(EmailDraftModel).where(EmailDraftModel.prospect_id == id))
    emails = result.scalars().all()
    return emails
