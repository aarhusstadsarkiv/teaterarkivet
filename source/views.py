from starlette.responses import Response, JSONResponse, RedirectResponse
from starlette.requests import Request
from starlette.datastructures import FormData
from starlette.exceptions import HTTPException

from . import settings, utils, client
from .resources import templates


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
    ctx = {"page": {"type": "homepage"}}
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
        ctx = dict()
        if request.session.get("user"):
            ctx["already"] = True
        else:
            if request.query_params.get("return"):
                ctx["return"] = request.query_params["return"]
            if request.query_params.get("access_request"):
                ctx["access_request"] = True
            if request.get("failed"):
                ctx["failed"] = True
        return render(request, "login.html", ctx)

    if request.method == "POST":
        form: FormData = await request.form()
        email = form.get("email")
        pw = form.get("password")
        return_url = request.query_params.get("return", False)

        if email == settings.config("EMAIL") and pw == settings.config("PASSWORD"):
            request.session["user"] = True

            if return_url:
                # status_code 307 preserves request.method
                return RedirectResponse(return_url, status_code=302)
            else:
                return RedirectResponse("/", status_code=302)
        else:
            return RedirectResponse("/login?failed=True", status_code=302)


async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)


async def test(request: Request):
    res = client.get_resource("events", 112996)
    ctx = {"collection": "events", "resource": res}
    return render(request, "test.html", ctx)


async def search(request: Request):
    resp = client.get_collection(request.query_params)
    if resp.get("status_code") != 0:
        return render(request, "message.html", resp)
    return render(request, "search.html", resp)


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


async def relations(request: Request):
    if not request.session.get("user"):
        raise HTTPException(status_code=403)

    if request.method == "POST":
        data: list = await request.form()
        resp = client.create_relation(data)
        if request.headers.get("x-requested-with", "") == "XMLHttpRequest":
            return JSONResponse(resp)
        else:
            render("message.html", {"message": resp})

    if request.method == "DELETE":
        id: int = request.path_params["id"]
        resp: dict = client.delete_relation(id)
        if request.headers.get("x-requested-with", "") == "XMLHttpRequest":
            return JSONResponse(resp)
        else:
            render("message.html", {"message": resp})


async def not_found(request: Request, exc: Exception) -> Response:
    context = {"request": request}
    return templates.TemplateResponse("404.html", context=context, status_code=404)


async def internal_server_error(request: Request, exc: Exception) -> Response:
    context = {"request": request}
    return templates.TemplateResponse("500.html", context=context, status_code=500)
