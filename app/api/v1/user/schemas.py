from pydantic import BaseModel, constr
from typing import Optional, List


class UserBase(BaseModel):
    username: constr(min_length=1, max_length=50)
    fio: constr(min_length=1, max_length=50)


class UserCreate(UserBase):
    password: constr(min_length=8)
    is_admin: bool = False


class UserUpdate(BaseModel):
    username: Optional[constr(min_length=1, max_length=50)]
    fio: Optional[constr(min_length=1, max_length=50)]
    password: Optional[constr(min_length=8)]
    is_admin: Optional[bool]


class UserOut(UserBase):
    id: int
    is_admin: bool

    class Config:
        from_attributes = True


