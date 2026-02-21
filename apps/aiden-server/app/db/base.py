# Import all the models, so that Base has them before being
# imported by Alembic
from app.models.base import Base  # noqa
from app.models.prospect import Prospect  # noqa
from app.models.campaign import Campaign  # noqa
from app.models.email_draft import EmailDraft  # noqa
