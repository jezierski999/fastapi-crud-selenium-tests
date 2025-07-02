from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)      # Unique user ID (primary key)
    name = Column(String, index=True)                       # User name
    email = Column(String, unique=True, index=True)         # User email (must be unique)