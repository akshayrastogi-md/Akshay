import asyncio
from sqlalchemy import select

from app.core.celery_app import celery_app
from app.services.llm import LLMService
from app.db.session import SessionLocal
from app.models.prospect import Prospect
from app.models.email_draft import EmailDraft

async def _generate_email_draft_async(prospect_id: int, template_type: str):
    print(f"Generating email draft for prospect ID {prospect_id} using {template_type}...")

    async with SessionLocal() as db:
        result = await db.execute(select(Prospect).where(Prospect.id == prospect_id))
        prospect = result.scalars().first()

        if not prospect:
            print(f"Prospect ID {prospect_id} not found.")
            return None

        if not prospect.research_data:
            print(f"Prospect ID {prospect_id} has no research data. Cannot generate email.")
            return None

        llm_service = LLMService()
        # LLMService is synchronous for now, but we run it inside async task.
        # This blocks the loop, but it's fine for now as we are the only task in this worker process.
        email_body = llm_service.generate_email_draft(prospect.research_data, template_type)

        # Create EmailDraft
        draft = EmailDraft(
            prospect_id=prospect.id,
            subject=f"Question about {prospect.company_name}",
            body_text=email_body,
            template_type=template_type,
            status="DRAFT"
        )

        db.add(draft)
        prospect.status = "DRAFTED"
        db.add(prospect)

        await db.commit()
        await db.refresh(draft)

        print(f"Email draft generated for {prospect.email}. ID: {draft.id}")
        return draft.id

@celery_app.task
def generate_email_draft(prospect_id: int, template_type: str = "AIDA"):
    """
    Generate an email draft for a prospect.
    """
    return asyncio.run(_generate_email_draft_async(prospect_id, template_type))
