from typing import Optional, Dict, Any

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

    def generate_email_draft(self, research_data: Dict[str, Any], template_type: str = "AIDA") -> str:
        """
        Generate a cold email draft based on research data and a template type.
        """

        prospect_name = research_data.get("linkedin", {}).get("headline", "Prospect")
        company_news = research_data.get("company_news", [])
        news_snippet = company_news[0]["snippet"] if company_news else "recent industry trends"
        tech_stack = ", ".join(research_data.get("tech_stack", []))

        prompt = f"""
        You are an expert SDR. Write a personalized cold email to a prospect.

        Prospect Info:
        - Name/Title: {prospect_name}
        - Recent News: {news_snippet}
        - Tech Stack: {tech_stack}

        Template Framework: {template_type} (Attention, Interest, Desire, Action)

        Goal: Book a meeting to discuss our AI SDR solution 'AIDEN'.
        Tone: Professional, direct, not salesy.
        """

        if not self.client:
            # return mock response
            return f"""Subject: Quick question about {tech_stack}

Hi {prospect_name.split(' ')[0]},

I saw that you recently made news with "{news_snippet}". Congrats!

Noticed you are using {tech_stack}. Many teams using this stack struggle with consistent outbound pipeline.

AIDEN is an AI SDR that automates research and outreach.

Open to a 10-min chat next Tuesday?

Best,
[Your Name]
"""

        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=1000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error generating email: {str(e)}"
