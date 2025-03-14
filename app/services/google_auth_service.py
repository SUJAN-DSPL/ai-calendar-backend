from config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REDIRECT_URI, GOOGLE_CALENDAR_SCOPE, GOOGLE_PROFILE_SCOPE
from urllib.parse import urlencode, parse_qs
import requests

class GoogleAuthService:
    
    def get_google_auth_url(self, type: str):
        scope = {
            "CALENDAR": GOOGLE_CALENDAR_SCOPE,
            "PROFILE": GOOGLE_PROFILE_SCOPE
         }.get(type, GOOGLE_PROFILE_SCOPE)

        params = {
            "client_id": GOOGLE_CLIENT_ID,
            "redirect_uri": GOOGLE_REDIRECT_URI,
            "response_type": "code",
            "scope": scope,
            "access_type": "offline",
            "prompt": "consent"
        }
        
        auth_url = f"https://accounts.google.com/o/oauth2/auth?{urlencode(params)}"
        
        return auth_url;
    
    def retrieve_token(self, code: str):
        token_url = "https://oauth2.googleapis.com/token"
        
        data = {
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": GOOGLE_REDIRECT_URI
        }
        
        print(data)
        
        response = requests.post(token_url, data=data).json()
        
        return response