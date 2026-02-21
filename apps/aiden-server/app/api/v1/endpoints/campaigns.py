from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.models.campaign import Campaign as CampaignModel
from app.models.sequence_step import SequenceStep as SequenceStepModel
from app.schemas.campaign import Campaign, CampaignCreate

router = APIRouter()

@router.get("/", response_model=List[Campaign])
async def read_campaigns(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """
    Retrieve campaigns.
    """
    # Use selectinload to eagerly load the steps relationship
    result = await db.execute(
        select(CampaignModel)
        .options(selectinload(CampaignModel.steps))
        .offset(skip)
        .limit(limit)
    )
    campaigns = result.scalars().all()
    return campaigns

@router.post("/", response_model=Campaign)
async def create_campaign(
    *,
    db: AsyncSession = Depends(deps.get_db),
    campaign_in: CampaignCreate,
) -> Any:
    """
    Create new campaign with steps.
    """
    campaign = CampaignModel(
        name=campaign_in.name,
        description=campaign_in.description,
        status=campaign_in.status
    )
    db.add(campaign)
    await db.flush()
    await db.commit()  # Commit to get ID
    await db.refresh(campaign)

    if campaign_in.steps:
        for step_data in campaign_in.steps:
            step = SequenceStepModel(
                campaign_id=campaign.id,
                step_number=step_data.step_number,
                delay_days=step_data.delay_days,
                template_type=step_data.template_type,
                prompt_template=step_data.prompt_template
            )
            db.add(step)
        await db.commit()

    # Reload with steps
    result = await db.execute(
        select(CampaignModel)
        .options(selectinload(CampaignModel.steps))
        .where(CampaignModel.id == campaign.id)
    )
    return result.scalars().first()

@router.get("/{id}", response_model=Campaign)
async def read_campaign(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get campaign by ID.
    """
    result = await db.execute(
        select(CampaignModel)
        .options(selectinload(CampaignModel.steps))
        .where(CampaignModel.id == id)
    )
    campaign = result.scalars().first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign
