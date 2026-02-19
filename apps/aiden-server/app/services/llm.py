from typing import Optional

from anthropic import Anthropic

from app.core.config import settings


class LLMService:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.ANTHROPIC_API_KEY
        # If API key is present, initialize client, otherwise mock
        self.client = Anthropic(api_key=self.api_key) if self.api_key else None

    def generate_research_summary(self, prospect_email: str) -> str:
        """
        Mock implementation for now.
        In production, this would use self.client.messages.create()
        """
        if not self.client:
            return f"[MOCK] Research summary for {prospect_email}: High growth startup, recently funded."

        # Real call (commented out for now until we have real API key and context)
        # response = self.client.messages.create(
        #     model="claude-3-5-sonnet-20240620",
        #     max_tokens=1000,
        #     messages=[
        #         {"role": "user", "content": f"Research prospect with email {prospect_email}."}
        #     ]
        # )
        # return response.content[0].text

        return f"[MOCK with Key] Research summary for {prospect_email}: High growth startup, recently funded."
