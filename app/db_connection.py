import os
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

db_engine = create_async_engine(os.environ.get("DATABASE_URL"), echo=True)


async def db_init():
    try:
        async with db_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
    except Exception as e:
        print(f"Error initializing database: {str(e)}")


@asynccontextmanager
async def db_get_session() -> AsyncSession:
    async_session = sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
