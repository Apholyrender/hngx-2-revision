from uuid import UUID

from pydantic import BaseModel


class Account(BaseModel):
    name: str


class AccountProfile(Account):
    user_id: UUID


class Message(BaseModel):
    message: str

