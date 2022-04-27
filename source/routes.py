from starlette.routing import Route, Mount
from . import views
from .resources import static

# from enum import Enum

# class Resource(str, Enum):
#     people = "people"
#     events = "events"
#     records = "records"


routes = [
    Route('/', views.homepage),
    # Route('/search', views.search),
    Route('/autocomplete', views.autocomplete),
    Route('/login', views.login),
    # Route('/logout', endpoint=logout),
    Route('/events/{id:int}', views.resource, methods=["GET", "POST", "DELETE"]),
    Route('/people/{id:int}', views.resource, methods=["GET", "POST", "DELETE"]),
    Route('/records/{id:int}', views.record),
    Route('/about', views.about),
    Route('/info', views.info),
    Route('/how-to-search', views.how_to_search),
    Route("/test", views.test),
    Mount('/static', static, name="static"),
    Route("/robots.txt", static, name="robots"),
    Route("/favicon.ico", static, name="favicon")
]
