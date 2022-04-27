
import urllib
import urllib.parse as urlparse

from . import settings

# API-module
import serviceInterface_v2


class Client():

    def __init__(self, config):
        # Fetch config
        self.host = config.get("host")
        self.facets = config.get("facets")
        self.filters = config.get("filters")
        self.default_params = config.get("default_query_params")
        self.service = serviceInterface_v2.Service("api_key-fetch-from-config")

    def get_resource_v3(self, collection, resource_id, include_relations=True,
                        fmt=None):
        """Fetch a single resource.

        Args:
            collection (str): The domain to which the resource belongs.
            resourceID (str): The id of the resource.
            include_relations (boolean): Defaults to True. Add the relations to the response.

        Returns:
            payload (dict)
        """
        def format_metadata(resource):
            result = {}

            for k, v in resource.iteritems():

                if k == 'representations':
                    result[k] = v

                elif k == 'series':
                    output = []
                    currentLevel = []
                    urlpath = {}

                    if resource.get('collection'):
                        urlpath['collection'] = resource['collection'].get('id')

                    for i in v.split('/'):
                        level = {}
                        currentLevel.append(i)
                        urlpath['series'] = '/'.join(currentLevel)
                        level['label'] = i
                        level['new_link'] = self._generate_new_link(urlpath)
                        output.append(level)
                    result[k] = output

                elif k in ['date_from', 'date_to']:
                    item = {}
                    item['label'] = k
                    item['date'] = v
                    item['new_link'] = self._generate_new_link(k, v)
                    result[k] = item

                # If key is list of simple strings
                elif k in ['admin_tags', 'collection_tags']:
                    output = []
                    for idx in v:
                        item = {}
                        item['label'] = idx
                        item['new_link'] = self._generate_new_link(k, idx)
                        output.append(item)
                    result[k] = output

                elif k in ['resources']:
                    result[k] = v

                # If key is filter and has type integer and NOT repeatable
                # elif type(v) is list:
                #     output = []
                #     for idx in v:
                #         current = {}
                #         if type(idx) is dict:
                #             current['id'] = idx.get('id')
                #             current['label'] = idx.get('label')
                #             current['new_link'] = self._generate_new_link(k, idx.get('id'))
                #         else:
                #             current['label'] = idx
                #             current['new_link'] = self._generate_new_link(k, idx)
                #         output.append(current)
                #     result[k] = output

                elif type(v) is dict:
                    output = {}
                    output['id'] = v.get('id')
                    output['label'] = v.get('label')
                    output['new_link'] = self._generate_new_link(k, v.get('id'))
                    result[k] = output

                elif isinstance(v, list) and k in self.filters:
                    output = []

                    for _dict in v:
                        # hierarchical concept or entity
                        if isinstance(_dict.get('id'), list):
                            hierarchy = []
                            for i, v in enumerate(_dict.get('id')):
                                item = {}
                                item['id'] = v
                                item['label'] = _dict.get('label')[i]
                                item['new_link'] = '='.join([k, str(v)])
                                hierarchy.append(item)
                            output.append(hierarchy)

                        # flat concept or entity
                        else:
                            _id = _dict.get('id')
                            label = _dict.get('label')
                            item = {}
                            item['id'] = _id
                            item['label'] = label
                            item['new_link'] = self._generate_new_link(k, _id)
                            output.append(item)

                    result[k] = output

                else:
                    result[k] = v
            return result

        def format_relations(relations):

            def sort_by_value(list_of_dicts, key_name, default=None):
                decorated = [(dict_.get(key_name, default), dict_) for dict_ in list_of_dicts]
                decorated.sort()
                return [dict_ for (key, dict_) in decorated]

            # NOTE: SITE-SPECIFIK FOR AARHUSTEATER
            onstage = []
            offstage = []
            for rel in relations:
                label = rel.get("rel_label")
                if label.startswith("Skuespiller") and label.find("("):
                    start_index = label.find("(") + 1
                    rel["rel_label"] = label[start_index:-1]
                    onstage.append(rel)
                elif label.startswith("Skuespiller") or label.startswith("Statist"):
                    onstage.append(rel)
                else:
                    offstage.append(rel)

            if collection in ['people']:
                onstage_sorted = sort_by_value(onstage, 'rel_date_from', '2020-12-12')
                offstage_sorted = sort_by_value(offstage, 'rel_date_from', '2020-12-12')
            else:
                onstage_sorted = sort_by_value(onstage, 'rel_label')
                offstage_sorted = sort_by_value(offstage, 'rel_label')

            return [
                {
                    "label": u"Sceneroller",
                    "data": onstage_sorted
                },
                {
                    "label": u"Produktionshold",
                    "data": offstage_sorted
                }
            ]

        def has_references(collection, resource_id):
            # payload = self.get_collection('records',
            #                               query_params=[(collection, resource_id), ('limit', '1')])

            payload = self.get_collection_v2([(collection, resource_id), ('size', '1')])

            # if payload.get('status_code') == 0 and payload.get('result'):
            if payload.get('result'):
                return True
            else:
                return False

        # Request api
        payload = self.service.get_resource(collection, resource_id)

        if payload.get('status_code') == 0:

            # If json-view, no need to process GUI-stuff
            # render_json() will convert the dict back to json before sending to browser
            if fmt == 'json':
                return payload.get('result')

            else:
                response = {}
                response['status_code'] = 0
                response['collection'] = collection
                response['id'] = resource_id

                # Linkify the filter-links and update any deprecated key-names
                response['resource'] = format_metadata(payload.get('result'))

                # If relations, format those as well
                # NOTE: Teater-specifik
                if include_relations and payload['result'].get('relations'):
                    response['resource']['relations'] = format_relations(payload['result'].get("relations"))

                # If an entity, is it referenced in any records.
                # NOTE: Teater-specifik subset af entiteter
                if collection in ["events", "people", "organisations", "creators"]:
                    if collection == 'creators':
                        collection = response['resource'].get("domain")
                    response['is_subject'] = has_references(collection, resource_id)

                # If a possible creator, has it actually created any records?
                # NOTE: Teater-specifik subset af entiteter
                if collection in ["people", "organisations", "creators"]:
                    if collection == 'creators':
                        collection = response['resource'].get("domain")
                    response['is_creator'] = has_references('creators', resource_id)

                return response
        else:
            return payload

    # Base methods
    def get_resource(self, collection, resource_id, include_relations=True,
                     fmt=None):
        """Fetch a single resource.

        Args:
            collection (str): The domain to which the resource belongs.
            resourceID (str): The id of the resource.
            include_relations (boolean): Defaults to True. Add the relations to the response.

        Returns:
            payload (dict)
        """
        def format_metadata(collection, result):

            def update_keyname(key_name):
                UPDATE = {
                    "hierarchical_level": "series",
                    "curator": "curators",
                    "doctype": "content_type",
                    "creator": "creators",
                    "subject": "subjects",
                    "local_tag": "collection_tags",
                    "oas_list": "ids_only",
                    "online_access": "online_only",
                    "location": "locations",
                    "organisation": "organisations",
                    "event": "events",
                    "tag": "tags",
                    "rightsholder": "rightsholders"
                }
                if key_name in UPDATE:
                    return UPDATE[key_name]
                else:
                    return key_name

            def iterate_node(inputDict):
                result = {}

                for k, v in inputDict.items():
                    k = update_keyname(k)

                    if k == 'series':
                        output = []
                        currentLevel = []
                        urlpath = {}

                        collection = inputDict.get('collection')
                        if ('collection', collection[0]) not in self.default_params:
                            if type(collection) is list:
                                urlpath['collection'] = collection[0]
                            else:
                                urlpath['collection'] = collection

                        for i in v.split('/'):
                            level = {}
                            currentLevel.append(i)
                            urlpath['series'] = '/'.join(currentLevel)
                            level['name'] = i
                            level['new_link'] = self._generate_new_link(urlpath)
                            output.append(level)
                        result[k] = output

                    # Needs to have collectionID added to add_link to contain
                    elif k == 'collection_tags':
                        collection = inputDict.get('collection')
                        collection_tuple = ("collection", collection[0])
                        output = []
                        for i in v:
                            current = {}
                            current['name'] = i
                            current['new_link'] = self._generate_new_link(k, i)
                            output.append(current)
                        result[k] = output

                    # If key is filter and has type string and repeatable. Only admin_tags (besides collectiontags)?
                    elif k in ['admin_tags']:
                        output = []
                        for i in v:
                            current = {}
                            current['name'] = i
                            current['new_link'] = self._generate_new_link(k, i)
                            output.append(current)
                        result[k] = output

                    # If key is filter and has type integer and NOT repeatable (license, doctype)
                    elif k in ['license', 'content_type', 'content_types', 'collection']:
                        output = {}

                        if type(v) is list:
                            output['id'] = v[0]
                            output['name'] = v[1]
                            output['new_link'] = self._generate_new_link(k, v[0])
                        else:
                            output['name'] = v
                            output['new_link'] = self._generate_new_link(k, v)

                        result[k] = output

                    # If key is filter and has type integer and repeatable (subject, creator, curator, people...)
                    elif k in self.filters and self.filters[k].get('type') == 'integer':
                        output = []
                        for i in v:
                            current = {}

                            if type(i) is list:
                                current['id'] = i[0]
                                current['name'] = i[1]
                                current['new_link'] = self._generate_new_link(k, i[0])
                            else:
                                current['name'] = i
                                current['new_link'] = self._generate_new_link(k, i)

                            output.append(current)
                        result[k] = output

                    else:
                        result[k] = v

                return result

            output = {}
            if collection == 'records':
                for header, values in result.items():
                    output[header] = iterate_node(values)
            else:
                output = iterate_node(result)
            return output

        def format_relations(relations):

            def sort_by_value(list_of_dicts, key_name, default=None):
                decorated = [(dict_.get(key_name, default), dict_) for dict_ in list_of_dicts]
                decorated.sort()
                return [dict_ for (key, dict_) in decorated]

            # NOTE: SITE-SPECIFIK FOR AARHUSTEATER
            onstage = []
            offstage = []
            for rel in relations:
                label = rel.get("rel_label")
                if label.startswith("Skuespiller") and label.find("("):
                    start_index = label.find("(") + 1
                    rel["rel_label"] = label[start_index:-1]
                    onstage.append(rel)
                elif label.startswith("Skuespiller") or label.startswith("Statist"):
                    onstage.append(rel)
                else:
                    offstage.append(rel)

            if collection in ['people']:
                onstage_sorted = sort_by_value(onstage, 'rel_date_from', '2020-12-12')
                offstage_sorted = sort_by_value(offstage, 'rel_date_from', '2020-12-12')
            else:
                onstage_sorted = sort_by_value(onstage, 'rel_label')
                offstage_sorted = sort_by_value(offstage, 'rel_label')

            return [
                {
                    "label": u"Sceneroller",
                    "data": onstage_sorted
                },
                {
                    "label": u"Produktionshold",
                    "data": offstage_sorted
                }
            ]

        def has_references(collection, resource_id):
            # payload = self.get_collection('records',
            #                               query_params=[(collection, resource_id), ('limit', '1')])

            payload = self.get_collection_v2([(collection, resource_id), ('size', '1')])
            # if payload.get('status_code') == 0 and payload.get('result'):
            if payload.get('result'):
                return True
            else:
                return False

        # Request api
        payload = self.service.get_resource(collection, resource_id)

        if payload.get('status_code') == 0:

            # If json-view, no need to process GUI-stuff
            # render_json() will convert the dict back to json before sending to browser
            if fmt == 'json':
                return payload.get('result')

            else:
                response = {}
                response['status_code'] = 0
                response['collection'] = collection
                response['id'] = resource_id

                # Linkify the filter-links and update any deprecated key-names
                response['resource'] = format_metadata(collection, payload.get('result'))

                # If relations, format those as well
                # NOTE: Teater-specifik
                if include_relations and payload['result'].get('relations'):
                    response['resource']['relations'] = format_relations(payload['result'].get("relations"))

                # If an entity, is it referenced in any records.
                # NOTE: Teater-specifik subset af entiteter
                if collection in ["events", "people", "organisations", "creators"]:
                    if collection == 'creators':
                        collection = response['resource'].get("domain")
                    response['is_subject'] = has_references(collection, resource_id)

                # If a possible creator, has it actually created any records?
                # NOTE: Teater-specifik subset af entiteter
                if collection in ["people", "organisations", "creators"]:
                    if collection == 'creators':
                        collection = response['resource'].get("domain")
                    response['is_creator'] = has_references('creators', resource_id)

                return response
        else:
            return payload

    def get_collection(self, collection, query_params=None):

        def process_params(query_params, default_params):
            """Sanitize the query params (multidict) and merge with
            any client-specific default params

            Args:
                query_params (list of tuples): query-params
                default_params (list of tuples): hidden default-params

            Returns:
                Total set of sanitized param-tuples. And flags.
            """

            # Defining putput-vars
            processed_params = []
            start_date = None
            end_date = None
            limit_int = None
            online_only_bool = False
            ids_only_bool = False
            cursor_bool = False

            # If any query-tuples, then satize, set flags
            total_params = list(set(query_params + default_params))
            if total_params:
                # temp-vars
                dateTuple = None
                rangeTuple = None

                # Strip params and set flags
                for t in total_params:
                    if t[1].strip() == "":
                        continue
                    if t[0].strip() == 'date'and len(t[1]) > 3:
                        dateTuple = t
                        # Renamed tuple is added to sanitized_params later
                        continue
                    if t[0].strip() == 'range' and t[1] in ['later', 'earlier']:
                        rangeTuple = t
                        # Renamed tuple is added to sanitized_params later
                        continue
                    if t[0].strip() == 'limit':
                        limit_int = t[1]
                    if t[0].strip() == 'online_only':
                        online_only_bool = True
                    if t[0].strip() == 'ids_only':
                        ids_only_bool = True
                    if t[0].strip() == 'cursor':
                        cursor_bool = t[1]

                    processed_params.append(t)

                # Rename any date-related params
                if dateTuple and rangeTuple:
                    date = dateTuple[1]
                    date_type = rangeTuple[1]
                    if len(date) == 4:
                        date += '-01-01'
                    elif len(date) == 7:
                        date += '-01'
                    elif len(date) != 10:
                        date = date[:3]

                    if date_type == 'earlier':
                        processed_params.append(('end_date', date))
                        end_date = date
                    elif date_type == 'later':
                        processed_params.append(('start_date', date))
                        start_date = date

            return processed_params, limit_int, start_date, end_date, online_only_bool, ids_only_bool, cursor_bool

        def update_keynames(result):

            def update_keys(dictionary):
                output = {}
                latest_keys = {
                    "hierarchical_level": "series",
                    "curator": "curators",
                    "doctype": "content_type",
                    "creator": "creators",
                    "subject": "subjects",
                    "local_tag": "collection_tags",
                    "oas_list": "ids_only",
                    "online_access": "online_only",
                    "location": "locations",
                    "organisation": "organisations",
                    "event": "events",
                    "tag": "tags",
                    "rightsholder": "rightsholders"
                }

                for key, value in dictionary.items():
                    if key in latest_keys:
                        output[latest_keys[key]] = value
                    else:
                        output[key] = value

                return output

            output = []
            for item in result:
                if collection == 'records':
                    # hierarchical metadata
                    hit = {}
                    for header, values in item.items():
                        # Do not format relations - yet
                        if header == 'relations':
                            continue
                        hit[header] = update_keys(values)
                    output.append(hit)

                else:
                    # flat metadata
                    output.append(update_keys(item))
            return output

        def format_next_page_url(url_string, default_params):
            """Remove default-params and omit domain-part of url

            Args:
                url_string (str): The current next_page_url from which to strip domain and any hidden params.
                default_params (list of tuples): Client-specific behind-the-scenes default-params.

            Returns:
                url (str)

            Docs:
                https://docs.python.org/2/library/urllib.html#urllib.urlencode
                http://www.tappister.com/2011/06/python-url-mangling/
                http://stackoverflow.com/questions/3542881/python-opposite-function-urllib-urlencode
            """

            # parse string into url-parts
            parsed_url = urlparse.urlparse(url_string)
            # generate list of param-tuples from query-part of url
            # NOTE: str-wrapping is necessary - don't know why
            query_params = urlparse.parse_qsl(str(parsed_url.query))
            # Remove any present default-param-tuples
            for tup in default_params:
                if tup in query_params:
                    query_params.remove(tup)
            # Re-encode into query-string
            querystring = urllib.urlencode(query_params)
            # Return path and query-parts
            return '?'.join([parsed_url.path, querystring])

        def format_resolved_params(resolved_params, default_params):
            for tup in default_params:
                if tup[0] in resolved_params.keys():
                    if resolved_params[tup[0]].get(tup[1]):
                        resolved_params[tup[0]].pop(tup[1])
                        if not resolved_params[tup[0]]:
                            resolved_params.pop(tup[0])

            return resolved_params

        def generate_limits(params=None, limit=None):
            limit_options = ['10', '20', '100']
            non_limit_params = [(t[0], t[1]) for t in params if t[0] != 'limit']
            output = []

            for e in limit_options:
                current = {}
                current['name'] = e
                if limit and (e == limit):
                    current['selected'] = True
                elif not limit and (e == '10'):
                    current['selected'] = True
                else:
                    current['add_link'] = self._urlencode(non_limit_params + [('limit', e)])
                output.append(current)

            return output

        def generate_filters(client_params, resolved_params=None):
            # query_params er en set-liste af tuples med paramkeys og -values
            # resolved_params er en dict af key-dics. Hvor hver key-dict har dicts med param-vals som key og
            # display_label som value
            output = []

            def trim_value(value):
                # remove leading zeros
                try:
                    value = str(int(value))
                except ValueError:
                    pass
                return value

            for tup in client_params:
                key = tup[0]
                value = trim_value(tup[1])

                if key in self.filters and self.filters[key]['filter'] is True:
                    current_filter = {'name': key, 'value': value}

                    # GENERATE REMOVE-LINK
                    if key == 'collection':
                        new_params = [(e[0], e[1]) for e in client_params if e != tup and e[0] in self.filters and
                            e[0] != 'series']
                    else:
                        new_params = [(e[0], e[1]) for e in client_params if e != tup and e[0] in self.filters]
                    current_filter['remove_link'] = self._urlencode(new_params)

                    # GENERATE VIEW-LINK
                    if self.filters[key]['type'] == 'integer':
                        current_filter['view_link'] = self.filters[key]['endpoint'] + '/' + value

                    # GENERATE DISPLAY_LABEL
                    if resolved_params and key in resolved_params.keys():
                        current_filter['display_label'] = resolved_params[key][value]
                    elif self.filters[key]['type'] == 'boolean':
                        current_filter['display_label'] = self.filters[key]['display_label']
                    else:
                        current_filter['display_label'] = value

                    output.append(current_filter)

            return output

        # Process query_params and default_params - renaming and looking for flags
        total_params, limit_int, start_date, end_date, online_only_bool, \
            ids_only_bool, cursor_bool = process_params(query_params, self.default_params)

        # Request api
        payload = self.service.get_collection(collection, total_params)

        if payload.get('status_code') == 0:

            # temp-vars
            resolved_params = None
            processed_query_params = [x for x in total_params if x not in self.default_params]

            # Start building response
            response = {}
            response['status_code'] = 0
            response['collection'] = collection

            # Return response with updated keynames, if full response
            if ids_only_bool:
                response['result'] = payload.get('result')
            else:
                response['result'] = update_keynames(payload.get('result'))

            if start_date:
                response['start_date'] = start_date

            if end_date:
                response['end_date'] = end_date

            if online_only_bool:
                response['online_only'] = online_only_bool

            # If the request includes a cursor, there must be a previous result-page
            if cursor_bool:
                response['previous_page'] = 'javascript:history.back()'

            # If hidden default_params, remove them from "resolved_params" and "next_page_url"
            if self.default_params and payload.get('resolved_params'):
                resolved_params = format_resolved_params(payload.get('resolved_params'), self.default_params)

            # Remove domain-part - and if hidden default_params, remove them
            if payload.get('next_page_url'):
                response['next_page'] = format_next_page_url(payload.get('next_page_url'), self.default_params)

            # Generate filters from query_params
            if processed_query_params:
                response['filters'] = generate_filters(processed_query_params, resolved_params)

            # Generate limit-links if any results
            if response['result']:
                response['limits'] = generate_limits(processed_query_params, limit_int)

            return response

        else:
            return payload

    def get_collection_v2(self, query_params=[]):
        # SEARCH-PAGE
        default_params = [('curators', "4"), ('fmt', 'json')]
        api_response = self.service.get_collection_v2(list(set().union(default_params, query_params)))

        # Remove irrelevant filters
        if api_response.get('filters'):
            for idx, el in enumerate(api_response.get('filters')):
                if el.get('key') not in self.filters:
                    api_response['filters'].pop(idx)

        if not api_response.get("errors"):
            return {
                "status_code": 0,
                "previous": api_response.get("previous"),
                "next": api_response.get("next"),
                "size_list": api_response.get("size_list"),
                "result": api_response.get("result")
            }
        else:
            return {
                "status_code": 1,
                "msg": api_response.get("errors")
            }
        # return api_response

    def create_relation(self, post_params):
        """Create relation between two entities

        Args:
            query_params (list of tuples): webapp2 post-params

        Returns:
            payload (dict)
        """
        return self.service.insert_relation(post_params)

    def update_resource(self, collection, resource_id, post_params):
        return self.service.update_resource(collection, resource_id, post_params)

    def delete_resource(self, collection, resource_id):
        if collection == 'relations':
            return self.service.delete_relation(resource_id)

    def autocomplete(self, q):
        """Queries autocomplete

        Args:
            query_params (list of tuples): Tuplelist of key-value params.
            decode (boolean): utf8-decode before http-request.

        Returns:
            boolean: True if successful, False otherwise.
            payload: response
        """
        # return self.service.autocomplete([('t', q), ('limit', '20')], decode=False)
        return self.service.autocomplete([('t', q), ('auto_group', '2'), ('limit', '25')], decode=False)

    def populate_schema(self, schema, data):
        # TODO - doesn't handle arrays
        def recursive(props, data):
            for key, values in props.items():
                if data.get(key):
                    prop_type = values.get("type")
                    if prop_type == 'object':
                        recursive(values.get("properties"), data.get(key))
                    else:
                        values["_value"] = data.get(key)
                else:
                    continue

            # return schema

        recursive(schema.get("properties"), data)
        return schema
        # if schema['properties'].get('additionalProperties'):

    def populate_schema_v2(self, schema, resource):
        # TODO - doesn't handle arrays!!
        def recursive(props, resource):
            for key, values in props.items():
                if resource.get(key):
                    if values.get('type') == 'object':
                        recursive(values.get("properties"), resource.get(key))
                    else:
                        values["_value"] = resource.get(key)
                else:
                    continue

            # Finish each recursive call with adding non-schema keys to
            # current level of properties
            for key, value in resource.items():
                if key not in props:
                    if value is None:
                        continue
                    else:
                        if isinstance(value, list):
                            val_type = 'array'
                        elif isinstance(value, dict):
                            val_type = 'object'
                        elif isinstance(value, bool):
                            val_type = 'boolean'
                        elif isinstance(value, int):
                            val_type = 'number'
                        elif isinstance(value, float):
                            val_type = 'number'
                        else:
                            val_type = 'string'

                        props[key] = {'_value': value, 'type': val_type}

        # Relations skal ikke inkluderes i formularen
        resource.pop('relations', None)

        # Hvis mand, fjern pigenavn
        # if resource.get('gender') == 'mand':
        #     resource.pop('birthname', None)
        #     schema['properties'].pop('birthname')

        recursive(schema.get("properties"), resource)
        return schema




    def generate_facets(self, query_params=None):

        def generate_facet(facet_file, facet_name, query_params=None):

            def recursive(facet_obj, filterParams):
                repeatable = self.filters[facet_name].get('repeatable')
                for item in facet_obj:
                    if self.filters[facet_name].get('endpoint') == 'literal':
                        currentParam = (facet_name, item.get('display_label'))
                    else:
                        currentParam = (facet_name, item.get('id'))

                    if filterParams:
                        if currentParam in filterParams:
                            item['remove_link'] = self._generate_remove_link(filterParams, currentParam)
                        else:
                            item['add_link'] = self._generate_add_link(filterParams, currentParam,
                                                repeatable=repeatable)
                    else:
                        item['add_link'] = self._generate_add_link(currentFilters=None, newFilter=currentParam,
                                            repeatable=repeatable)

                    if item.get('children'):
                        recursive(item['children'], filterParams)

                return facet_obj

            if query_params:
                filterParams = [(e[0], e[1]) for e in query_params if e[0] in self.filters]
            else:
                filterParams = None

            return recursive(facet_file, filterParams)

        output = {}
        for facet in self.facets:
            url = '/'.join([self.host, facet.get('facet_file')])
            # url = '/'.join(["http://localhost:16080", facet.get('facet_file')])
            facet_file = self.service.get_static_resource(url)
            output[facet.get('facet_label')] = generate_facet(facet_file, facet.get('facet_field'), query_params)

        return output

    # PRIVATE GENERIC METHODS
    def _generate_new_link(self, key, value=None):
        """Takes one dict of key(s) and value(s) OR two strings"""
        if value:
            return self._urlencode({key: value})
        else:
            return self._urlencode(key)

    def _generate_add_link(self, currentFilters, newFilter, repeatable=False):
        """
        Takes a list of sanitized filter-tuples AND a single new tuple
        Returns a safe querystring
        """
        if currentFilters is None:
            output = []
        else:
            output = currentFilters[:]

        if not repeatable:
            for tup in output:
                if tup[0] == newFilter[0]:
                    output.remove(tup)
        output.append(newFilter)
        return self._urlencode(output)

    def _generate_remove_link(self, query_params, remove_param):
        """
        Removes param from list of params and return urlencoded string
        """
        return urllib.urlencode(query_params - remove_param)

    def _urlencode(self, params, decode=True):
        path = {}
        if type(params) == dict:
            iterable = params.items()
        else:
            iterable = params
        for key, value in iterable:

            if key in path:
                path[key] += ';' + value
            else:
                path[key] = value

        encoded = urllib.urlencode(path)
        if decode:
            return encoded.decode('utf-8')
        else:
            return encoded
