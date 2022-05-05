import httpx
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from . import settings

async_client = httpx.AsyncClient()
client = httpx.Client()

templates = Jinja2Templates(directory=str(settings.TEMPLATES_DIR))
templates.env.globals = settings.TEMPLATE_GLOBALS

static = StaticFiles(directory=str(settings.STATIC_DIR))
