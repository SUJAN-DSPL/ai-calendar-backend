from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    
    def __init__(self, db:Session):
        self.db = db
        
    def create_user(self, name, email, google_id):
        new_user = User(name=name, email=email, google_id=google_id)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user.to_dict()