from fastapi import APIRouter, Depends
from typing import List
import app.api.v1.user.schemas as s_s
import app.api.v1.client.schemas as c_s
import app.api.v1.user.logic as l
from services.authentication import get_current_user, get_admin_user
from app.api.v1.user.models import User

router = APIRouter(prefix="/user", tags=["users"])


@router.post(
    "/",
    response_model=s_s.UserOut,
    summary="Create a User",
    description=(
            "Create a new user with a username, email, and password. "
            "Only administrators can create new users."
    ),
    response_description="The created user."
)
async def create_user(user: s_s.UserCreate, current_user: User = Depends(get_admin_user)):
    return await l.create_user_logic(user)


@router.get(
    "/user-clients",
    response_model=c_s.ClientResponse,
    summary="List User Clients",
    description=(
            "Fetch a paginated list of all clients for a specific user.\n\n"
            "The number of notes to skip and the maximum number to return can be adjusted using the "
            "page and size parameters."
    ),
    response_description="A list of notes for the specified user along with pagination details."
)
async def get_user_notes(current_user: User = Depends(get_current_user), page: int = 1, size: int = 10):

    clients, total = await l.get_user_clients_logic(current_user=current_user, page=page, size=size)

    return {
        "total": total,
        "page": page,
        "per_page": size,
        "clients": clients
    }


@router.put(
    "/update/{client_id}",
    response_model=c_s.ClientOut,
    summary="Update a Client",
    description=(
            "Update the details of a specific client by their ID. "
            "Only users can update client details."
    ),
    response_description="The updated client."
)
async def update_user(client_id: int, client: c_s.ClientUpdate, current_user: User = Depends(get_current_user)):
    return await l.update_user_logic(client_id, client)

