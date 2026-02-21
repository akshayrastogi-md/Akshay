from typing import List, Dict, Any
from duckduckgo_search import DDGS

class DuckDuckGoService:
    def __init__(self):
        self.ddgs = DDGS()

    def find_linkedin_url(self, name: str, company: str) -> str:
        """
        Search for a LinkedIn profile URL.
        """
        query = f"site:linkedin.com/in/ {name} {company}"
        try:
            results = self.ddgs.text(query, max_results=1)
            if results:
                return results[0]['href']
        except Exception as e:
            print(f"DDG Search Error: {e}")
        return ""

    def find_recent_news(self, company: str) -> List[Dict[str, Any]]:
        """
        Search for recent news about the company.
        """
        query = f"{company} news funding launch partnership"
        news_items = []
        try:
            results = self.ddgs.news(query, max_results=3)
            if results:
                for res in results:
                    news_items.append({
                        "title": res.get("title"),
                        "source": res.get("source"),
                        "date": res.get("date"),
                        "snippet": res.get("body"),
                        "url": res.get("url")
                    })
        except Exception as e:
            print(f"DDG News Error: {e}")
        return news_items
