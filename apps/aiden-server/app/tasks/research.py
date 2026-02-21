import asyncio
from sqlalchemy import select
from sqlalchemy.exc import OperationalError

from app.core.celery_app import celery_app
from app.services.research import ResearchService
from app.db.session import SessionLocal
from app.models.prospect import Prospect

async def _research_prospect_async(prospect_id: int):
    print(f"Starting research for prospect ID {prospect_id}...")

    async with SessionLocal() as db:
        result = await db.execute(select(Prospect).where(Prospect.id == prospect_id))
        prospect = result.scalars().first()

        if not prospect:
            print(f"Prospect ID {prospect_id} not found.")
            return None

        research_service = ResearchService()

        # Prepare input data
        input_data = {
            "linkedin_url": prospect.linkedin_url,
            "company_name": prospect.company_name
        }

        # Gather data
        try:
            research_data = await research_service.conduct_comprehensive_research(input_data)
        except Exception as e:
            # Re-raise to trigger Celery retry
            raise e

        # Update Prospect
        prospect.research_data = research_data
        prospect.research_summary = f"Found {len(research_data.get('company_news', []))} news items and {len(research_data.get('tech_stack', []))} technologies."
        prospect.status = "RESEARCHED"
        prospect.icp_score = 85 # Mock score logic

        db.add(prospect)
        await db.commit()
        await db.refresh(prospect)

        print(f"Research complete for {prospect.email}. Status updated to RESEARCHED.")
        return prospect.research_data

@celery_app.task(
    autoretry_for=(Exception, OperationalError),
    retry_backoff=True,
    retry_backoff_max=600,
    retry_jitter=True,
    max_retries=3
)
def research_prospect(prospect_id: int):
    """
    Research a prospect by ID and update the database.
    Retries on network/DB errors.
    """
    return asyncio.run(_research_prospect_async(prospect_id))
