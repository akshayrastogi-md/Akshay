import asyncio
from typing import Dict, Any, List

from app.services.proxycurl import ProxycurlService
from app.services.apollo import ApolloService

class ResearchService:
    def __init__(self):
        self.proxycurl = ProxycurlService()
        self.apollo = ApolloService()

    async def gather_linkedin_data(self, linkedin_url: str) -> Dict[str, Any]:
        """
        Gather data from LinkedIn via Proxycurl or fallback to mock.
        """
        if not linkedin_url:
            return {}

        # Use Real API if Key is present
        if self.proxycurl.api_key:
            data = self.proxycurl.get_profile(linkedin_url)
            if data:
                return data

        # Fallback Mock
        await asyncio.sleep(1)
        return {
            "profile_url": linkedin_url,
            "headline": "Founder & CEO at TechStart",
            "summary": "Building the future of B2B SaaS.",
            "experience": [
                {
                    "title": "Founder",
                    "company": "TechStart",
                    "date_range": "2023 - Present",
                    "description": "Leading the team."
                },
                {
                    "title": "VP Sales",
                    "company": "BigCorp",
                    "date_range": "2018 - 2023",
                    "description": "Scaled revenue from $1M to $10M."
                }
            ],
            "recent_posts": [
                "Just launched our new feature!",
                "Hiring engineers in Bangalore."
            ]
        }

    async def gather_company_news(self, company_name: str) -> List[Dict[str, Any]]:
        """
        Simulate gathering company news via Google News or similar.
        """
        # Mock delay
        await asyncio.sleep(1)

        if not company_name:
            return []

        return [
            {
                "title": f"{company_name} raises Series A",
                "source": "TechCrunch",
                "date": "2024-01-15",
                "snippet": f"{company_name} has secured $5M in funding to expand its AI capabilities."
            },
            {
                "title": f"{company_name} partners with BigCorp",
                "source": "Business Wire",
                "date": "2023-11-20",
                "snippet": "Strategic partnership announced to deliver enterprise solutions."
            }
        ]

    async def gather_tech_stack(self, company_name: str) -> List[str]:
        """
        Simulate gathering tech stack via BuiltWith.
        """
        # Mock delay
        await asyncio.sleep(0.5)

        if not company_name:
            return []

        # Return random-ish stack based on name length just to vary it
        if len(company_name) % 2 == 0:
            return ["Salesforce", "Marketo", "AWS", "React"]
        else:
            return ["HubSpot", "Segment", "GCP", "Vue.js"]

    async def conduct_comprehensive_research(self, prospect_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Orchestrate the research process.
        """
        linkedin_url = prospect_data.get("linkedin_url")
        company_name = prospect_data.get("company_name")

        # Run in parallel
        linkedin_data, news_data, tech_stack = await asyncio.gather(
            self.gather_linkedin_data(linkedin_url),
            self.gather_company_news(company_name),
            self.gather_tech_stack(company_name)
        )

        return {
            "linkedin": linkedin_data,
            "company_news": news_data,
            "tech_stack": tech_stack,
            "sources": ["LinkedIn", "Google News", "BuiltWith"]
        }
