from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.models.prospect import Prospect as ProspectModel
from app.schemas.prospect import Prospect, ProspectCreate

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
