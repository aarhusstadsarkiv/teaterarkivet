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
    # Route('/autocomplete', views.autocomplete),
    # Route('/login', views.login),
    # Route('/logout', endpoint=logout),
    # Route('/events/{event_id:int}', endpoint=event, methods=["GET", "POST", "DELETE"]),
    # Route('/people/{person_id:int}', endpoint=person, methods=["GET", "POST", "DELETE"]),
    # Route('/records/{record_id:int}', endpoint=record),
    Route('/about', views.about),
    Route('/info', views.info),
    Route('/how-to-search', views.how_to_search),
    Route("/test", views.test),
    Mount('/static', static, name="static"),
    Route("/robots.txt", static, name="robots")
]
