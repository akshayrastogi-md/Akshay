from typing import Any, Dict, List, Optional
import requests
from app.core.config import settings

class ApolloService:
    def __init__(self):
        self.api_key = settings.APOLLO_API_KEY
        self.base_url = "https://api.apollo.io/v1"

    def search_people(self, query: str) -> List[Dict[str, Any]]:
        if not self.api_key:
            return []

        url = f"{self.base_url}/mixed_people/search"
        headers = {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache"
        }
        payload = {
            "api_key": self.api_key,
            "q_keywords": query,
            "page": 1,
            "per_page": 5
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json().get("people", [])
        except Exception as e:
            print(f"Apollo API Error: {e}")
            return []

    def enrich_person(self, email: str) -> Optional[Dict[str, Any]]:
        if not self.api_key:
            return None

        url = f"{self.base_url}/people/match"
        headers = {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache"
        }
        payload = {
            "api_key": self.api_key,
            "email": email
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 429:
                print("Apollo API Rate Limit Exceeded")
                return None
            response.raise_for_status()
            return response.json().get("person")
        except Exception as e:
            print(f"Apollo Enrichment Error: {e}")
            return None
