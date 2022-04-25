from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.gzip import GZipMiddleware
from . import settings


middleware = [
    Middleware(GZipMiddleware),
    Middleware(SessionMiddleware, secret_key=settings.SECRET, https_only=settings.HTTPS_ONLY)
]
