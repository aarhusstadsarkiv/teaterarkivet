from typing import Collection
from starlette.responses import JSONResponse
# from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import Response

from . import settings, utils, client
from .resources import templates

def authenticated(request):
    if request.session.get("user"):
        return True
    return False

def render(request: Request, template: str, context: dict = {}):
    context["request"] = request
    context["site"] = settings.CLIENT
    context["currentUrl"] = request.url
    if not context.get("page"):
        context["page"] = {}
    if not context.get("facets"):
        context["facets"] = utils.generate_facets()
    return templates.TemplateResponse(template, context)


# def render_json(request: Request, context: dict = {}):
#     # Remove links to image-files if not user
#     if not self.user:
#         response.pop("representations", None)
#         response.pop("thumbnail", None)
#         response.pop("portrait", None)
#     self.response.headers["Content-Type"] = "application/json; charset=utf-8"
#     self.response.write(json.dumps(response))


async def homepage(request: Request):
    ctx: dict = {"page": {"type": "homepage"}}
    return render(request, "index.html", ctx)


async def autocomplete(request: Request):
    term = request.query_params["q"]
    if term:
        return JSONResponse(client.autocomplete(term))


async def info(request: Request):
    return render(request, "info.html")


async def about(request: Request):
    return render(request, "about.html")


async def how_to_search(request: Request):
    return render(request, "how-to-search.html")


async def login(request: Request):
    if request.method == "GET":
        return render(request, "login.html")


async def test(request: Request):
    res = client.get_resource("events", 112996)
    ctx = {"collection": "events", "resource": res}
    return render(request, "test.html", ctx)


# async def search(request):
#     return templates.TemplateResponse("search.html", {"request": request})
#     # return templates.TemplateResponse("page_collections_v2.html", {"request": request})


async def record(request: Request):
    id = request.path_params["id"]
    json = request.query_params.get("json") or False
    resp = client.get_record(id, json=json)

    if resp.get("status_code") != 0:
        if json:
            return JSONResponse(resp)
        return render(request, "message.html", resp)

    return render(request, "resource.html", resp)


async def resource(request: Request):
    id = request.path_params["id"]
    json = request.query_params.get("json") or False
    collection = "events" if "events" in request.url.path else "people"
    resp = client.get_resource(collection, id, json=json)

    if resp.get("status_code") != 0:
        if json:
            return JSONResponse(resp)
        return render(request, "message.html", resp)

    if request.method == "GET":
        resp["operation"] = "view"
        return render(request, "resource.html", resp)


async def not_found(request: Request, exc: Exception) -> Response:
    context = {"request": request}
    return templates.TemplateResponse(
        "404.html", context=context, status_code=404
    )


async def internal_server_error(request: Request, exc: Exception) -> Response:
    context = {"request": request}
    return templates.TemplateResponse(
        "500.html", context=context, status_code=500
    )
