from pydantic import BaseModel, constr
from typing import Optional, List


class ClientBase(BaseModel):
    lastname: constr(min_length=1, max_length=100)
    firstname: constr(min_length=1, max_length=100)
    fathername: constr(min_length=1, max_length=100)
    birthday: constr(min_length=1, max_length=50)
    inn: constr(min_length=1, max_length=50)
    user_fio_id: constr(min_length=1, max_length=100)

    class Config:
        from_attributes = True


class ClientCreate(ClientBase):
    pass


class ClientUpdate(BaseModel):
    is_working: constr(min_length=1, max_length=100)


class ClientInDB(ClientBase):
    id: int
    user_fio_id: str

    class Config:
        from_attributes = True


class ClientOut(ClientInDB):
    pass


class ClientResponse(BaseModel):
    total: int
    page: int
    per_page: int
    clients: List[ClientOut]