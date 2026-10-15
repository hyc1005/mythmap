from collections.abc import Generator
from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .config import settings

@lru_cache(maxsize=1)
def session_factory():
    engine = create_engine(settings.database_url, pool_pre_ping=True) if settings.database_url else None
    return sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_db() -> Generator[Session, None, None]:
    with session_factory()() as session:
        yield session
