import os
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel


DATABASE_URL = os.getenv("DATABASE_URL")

# Async engine for Neon/PostgreSQL; pool size kept modest for serverless
engine = create_async_engine(
    DATABASE_URL or "postgresql+asyncpg://user:password@localhost:5432/todos",
    echo=False,
    future=True,
)

async_session_factory = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def init_db() -> None:
    """Create tables on startup."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session
