"""
Initialization Services.

This module provides a utility function to ensure the presence of
an admin user in the system.
If an admin user doesn't exist, it initializes a new admin user with
default credentials.
"""
from passlib.context import CryptContext
from app.api.v1.user.models import User
from app.core.config.settings import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def init_default_admin():
    """
    Ensure the presence of an admin user in the system.

    This function checks if a default admin exists.
    If not, it creates a new default admin with credentials from settings.
    """

    admin = await User.get_or_none(
        username=settings.DEFAULT_ADMIN_USERNAME
    )

    if not admin:
        hashed_password = pwd_context.hash(settings.DEFAULT_ADMIN_PASSWORD)
        new_admin = await User.create(
            fio=settings.DEFAULT_ADMIN_FIO,
            username=settings.DEFAULT_ADMIN_USERNAME,
            password_hash=hashed_password,
            is_admin=1
        )

        await new_admin.save()

