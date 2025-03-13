from app.utils.database import Base
from sqlalchemy import Column, Integer, String, DateTime, func

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    google_id = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    