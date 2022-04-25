from urllib import request
from starlette.responses import JSONResponse
# from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import Response

from . import settings
from .resources import templates, client

import clientInterface_v2

def authenticated(request):
    if request.session.get("user"):
        return True
    return False


async def homepage(request):
    return templates.TemplateResponse('page_home.html', {'request': request})


# async def autocomplete(request):
#     term = request.path_params["q"]
#     if term:
#         return JSONResponse(client.autocomplete(term))


# async def search(request):
#     return templates.TemplateResponse("search.html", {"request": request})
#     # return templates.TemplateResponse("page_collections_v2.html", {"request": request})


# async def records(request):
#     id = request.path_params["id"]
#     fmt = request.path_params.get("fmt")
#     resp = client.get_resource_v3("records_v3", id, fmt=fmt)

#     if resp.get("status_code") != 0:
#         ctx = {"request": request, "message": resp.get("status_msg")}
#         return templates.TemplateResponse("message.html", {"request": request})

#     if fmt == "json":
#         return JSONResponse(rec)
#     else:
#         # return templates.TemplateResponse("page_resource_v3.html", {"request": request})
#         return templates.TemplateResponse("record.html", ctx)

#             elif response.get("status_code") == 0:

#                 if self.request.get("operation") == "edit" and self.user:
#                     # GET SCHEMA - HARD_CODED
#                     schema = urlfetch.fetch(
#                         "https://almanak.github.io/schemas/%s.aarhusteater.json"
#                         % collection,
#                         deadline=30,
#                     )
#                     schema = json.loads(schema.content)
#                     response["operation"] = "edit"
#                     response["resource"] = self.client.populate_schema_v2(
#                         schema, response["resource"]
#                     )
#                 else:
#                     response["operation"] = "view"

#                 self.render("page_resource_v3.html", response)
#             else:
#                 # self.render_json(response)
#                 self.render(
#                     "page_message.html", {"message": response.get("status_msg")}
#                 )
#         else:
#             self.abort(404)

async def info(request):
    return templates.TemplateResponse("info.html", {"request": request})


async def about(request):
    return templates.TemplateResponse("about.html", {"request": request})


async def how_to_search(request):
    return templates.TemplateResponse("how-to-search.html", {"request": request})


# async def login(request):
#     if request.method == "GET":
#         return templates.TemplateResponse("page_login.html", {"request": request})


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

async def test(request):
    return templates.TemplateResponse("test.html", {"request": request})
