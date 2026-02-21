import asyncio
from typing import Dict, Any, List

from app.services.proxycurl import ProxycurlService
from app.services.apollo import ApolloService
from app.services.harvest.search import DuckDuckGoService
from app.services.harvest.scraper import WebsiteScraper

class ResearchService:
    def __init__(self):
        # Premium Services
        self.proxycurl = ProxycurlService()
        self.apollo = ApolloService()

        # Cheap/Free Services
        self.ddg = DuckDuckGoService()
        self.scraper = WebsiteScraper()

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
        Strategy:
        1. Try DuckDuckGo News (Free)
        2. Fallback to Mock (or other paid APIs in future)
        """
        if not company_name:
            return []

        # 1. Try Free Source
        print(f"Searching news for {company_name} via DDG...")
        news = self.ddg.find_recent_news(company_name)
        if news:
            print(f"Found {len(news)} news items via DDG.")
            return news

        # 2. Mock Fallback
        await asyncio.sleep(1)
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

    async def waterfall_research(self, prospect_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Cost-Effective Waterfall Enrichment Strategy:
        1. Find LinkedIn URL via DDG if missing.
        2. Scrape Company Website for text (Free).
        3. Search News via DDG (Free).
        4. (Optional) Use Paid APIs if critical data missing.
        """
        company_name = prospect_data.get("company_name")
        first_name = prospect_data.get("first_name")
        last_name = prospect_data.get("last_name")
        website_url = prospect_data.get("website_url") # Assuming this might be passed

        # 1. Find LinkedIn URL if missing
        if not prospect_data.get("linkedin_url"):
            print("LinkedIn URL missing. Searching via DDG...")
            found_url = self.ddg.find_linkedin_url(f"{first_name} {last_name}", company_name)
            if found_url:
                prospect_data["linkedin_url"] = found_url
                print(f"Found LinkedIn URL: {found_url}")

        # 2. Scrape Website
        website_text = None
        if website_url:
             print(f"Scraping website: {website_url}")
             website_text = await self.scraper.scrape_text(website_url)
        elif company_name:
             # Try to guess or search website (omitted for brevity, assume passed or mocked)
             pass

        # 3. Parallel Gather (LinkedIn Profile + News + Stack)
        # Note: LinkedIn gathering uses Proxycurl (Paid) or Mock.
        # Ideally we would scrape public profile here for free tier, but that's complex to implement reliably.
        linkedin_url = prospect_data.get("linkedin_url")

        linkedin_data, news_data, tech_stack = await asyncio.gather(
            self.gather_linkedin_data(linkedin_url),
            self.gather_company_news(company_name),
            self.gather_tech_stack(company_name)
        )

        return {
            "linkedin": linkedin_data,
            "company_news": news_data,
            "tech_stack": tech_stack,
            "website_text": website_text,
            "sources": ["DuckDuckGo", "WebsiteScraper", "Proxycurl" if self.proxycurl.api_key else "Mock"]
        }

    async def conduct_comprehensive_research(self, prospect_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Orchestrate the research process using the waterfall strategy.
        """
        return await self.waterfall_research(prospect_data)
