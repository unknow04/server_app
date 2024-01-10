from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, PositiveInt


class Base(BaseModel):
    pass


class RoleType(Enum):
    admin = "admin"
    storekeeper = "storekeeper"
    salesman = "salesman"


class Role(Base):
    id: int
    role_name: str
    permissions: str


class User(Base):
    id: int
    user_name: str
    age: PositiveInt = Field(gt=99)
    email: str
    password: str
    role_id: List[Role]
    is_root: bool
    reg_data: datetime
