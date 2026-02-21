import requests
from typing import Dict, Any, Optional
from app.core.config import settings

class ProxycurlService:
    def __init__(self):
        self.api_key = settings.PROXYCURL_API_KEY
        self.base_url = "https://nubela.co/proxycurl/api/v2"

    def get_profile(self, linkedin_url: str) -> Optional[Dict[str, Any]]:
        if not self.api_key:
            return None

        url = f"{self.base_url}/linkedin"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {
            "url": linkedin_url,
            "fallback_to_cache": "on-error",
            "use_cache": "if-present",
            "skills": "include",
            "inferred_salary": "include",
            "personal_email": "include",
            "personal_contact_number": "include",
            "twitter_profile_id": "include",
            "facebook_profile_id": "include",
            "github_profile_id": "include",
            "extra": "include",
        }

        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Proxycurl API Error: {e}")
            return None
