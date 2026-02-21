import httpx
from bs4 import BeautifulSoup
from typing import Optional

class WebsiteScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    async def scrape_text(self, url: str) -> Optional[str]:
        """
        Scrape text content from a website using httpx and BeautifulSoup.
        """
        if not url:
            return None

        if not url.startswith("http"):
            url = "https://" + url

        try:
            async with httpx.AsyncClient(follow_redirects=True, timeout=10.0) as client:
                response = await client.get(url, headers=self.headers)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, 'html.parser')

                # Remove script and style elements
                for script in soup(["script", "style", "nav", "footer"]):
                    script.extract()

                # Get text
                text = soup.get_text(separator=' ', strip=True)

                # Truncate if too long (e.g., 5000 chars)
                return text[:5000]

        except Exception as e:
            print(f"Scraping Error for {url}: {e}")
            return None
