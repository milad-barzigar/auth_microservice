# authz/resource/apiv1/__init__.py

from .user import UserResource
try:
    from .auth import AuthResource
except Exception:
   
    AuthResource = None

__all__ = ["UserResource", "AuthResource"]

