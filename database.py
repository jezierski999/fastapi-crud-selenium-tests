from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database URL format: "dialect:///relative/path"
SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"

# Create the SQLAlchemy engine with SQLite-specific settings
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # Required for SQLite in multi-threaded environments (e.g., FastAPI dev server)
)

# Session factory: creates new DB sessions when needed
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base class for all ORM models
Base = declarative_base()
