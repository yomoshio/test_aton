from fastapi import HTTPException, status
from typing import List
from app.api.v1.user.models import User
from app.api.v1.client.models import Client
from app.api.v1.user.schemas import UserCreate
from app.api.v1.client.schemas import ClientUpdate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


async def create_user_logic(user: UserCreate):
    user_obj = User(
        fio=user.fio,
        username=user.username,
        password_hash=get_password_hash(user.password),
        is_admin=user.is_admin
    )
    await user_obj.save()
    return user_obj


async def get_user_clients_logic(current_user: User, page: int, size: int):
    query = Client.filter(user_fio=current_user.fio)
    clients = await query.offset((page - 1) * size).limit(size).all()
    if not clients:
        raise HTTPException(status_code=404, detail="No clients found for the current user")
    total = await query.count()
    return clients, total


async def update_user_logic(client_id: int, client: ClientUpdate):
    client_obj = await Client.get(id=client_id)
    if not client_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    if client.is_working:
        client_obj.is_working = client.is_working

    await client_obj.save()
    return client_obj




