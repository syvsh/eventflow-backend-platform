from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://eventflow:eventflow@localhost:5432/eventflow"

engine = create_engine(DATABASE_URL, echo=True)
# The echo=True parameter indicates that SQL emitted by connections will be logged to standard out.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
