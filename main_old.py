# Python libraries
import webapp2_dep
import jinja2
import os
import json
import urllib

# Application libraries
import clientInterface_v2
import settings

from google.appengine.api_dep import urlfetch
from webapp2_dep_extras import sessions


class BaseSessionHandler(webapp2_dep.RequestHandler):
    def dispatch(self):  # override dispatch
        self.site = settings.CLIENT
        self.client = clientInterface_v2.Client(self.site)
        self.auth = authInterface.AuthInterface()
        self.user = self.auth.get_user()

        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
        try:
            # Dispatch the request.
            webapp2_dep.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    def render(self, template, context={}):
        context["site"] = self.site
        context["user"] = self.user
        # RENAME
        context["currentUrl"] = self.request.path_qs
        if not context.get("page"):
            context["page"] = {}
        # TODO
        if not context.get("facets"):
            context["facets"] = self.client.generate_facets()

        temp = JINJA_ENVIRONMENT.get_template(template)
        self.response.write(temp.render(context))

    def render_json(self, response):
        # Remove links to image-files if not user
        if not self.user:
            response.pop("representations", None)
            response.pop("thumbnail", None)
            response.pop("portrait", None)
        self.response.headers["Content-Type"] = "application/json; charset=utf-8"
        self.response.write(json.dumps(response))

    @webapp2_dep.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()


# DONE
class ItemHandler(BaseSessionHandler):
    def get(self, collection, resource_id):

        if collection in self.site.get("collections"):
            fmt = self.request.get("fmt")

            # UPDATED TO LATEST RECORDS_VERSION
            if collection != "records":
                response = self.client.get_resource(collection, resource_id, fmt=fmt)
            else:
                response = self.client.get_resource_v3(
                    "records_v3", resource_id, fmt=fmt
                )

            if fmt == "json":
                self.render_json(response)

            elif response.get("status_code") == 0:

                if self.request.get("operation") == "edit" and self.user:
                    # GET SCHEMA - HARD_CODED
                    schema = urlfetch.fetch(
                        "https://almanak.github.io/schemas/%s.aarhusteater.json"
                        % collection,
                        deadline=30,
                    )
                    schema = json.loads(schema.content)
                    response["operation"] = "edit"
                    response["resource"] = self.client.populate_schema_v2(
                        schema, response["resource"]
                    )

                else:
                    response["operation"] = "view"
                    # TODO Temporary collection-specific tests
                    # if collection == 'collections':
                    #     temp_structure = 'https://aarhusteaterarkiv-web.appspot.com/static/json/structure.json'
                    #     structure = urlfetch.fetch(temp_structure, follow_redirects=False, deadline=10)
                    #     response['resource']['structure'] = json.loads(structure.content)

                # OPDATED TO LATEST RECORDS_VERSION
                # self.render('page_resource.html', response)
                self.render("page_resource_v3.html", response)
                # self.render_json(response)
            else:
                # self.render_json(response)
                self.render(
                    "page_message.html", {"message": response.get("status_msg")}
                )
        else:
            self.abort(404)

    def post(self, collection, resource_id):
        # if self.user and self.user.get("user_level") == 2:

        if collection in self.site.get("collections"):
            if self.user:
                post_params = self.request.POST.items()
                response = self.client.update_resource(
                    collection, resource_id, post_params
                )
                # self.render_json(response)
                self.response.write(response)
            else:
                self.abort(401)
        else:
            self.abort(404)

    def delete(self, collection, resource_id):
        if self.user and self.user.get("user_level") == 2:

            # Only relations so far...
            if collection == "relations":
                response = self.client.delete_resource(collection, resource_id)

                if self.request.headers["x-requested-with"] == "XMLHttpRequest":
                    self.render_json(response)
                else:
                    self.render("page_message.html", {"message": response})
            else:
                self.abort(404)
        else:
            self.abort(401)


# DONE
class SearchHandler(BaseSessionHandler):
    def get(self):
        response = self.client.get_collection_v2(self.request.GET.items())
        if response.get("status_code") == 0:
            # self.render_json(response)
            self.render("page_collections_v2.html", response)
        else:
            self.render(
                "page_message.html",
                {"message": response.get("status_msg", "Manglende fejlbesked!")},
            )


