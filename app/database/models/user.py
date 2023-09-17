from sqlalchemy.orm import Mapped
from app.database.db import Base
from app.database.models.common import UUIDMixin


class User(UUIDMixin, Base):
    __tablename__ = "users"

    name: Mapped[str]

    def __repr__(self):
        return f"<User (id: {self.id})>"

