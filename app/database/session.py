from sqlalchemy.orm import sessionmaker
from app.database.config import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
