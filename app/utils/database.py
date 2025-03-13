import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

def get_mysql_db_url():
    return DATABASE_URL

engine = create_engine(get_mysql_db_url(), echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()