# DONE
class CollectionHandler(BaseSessionHandler):
    def get(self, collection):

        if collection in self.site.get("collections"):
            response = self.client.get_collection(collection, self.request.GET.items())
            if response.get("status_code") == 0:
                self.render("page_collections.html", response)
            else:
                self.render(
                    "page_message.html",
                    {"message": response.get("status_msg", "Manglende fejlbesked!")},
                )
        else:
            self.abort(404)

    def post(self, collection):
        if self.user and self.user.get("user_level") == 2:
            # Only relations so far...
            if collection == "relations":
                response = self.client.create_relation(self.request.POST.items())

                if self.request.headers["x-requested-with"] == "XMLHttpRequest":
                    self.render_json(response)
                else:
                    self.render("page_message.html", {"message": response})
            else:
                self.abort(404)
        else:
            self.abort(401)


# DONE
class PageHandler(BaseSessionHandler):
    def get(self, path=None):
        context = {}

        if not path:
            context["page"] = {}
            context["page"]["type"] = "homepage"
            self.render("page_home.html", context)

        elif path == "logout":
            if self.user:
                self.auth.logout()
                self.redirect("/")
            else:
                self.render(
                    "page_message.html",
                    {"message": "To logout, you need to be logged in"},
                )

        else:
            self.render("page_" + path + ".html", context)

    # DONEclass LoginHandler(BaseSessionHandler):
    def get(self):
        context = {}

        if self.user:
            context["already"] = True
        else:
            if self.request.get("return"):
                context["return"] = self.request.get("return")
            if self.request.get("access_request"):
                context["access_request"] = True
            if self.request.get("failed"):
                context["failed"] = True

        self.render("page_login.html", context)

    def post(self):
        parameters = self.request.params
        email = parameters.get("email")
        password = parameters.get("password")

        if parameters.get("return_url"):
            return_encoded = parameters.get("return_url").encode("utf-8")
            return_url = urllib.quote(return_encoded, "?=/")
        else:
            return_url = False

        success, _ = self.auth.login(email, password)
        if success:
            if return_url:
                self.redirect(return_url)
            else:
                self.redirect("/users/me")
        else:
            self.redirect("/login?failed=True")


# DONE
class AutocompleteHandler(BaseSessionHandler):
    def get(self):

        term = self.request.get("q")
        if term:
            self.response.headers["Content-Type"] = "application/json; charset=utf-8"
            self.response.write(self.client.autocomplete(term))


WEBAPP2_dep_CONFIG = {
    "webapp2_dep_extras.auth": {
        "user_model": "models.User",
        "user_attributes": ["email_address", "name", "user_level", "user_group"],
    },
    "webapp2_dep_extras.sessions": {"secret_key": """find in local env file"""},
}

APPLICATION = webapp2_dep.WSGIApplication(
    [
        # webapp2_dep.Route("/", handler=PageHandler, methods=["GET"]),
        # webapp2_dep.Route('/test', handler=TestHandler, methods=['GET']),
        # webapp2_dep.Route("/autocomplete", handler=AutocompleteHandler, methods=["GET"]),
        # webapp2_dep.Route('/signup', handler=SignupHandler, methods=['GET', 'POST']),
        webapp2_dep.Route("/login", handler=LoginHandler, methods=["GET", "POST"]),
        # webapp2_dep.Route(
        #     "/<path:(about|how-to-search|cookies|info|logout)>",
        #     handler=PageHandler,
        #     methods=["GET"],
        # ),
        webapp2_dep.Route("/search", handler=SearchHandler, methods=["GET"]),
        webapp2_dep.Route(
            "/<collection:[a-z\_]+>", handler=CollectionHandler, methods=["GET", "POST"]
        ),
        webapp2_dep.Route(
            "/<collection:[a-z\_]+>/<resource_id:\d+>",
            handler=ItemHandler,
            methods=["GET", "POST", "DELETE"],
        ),
    ],
    debug=True,
    config=WEBAPP2_dep_CONFIG,
)
