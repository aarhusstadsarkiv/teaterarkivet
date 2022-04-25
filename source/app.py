from starlette.applications import Starlette

from .middleware import middleware
from .routes import routes
from . import views, settings


app = Starlette(
    debug=settings.DEBUG,
    routes=routes,
    middleware=middleware,
    exception_handlers={
        404: views.not_found,
        500: views.internal_server_error
    },
)
