from uuid import UUID
from fastapi import APIRouter, Query
from app.api.user.schemas import Account, AccountProfile, Message
from app.api.user.services import UserService
from app.database.db import AnSession

router = APIRouter(prefix="/api")

@router.get("/", response_model=list[AccountProfile], status_code=200)
async def read_accounts(session: AnSession):
    user_services = UserService(session)
    return await user_services.get_all_users()

@router.get("/user")
async def read_an_account(session: AnSession, user_id: UUID = Query(..., alias="user_id")):
    user_services = UserService(session)
    return await user_services.get_single_user(user_id)

@router.post("/")
async def create_account(request: Account, session: AnSession):
    user_services = UserService(session)
    return await user_services.create_user(request)

@router.put("/user")
async def update_account(request: Account, session: AnSession, user_id: UUID = Query(..., alias="user_id")):
    user_services = UserService(session)
    return await user_services.update_user(user_id=user_id, user=request)

@router.delete("/user")
async def delete_account(session: AnSession, user_id: UUID = Query(..., alias="user_id")):
    user_services = UserService(session)
    await user_services.delete_user(user_id)
    return {"message": "User deleted Successfully"}

