# Import all the models, so that Base has them before being
# imported by Alembic
from app.models.base import Base as Base
from app.models.prospect import Prospect as Prospect
from app.models.campaign import Campaign as Campaign
from app.models.email_draft import EmailDraft as EmailDraft
from app.models.sequence_step import SequenceStep as SequenceStep
