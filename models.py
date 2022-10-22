from typing import Optional, List

from sqlalchemy import Column, BigInteger, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import declarative_base

from engine import create_async_session


Base = declarative_base()


class User(Base):
    __tablename__: str = 'users'

    id = Column(BigInteger, primary_key=True)


class CRUDUser(object):

    @staticmethod
    @create_async_session
    async def add(user_id: int, session: AsyncSession = None) -> bool:
        user = User(id=user_id)
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_async_session
    async def all(session: AsyncSession = None) -> List[User]:
        users = await session.execute(
            select(User)
        )
        return [user[0] for user in users]
