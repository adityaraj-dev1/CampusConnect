from sqlalchemy import create_engine
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL:  str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
engine = create_engine(settings.DATABASE_URL)

from sqlalchemy import text

with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.scalar())

# session management
from sqlalchemy.orm import sessionmaker
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit = False
)    

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
