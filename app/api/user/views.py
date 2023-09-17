from uuid import UUID

from fastapi import APIRouter

from app.api.user.schemas import Account, AccountProfile, Message
from app.api.user.services import UserService
from app.database.db import AnSession

router = APIRouter(prefix="/api/v1")


@router.get("/users", response_model=list[AccountProfile], status_code=200)
async def read_accounts(session: AnSession):
    user_services = UserService(session)
    return await user_services.get_all_users()


@router.get("/users/{user_id}")
async def read_an_account(user_id: UUID, session: AnSession):
    user_services = UserService(session)
    return await user_services.get_single_user(user_id)


@router.post("/users", response_model=AccountProfile, status_code=201)
async def create_account(request: Account, session: AnSession):
    user_services = UserService(session)
    return await user_services.create_user(request)


@router.put("/users/{user_id}", response_model=AccountProfile, status_code=200)
async def update_account(user_id: UUID, request: Account, session: AnSession):
    user_services = UserService(session)
    return await user_services.update_user(user_id=user_id, user=request)


@router.delete("/users/{user_id}", response_model=Message, status_code=200)
async def delete_account(user_id: UUID, session: AnSession):
    user_services = UserService(session)
    await user_services.delete_user(user_id)
    return {"message": "User deleted Successfully"}
