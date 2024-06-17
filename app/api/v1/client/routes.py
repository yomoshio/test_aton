from fastapi import APIRouter, Depends
from typing import List
import app.api.v1.user.schemas as s_s
import app.api.v1.client.schemas as c_s
import app.api.v1.client.logic as l
from services.authentication import get_current_user, get_admin_user
from app.api.v1.user.models import User

router = APIRouter(prefix="/client", tags=["users"])


@router.post(
    "/",
    response_model=c_s.ClientOut,
    summary="Create a Client",
    description=(
            "Create a new client with such fields "
            "Everyone can create new clients."
    ),
    response_description="The created clietnt."
)
async def create_client(client: c_s.ClientCreate):
    return await l.create_client_logic(client)


