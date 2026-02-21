from typing import Optional, Dict, Any

from anthropic import Anthropic

from app.core.config import settings
from app.services.vector_db import VectorDBService


class LLMService:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.ANTHROPIC_API_KEY
        # If API key is present, initialize client
        self.client = Anthropic(api_key=self.api_key) if self.api_key else None
        self.vector_db = VectorDBService()

    def generate_research_summary(self, prospect_email: str) -> str:
        """
        Generate a research summary for a prospect using the LLM.
        """
        if not self.client:
            return "Anthropic API Key not configured. Cannot generate research summary."

        prompt = f"""
        You are an expert research analyst.
        I need a brief research summary for a prospect with email: {prospect_email}.

        Since I cannot browse the web right now, please provide a general summary of what you know about the domain/company
        associated with this email or general industry trends relevant to them.

        Keep it concise (under 100 words).
        """

        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=300,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error generating research summary: {str(e)}"

    def generate_email_draft(self, research_data: Dict[str, Any], template_type: str = "AIDA") -> str:
        """
        Generate a cold email draft based on research data and a template type.
        Uses RAG (Vector DB) to find successful examples if available.
        """

        prospect_name = research_data.get("linkedin", {}).get("headline", "Prospect")
        company_news = research_data.get("company_news", [])
        news_snippet = company_news[0]["snippet"] if company_news else "recent industry trends"
        tech_stack = ", ".join(research_data.get("tech_stack", []))

        # RAG: Fetch successful examples
        examples_context = ""
        try:
            # We search based on the news snippet or prospect title to find relevant past emails
            query = f"{template_type} email for {prospect_name} about {news_snippet}"
            similar_emails = self.vector_db.search_similar_emails(query)

            if similar_emails:
                examples_context = "\n\nHERE ARE EXAMPLES OF SUCCESSFUL PAST EMAILS (Use them as style reference):\n"
                for i, email in enumerate(similar_emails):
                    examples_context += f"Example {i+1}:\nSubject: {email['subject']}\nBody: {email['body']}\n---\n"
        except Exception as e:
            print(f"Vector DB Search failed (skipping RAG): {e}")

        prompt = f"""
        You are an expert SDR (Sales Development Rep). Write a hyper-personalized cold email.

        TARGET PROSPECT:
        - Name/Title: {prospect_name}
        - Recent News/Context: {news_snippet}
        - Tech Stack: {tech_stack}

        FRAMEWORK: {template_type} (Attention, Interest, Desire, Action)

        YOUR GOAL: Book a 15-minute meeting to introduce 'AIDEN', our AI Sales Agent.
        {examples_context}

        GUIDELINES:
        - Be direct and professional.
        - No fluff ("I hope this finds you well").
        - Mention their tech stack or news to show research.
        - Keep it under 150 words.
        """

        if not self.client:
            return "Anthropic API Key not configured. Cannot generate email draft."

        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=500,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error generating email: {str(e)}"
