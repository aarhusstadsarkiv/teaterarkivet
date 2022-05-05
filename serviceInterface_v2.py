import urllib
import json

import requests

# from google.appengine.api import urlfetch


class Service:
    def __init__(self, api_key):

        self.API_KEY = api_key
        self.BASE_URL = "https://openaws.appspot.com"
        self.GET_COLLECTIONS = {
            "records": "records",
            "records_v3": "records_v3",
            "relations": "relations",
            "entities": "entities",
            "persons": "entities",
            "people": "entities",
            "organisations": "entities",
            "events": "entities",
            "places": "entities",
            "creators": "entities",
            "addresses": "entities",
            "locations": "entities",
            "tags": "entities",
            "collections": "collections",
        }

        self.POST_COLLECTIONS = {
            # records and creators er ikke med
            "relations": "relation_tools",
            "entities": "entity_tools",
            "persons": "entity_tools",
            "people": "entity_tools",
            "organisations": "entity_tools",
            "events": "entity_tools",
            "places": "entity_tools",
            "addresses": "entity_tools",
            "locations": "entity_tools",
            "tags": "entity_tools",
            "collections": "entity_tools"
            # 'collections': 'collections_v2'
        }

    #######################
    # PUBLIC BASE METHODS #
    #######################
    def get_collection(self, collection, query_params=None):
        """Fetches a collection of resources.

        Args:
            collection (str): The collection to fetch.
            query_params (list of tuples): Tuplelist of key-value params.

        Returns:
            payload (dict)
        """
        url = "/".join([self.BASE_URL, self.GET_COLLECTIONS[collection]])

        if query_params:
            encoded_params = self._urlencode(query_params)
            url = "?".join([url, encoded_params])

        return self._get_request(url)

    def get_collection_v2(self, query_params):
        # Checks if there are any (at least one) records that result from a query

        # if ('fmt', 'json') not in query_params:
        #     query_params.append(('fmt', 'json'))
        url = "?".join(
            [
                "https://aarhusarkivet.herokuapp.com/search",
                self._urlencode(query_params),
            ]
        )

        # url = '/'.join([self.BASE_URL, 'records_v3'])
        # url = '?'.join([url, self._urlencode(query_params)])
        return self._get_request(url)

    def get_resource(self, collection, resource_id, include_relations=True):
        """Fetches a single resource.

        Args:
            collection (str): The domain to which the resource belongs.
            resource_id (str): The id of the resource.
            include_relations (boolean): Defaults to True. Add all the resources relations to the response.

        Returns:
            payload (dict)
        """
        if collection in ["records", "records_v3"]:
            # url_root = '/'.join(['https://aarhusarkivet.herokuapp.com/records', resource_id])
            url_root = "/".join([self.BASE_URL, collection, resource_id])
            return self._get_request(url_root + "?fmt=json&curators=4")
            # return {'status_code': 0, 'result': api_response}

        else:
            url = "/".join(
                [self.BASE_URL, self.GET_COLLECTIONS.get(collection), resource_id]
            )
            resource = self._get_request(url)

            # If so far so good, go fetch any relations
            if include_relations and resource.get("status_code") == 0:
                rel_path = "/".join([self.BASE_URL, "relations"])
                rel_param = "=".join(["f_id", resource_id])
                payload = self._get_request("?".join([rel_path, rel_param]))
                # If succesful request that has relations-content
                if payload["status_code"] == 0 and payload.get("result"):
                    resource["result"]["relations"] = payload.get("result")

            return resource

    def get_static_resource(self, url):
        # Used to return facet-files and any other stuff
        return self._get_request(url)

    def update_resource(self, collection, resource_id, post_params):
        """Updates the supplied resource.

        Args:
            collection (str): The collection-name to which the resource belongs.
            resource_id (str): The ID of the resource to be updated.
            post_params (list of tuples): List of POST-data items.

        Returns:
            boolean: True if successful, False otherwise.

            If False, it furthermore returns an error-string.
            If True, it furthermore returns the ID (str) of the updated resource.
        """

        def format_post_params(params):
            # Convert multidict to standard dict
            # http://stackoverflow.com/questions/2429098/how-to-treat-the-last-element-in-list-differently-in-python
            # http://stackoverflow.com/questions/23049773/how-to-dynamically-move-inside-a-nested-dict-in-python
            # http://stackoverflow.com/questions/7653726/how-to-turn-a-list-into-nested-dict-in-python?rq=1

            def traverse_down(branch, keys):
                for key in keys:
                    if key not in branch:
                        branch[key] = {}
                    branch = branch[key]
                return branch

            def insert_value(result, keys, value):
                # branch = result
                if isinstance(keys, list):
                    result = traverse_down(result, keys[:-1])
                    current_key = keys[-1]
                else:
                    current_key = keys

                if current_key in result:
                    if not isinstance(result[current_key], list):
                        result[current_key] = [result[current_key]]
                    result[current_key].append(value)
                else:
                    result[current_key] = value

            result = {}
            for tup in params:
                key = tup[0].strip()
                value = tup[1].strip()

                if value:
                    if "." in key:
                        insert_value(result, key.split("."), value)
                    else:
                        insert_value(result, key, value)

            return result
            # count = 0
            # for key, value in result.items():
            #     if '.' in key:
            #         keys = key.split('.')
            #         for level in keys[:-1]:
            #             if level not in result:
            #                 result[level] = {}
            #             result = result[level]
            #         key = keys[-1]

        data = {}
        oaws_meta = {"id": resource_id}
        # data['id'] = int(resource_id)

        params = format_post_params(post_params)

        # HACK STUFF
        if collection == "people":
            firstnames = params.get("firstnames")
            if firstnames and not isinstance(firstnames, list):
                params["firstnames"] = [firstnames]

            lastnames = params.get("lastnames")
            if lastnames and not isinstance(lastnames, list):
                params["lastnames"] = [lastnames]

            occupation = params.get("occupation")
            if occupation and not isinstance(occupation, list):
                params["occupation"] = [occupation]

        if params.get("scheme"):
            params["schema"] = params["scheme"]
            params.pop("scheme")
            oaws_meta["schema_name"] = params["schema"]
        data = params
        data["oaws_meta"] = oaws_meta

        payload = {"operation": "update", "data": data}

        # return payload
        return self._post_request_v2(
            collection=collection,
            operation="update",
            resource_id=resource_id,
            payload=payload,
        )

    def insert_resource(self, collection, post_params):
        """Posts a new resource to a collection.

        Args:
            collection (str): The collection to which the resource must be added.
            post_params (list of tuples): List of POST-data items.

        Returns:
            boolean: True if successful, False otherwise.

            If False, it furthermore returns an error-string.
            If True, it furthermore returns the ID (str) of the created resource.
        """

        if collection not in self.POST_COLLECTIONS:
            return {
                "status_code": 5,
                "status_msg": "You do not have the rights to create this type of resource.",
            }

        if collection == "relations":
            return {
                "status_code": 4,
                "status_msg": "Wrong method. Call 'insert_relation' to create a relation.",
            }

        def format_post_params(self, params):
            # Convert multidict to standard dict
            formatted_params = {}
            for tup in params:
                key = tup[0].strip()
                value = tup[1].strip()
                if key in formatted_params.keys():
                    formatted_params[key].append(value)
                else:
                    formatted_params[key] = [value]
            return formatted_params

        data = {}
        # Generate payload
        params = format_post_params(params)
        params["schema"] = schema_name
        data["content"] = params

        payload = {
            "token": self.API_KEY,
            "operation": operation,
            "data": json.dumps(data),
        }

        return self._post_request(collection, operation="create", params=post_params)

    def insert_relation(self, post_params):
        def generate_relation(post_params):
            subject_id = (
                subject_domain
            ) = object_id = object_domain = rel_label = rel_start = rel_end = None

            for tup in post_params:
                if tup[0] == "subject_id":
                    subject_id = tup[1]
                if tup[0] == "subject_domain":
                    subject_domain = tup[1]
                if tup[0] == "object_id":
                    object_id = tup[1]
                if tup[0] == "object_domain":
                    object_domain = tup[1]
                if tup[0] == "rel_label":
                    rel_label = tup[1]
                if tup[0] == "rel_start":
                    rel_start = tup[1]
                if tup[0] == "rel_end":
                    rel_end = tup[1]

            if (
                subject_id
                and subject_domain
                and object_id
                and object_domain
                and rel_label
            ):

                if subject_domain == "people" and object_domain == "events":
                    rel_base_type = 7
                    object_url = "/".join([self.BASE_URL, "events", object_id])
                    rel_start, rel_end = get_dates(object_url)
                elif subject_domain == "events":
                    rel_base_type = 9

                return [
                    0,
                    subject_id,
                    object_id,
                    [2, 3],
                    rel_base_type,
                    rel_label,
                    rel_start,
                    rel_end,
                ]
            else:
                return False

        def generate_reverse_relation(relation):
            reverse = list(relation)  # copy relation

            # update base_rel_type
            if relation[4] == 7:
                reverse[4] = 9
            elif relation[4] == 9:
                reverse[4] = 7
            else:
                return False

            # flip sub-obj
            reverse[1] = relation[2]
            reverse[2] = relation[1]

            return reverse

        def get_dates(url):
            entity = self._get_request(url)
            date_from = entity.get("date_from")
            date_to = entity.get("date_to")
            return [date_from, date_to]

        relation = generate_relation(post_params)
        if relation:
            reverse = generate_reverse_relation(relation)

            payload = {"operation": "create", "data": {"rel_data": [relation, reverse]}}

            url = "/".join([self.BASE_URL, self.POST_COLLECTIONS.get("relations")])
            return self._post_request_v3(url, payload)
        else:
            return {"status_code": 5, "status_msg": "Unable to genrate relation."}

    def delete_relation(self, relation_id):
        payload = {"operation": "remove", "data": {"rel_id": int(relation_id)}}
        url = "/".join([self.BASE_URL, self.POST_COLLECTIONS.get("relations")])

        # return result
        return self._post_request_v3(url, payload)

    def delete_resource(self, collection, resource_id):
        """Deletes the supplied resource.

        Args:
            collection (str): The collection-name to which the resource belongs.
            resource_id (str): The ID of the resource to be deleted.

        Returns:
            boolean: True if successful, False otherwise.

            If False, it furthermore returns an error-string.
            If True, it furthermore returns the ID (str) of the deleted resource.
        """

        if collection in [
            "people",
            "organisations",
            "events",
            "places",
            "addresses",
            "collections",
            "relations",
        ]:
            return self._post_request(
                collection, operation="remove", resource_id=resource_id
            )
        else:
            return False, "You're not allowed to delete the selected resourcetype"

    def autocomplete(self, query_params, decode=True):
        """Queries autocomplete

        Args:
            query_params (list of tuples): Tuplelist of key-value params.
            decode (boolean): utf8-decode before http-request.

        Returns:
            payload (list)
        """
        params = self._urlencode(query_params, decode)
        url = "?".join(["https://aarhusiana.appspot.com/autocomplete_v3", params])
        # response = urlfetch.fetch(url, follow_redirects=False, deadline=10)
        # return response.content
        response = requests.get(url, allow_redirects=True, timeout=10)
        return response.text

    #####################
    # PRIVATE FUNCTIONS #
    #####################
    def _get_request(self, url):
        # response = urlfetch.fetch(url, follow_redirects=False, deadline=10)
        response = requests.get(url, allow_redirects=True, timeout=10)
        try:
            # response_to_dict = json.loads(response.content)
            # return response_to_dict
            response_to_dict = response.json()
            return response_to_dict
        except ValueError as e:
            return {"status_code": 5, "status_msg": e}

    def _post_request_v3(self, url, payload):

        if payload:
            payload["token"] = self.API_KEY
            payload["data"] = json.dumps(payload.get("data"))
            payload = urllib.urlencode(payload)

        # response = urlfetch.fetch(url, method=urlfetch.POST, payload=payload, follow_redirects=False,
        #             headers={'Content-Type': 'application/x-www-form-urlencoded'})
        response = requests.post(
            url,
            payload=payload,
            allow_redirects=False,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        try:
            # response_to_dict = json.loads(response.content)
            # return response_to_dict
            response_to_dict = response.json()
            return response_to_dict
        except ValueError as e:
            return {"status_code": 5, "status_msg": e}

    def _post_request_v2(self, collection, operation, payload=None, resource_id=None):

        url = "/".join([self.BASE_URL, self.POST_COLLECTIONS.get(collection)])

        if payload:
            payload["token"] = self.API_KEY
            payload["data"] = json.dumps(payload.get("data"))
            payload = urllib.urlencode(payload)

        # response = urlfetch.fetch(url, method=urlfetch.POST, payload=payload, follow_redirects=False,
        #             headers={'Content-Type': 'application/x-www-form-urlencoded'})
        response = requests.post(
            url,
            payload=payload,
            allow_redirects=False,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        try:
            # response_to_dict = json.loads(response.content)
            # return response_to_dict
            response_to_dict = response.json()
            return response_to_dict
        except ValueError as e:
            return {"status_code": 5, "status_msg": response.content}

    def _post_request(self, collection, operation, resource_id=None, params=None):
        def format_post_params(self, params):
            # Convert multidict to standard dict
            formatted_params = {}
            for tup in params:
                key = tup[0].strip()
                value = tup[1].strip()
                if key in formatted_params.keys():
                    formatted_params[key].append(value)
                else:
                    formatted_params[key] = [value]
            return formatted_params

        data = {}
        # Generate payload
        if params:
            params = format_post_params(params)
            # params['schema'] = schema_name
            data["content"] = params

        if resource_id:
            if collection == "relations":
                data["rel_id"] = int(resource_id)
            else:
                data["id"] = int(resource_id)

        payload = {
            "token": self.API_KEY,
            "operation": operation,
            "data": json.dumps(data),
        }

        # Temporary neccessity
        # If remove-request there are no params as arguments and therefore no schema_name is generated
        # Edit-requests always (?) include params
        if operation == "remove":
            if collection == "collections":
                url = self.COLLECTIONS_URL
            elif collection == "relations":
                url = self.RELATION_TOOLS_URL
            else:
                url = self.ENTITY_TOOLS_URL
        else:
            if schema_name != "collection":
                url = self.ENTITY_TOOLS_URL
            elif collection == "relations":
                url = self.RELATION_TOOLS_URL
            else:
                url = self.COLLECTIONS_URL

        # Encode and request
        encoded_data = urllib.urlencode(payload)
        # response = urlfetch.fetch(url, method=urlfetch.POST, payload=encoded_data, follow_redirects=False,
        #         headers={'Content-Type': 'application/x-www-form-urlencoded'})
        response = requests.post(
            url,
            payload=payload,
            allow_redirects=False,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        try:
            # response_to_dict = json.loads(response.content)
            # return response_to_dict
            response_to_dict = response.json()
            return response_to_dict
        except ValueError as e:
            return {"status_code": 5, "status_msg": e}

    def _urlencode(self, params, decode=True):
        path = {}
        if type(params) == dict:
            iterable = params.items()
        else:
            iterable = params

        for key, value in iterable:
            if key in path:
                # If value in current value-string, continue, else:
                path[key] += ";" + value
            else:
                path[key] = value

        encoded = urllib.urlencode(path)

        if decode:
            return encoded.decode("utf-8")
        else:
            return encoded
