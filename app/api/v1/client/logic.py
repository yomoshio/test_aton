from fastapi import HTTPException, status
from typing import List
from app.api.v1.client.models import Client
from app.api.v1.user.models import User
from app.api.v1.client.schemas import ClientCreate
from app.api.v1.client.schemas import ClientUpdate
from passlib.context import CryptContext


async def create_client_logic(client: ClientCreate):
    client_obj = Client(
            lastname=client.lastname,
            firstname=client.firstname,
            fathername=client.fathername,
            birthday=client.birthday,
            inn=client.inn,
            user_fio_id=client.user_fio_id,
    )
    await client_obj.save()
    return client_obj





