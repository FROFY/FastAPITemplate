from app.dao.base import BaseDAO
from app.auth.models import User, Role
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc, text, func, join


class UsersDAO(BaseDAO[User]):
    model = User

    @classmethod
    async def get_users_custom(cls, session: AsyncSession):
        query = select(cls.model)
        result = await session.execute(query)
        return result.scalars().all()


class RoleDAO(BaseDAO[Role]):
    model = Role
