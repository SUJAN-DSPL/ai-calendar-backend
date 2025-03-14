import json
from sqlalchemy.orm import Session
from app.models.google_credential import GoogleCredential
from app.utils.crypt import encrypt

class GoogleCredentialRepository:
    
    def __init__(self, db: Session):
        self.db = db
        
    def create_google_credential(self, token: object, user_id: int = 1):
        import json
from sqlalchemy.orm import Session
from app.models.google_credential import GoogleCredential
from app.utils.crypt import encrypt

class GoogleCredentialRepository:
    
    def __init__(self, db: Session):
        self.db = db
        
    def create_google_credential(self, token: dict, user_id: int = 1):
        try:
            token_json = json.dumps(token)
            encrypted_token = encrypt(token_json).decode()

            new_credential = GoogleCredential(user_token=encrypted_token, user_id=1)

            self.db.add(new_credential)
            self.db.commit()
            self.db.refresh(new_credential)

            return new_credential.to_dict() 
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error storing Google credentials: {str(e)}")

