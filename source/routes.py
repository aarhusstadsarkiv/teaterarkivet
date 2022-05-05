from starlette.routing import Route, Mount
from . import views
from .resources import static


routes = [
    Route("/", views.homepage),
    Route("/search", views.search),
    Route("/autocomplete", views.autocomplete),
    Route("/login", views.login, methods=["GET", "POST"]),
    Route("/logout", views.logout),
    Route("/records/{id:int}", views.record),
    Route("/events/{id:int}", views.resource, methods=["GET", "POST", "DELETE"]),
    Route("/people/{id:int}", views.resource, methods=["GET", "POST", "DELETE"]),
    Route("/relations/{id:int}", views.relations, methods=["DELETE"]),
    Route("/relations", views.relations, methods=["POST"]),
    Route("/about", views.about),
    Route("/info", views.info),
    Route("/how-to-search", views.how_to_search),
    Route("/test", views.test),
    Mount("/static", static, name="static"),
    Route("/robots.txt", static, name="robots"),
    Route("/favicon.ico", static, name="favicon"),
]
