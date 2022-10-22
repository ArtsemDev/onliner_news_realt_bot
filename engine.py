from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from config import CONFIG


DATABASE_SYNC_URL = f'sqlite:///{CONFIG.get("DATABASE")}'
DATABASE_ASYNC_URL = f'sqlite+aiosqlite:///{CONFIG.get("DATABASE")}'

ENGINE = create_async_engine(DATABASE_ASYNC_URL)

def create_async_session(func):
    async def wrapper(**kwargs):
        async with AsyncSession(bind=ENGINE) as session:
            return await func(**kwargs, session=session)
    return wrapper
