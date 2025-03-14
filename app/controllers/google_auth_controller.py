import cherrypy
from app.services.google_auth_service import GoogleAuthService
from app.repositories.google_credential_repository import GoogleCredentialRepository
from app.utils.database import SessionLocal

class GoogleAuthController:
    
    def __init__(self):
        self.google_auth_service = GoogleAuthService()
        
    
    @cherrypy.expose("/")
    @cherrypy.tools.json_out()
    @cherrypy.tools.allow(methods=["GET"])
    def index(self):
       return {"response": "google-auth-route"} 
   

    @cherrypy.expose("calendar")
    @cherrypy.tools.allow(methods=["GET"])
    def calendar_login(self):
        raise cherrypy.HTTPRedirect(self.google_auth_service.get_google_auth_url("CALENDAR"))
    
    @cherrypy.expose("callback")
    @cherrypy.tools.json_out()
    def oauth_callback(self, **param):
        token = self.google_auth_service.retrieve_token(param["code"])
        
        db = SessionLocal()
        repo = GoogleCredentialRepository(db)
        credential = repo.create_google_credential(token)
        db.close()
        
        return credential