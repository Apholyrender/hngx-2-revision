from fastapi.exceptions import HTTPException
from sqlalchemy import delete, select, update

from app.api.user.schemas import Account, AccountProfile
from app.database.db import AnSession
from app.database.models.user import User as UserDb


class UserService:
    def __init__(self, session: AnSession = None):
        self.session = session

    async def create_user(self, user: Account):
        user = UserDb(name=user.name)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        account_profile = AccountProfile(user_id=user.id, name=user.name)

        return account_profile

    async def get_all_users(self):
        statement = select(UserDb)
        users = (await self.session.execute(statement)).scalars().all()

        account_profiles = [
            AccountProfile(user_id=user.id, name=user.name) for user in users
        ]

        return account_profiles

    async def get_single_user(self, user_id):
        select_statement = select(UserDb).where(UserDb.id == user_id)
        user = (await self.session.execute(select_statement)).scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        account_profile = AccountProfile(user_id=user.id, name=user.name)

        return account_profile

    async def update_user(self, user_id, user: Account):
        update_statement = (
            update(UserDb)
            .where(UserDb.id == user_id)
            .values(name=user.name)
            .returning(UserDb)
        )
        result = (await self.session.execute(update_statement)).scalar_one_or_none()

        if result is None:
            raise HTTPException(status_code=404, detail="User not found")
        return AccountProfile(user_id=result.id, name=result.name)

    async def delete_user(self, user_id):
        delete_statement = delete(UserDb).where(UserDb.id == user_id).returning(UserDb)
        result = (await self.session.execute(delete_statement)).scalar_one_or_none()

        if result is None:
            raise HTTPException(status_code=404, detail="User not found")
