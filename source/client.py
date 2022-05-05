import json

from starlette.datastructures import QueryParams, URL, FormData
from . import settings, utils
from .resources import client


def get_collection(query_params: QueryParams = None) -> dict:
    # json-format needed to get aarhusarkivet to ship json
    default_params = [("curators", "4"), ("fmt", "json")]
    params = list(set().union(default_params, query_params.multi_items()))
    # hacky due to differences in json-dict between oaws and aarhusarkivet
    try:
        resp = client.get("https://www.aarhusarkivet.dk/search", params=params)
        resp.raise_for_status()
    except Exception as e:
        return {"status_code": resp.status_code, "status_msg": str(e)}

    # Remove irrelevant filters
    content = resp.json()

    if content.get("filters"):
        for idx, el in enumerate(content.get("filters")):
            if el.get("key") not in settings.FILTERS:
                content["filters"].pop(idx)

    content["status_code"] = 0
    return content


def get_record(record_id: int, json: bool = False) -> dict:
    """Fetch a single record.

    Args:
        record_id (int): The id of the resource.
        json (bool): Defaults to False. Set to True to get json

    Returns:
        dict: error-dict or resource-dict
    """

    def format_metadata(resource: dict):
        result = {}

        for k, v in resource.items():

            if k == "representations":
                result[k] = v

            elif k == "series":
                output = []
                currentLevel = []
                urlpath = {}

                if resource.get("collection"):
                    urlpath["collection"] = resource["collection"].get("id")

                for i in v.split("/"):
                    level = {}
                    currentLevel.append(i)
                    urlpath["series"] = "/".join(currentLevel)
                    level["label"] = i
                    level["new_link"] = utils.generate_new_link(urlpath)
                    output.append(level)
                result[k] = output

            elif k in ["date_from", "date_to"]:
                item = {}
                item["label"] = k
                item["date"] = v
                item["new_link"] = utils.generate_new_link(k, v)
                result[k] = item

            # If key is list of simple strings
            elif k in ["admin_tags", "collection_tags"]:
                output = []
                for idx in v:
                    item = {}
                    item["label"] = idx
                    item["new_link"] = utils.generate_new_link(k, idx)
                    output.append(item)
                result[k] = output

            elif k in ["resources"]:
                result[k] = v

            elif type(v) is dict:
                output = {}
                output["id"] = v.get("id")
                output["label"] = v.get("label")
                output["new_link"] = utils.generate_new_link(k, v.get("id"))
                result[k] = output

            elif isinstance(v, list) and k in settings.FILTERS:
                output = []

                for _dict in v:
                    # hierarchical concept or entity
                    if isinstance(_dict.get("id"), list):
                        hierarchy = []
                        for i, v in enumerate(_dict.get("id")):
                            item = {}
                            item["id"] = v
                            item["label"] = _dict.get("label")[i]
                            item["new_link"] = "=".join([k, str(v)])
                            hierarchy.append(item)
                        output.append(hierarchy)

                    # flat concept or entity
                    else:
                        _id = _dict.get("id")
                        label = _dict.get("label")
                        item = {}
                        item["id"] = _id
                        item["label"] = label
                        item["new_link"] = utils.generate_new_link(k, _id)
                        output.append(item)

                result[k] = output

            else:
                result[k] = v
        return result

    try:
        r = client.get(f"https://openaws.appspot.com/records_v3/{record_id}")
        r.raise_for_status()
    except Exception as e:
        return {"status_code": r.status_code, "status_msg": str(e)}

    payload: dict = r.json()
    if payload["status_code"] != 0:
        return payload
    if json:
        return payload.get("result")

    d = {}
    d["status_code"] = 0
    d["collection"] = "records"
    d["operation"] = "view"
    d["id"] = record_id

    # Linkify the filter-links and update any deprecated key-names
    d["resource"] = format_metadata(payload.get("result"))
    return d


def get_resource(
    collection: str, id: int, include_relations: bool = True, json: bool = False
) -> dict:
    """Fetch a single resource (person or event)

    Args:
        collection (str): 'people' or 'events'
        id (int): id of resource
        include_relations (boolean): Defaults to True
        json (bool): Defaults to False. Set to True to get json

    Returns:
        dict: error-dict or resource-dict
    """

    def format_relations(relations):
        def sort_by_value(list_of_dicts, key_name, default=None):
            decorated = [
                (dict_.get(key_name, default), dict_) for dict_ in list_of_dicts
            ]
            return [dict_ for (key, dict_) in decorated]

        # NOTE: SITE-SPECIFIK FOR AARHUSTEATER
        onstage = []
        offstage = []
        for rel in relations:
            label: str = rel.get("rel_label")
            if label.startswith("Skuespiller") and label.find("("):
                start_index = label.find("(") + 1
                rel["rel_label"] = label[start_index:-1]
                onstage.append(rel)
            elif label.startswith("Skuespiller") or label.startswith("Statist"):
                onstage.append(rel)
            else:
                offstage.append(rel)

        if collection in ["people"]:
            onstage_sorted = sort_by_value(onstage, "rel_date_from", "2020-12-12")
            offstage_sorted = sort_by_value(offstage, "rel_date_from", "2020-12-12")
        else:
            onstage_sorted = sort_by_value(onstage, "rel_label")
            offstage_sorted = sort_by_value(offstage, "rel_label")

        return [
            {"label": "Sceneroller", "data": onstage_sorted},
            {"label": "Produktionshold", "data": offstage_sorted},
        ]

    def has_references(collection: str, id: int):
        query_params = {
            collection: str(id),
            "curators": "4",
            "fmt": "json",
            "size": "1",
        }
        try:
            r = client.get("https://www.aarhusarkivet.dk/search", params=query_params)
            r.raise_for_status()
        except Exception as e:
            return False

        resource: dict = r.json()
        if resource.get("result"):
            return True
        return False

    # Fetch resource
    try:
        r = client.get(f"https://openaws.appspot.com/entities/{id}")
        r.raise_for_status()
    except Exception as e:
        return {"status_code": r.status_code, "status_msg": str(e)}

    # Test status_code from oaws-response
    json_response: dict = r.json()
    if json_response["status_code"] != 0:
        return json_response

    resource: dict = json_response.get("result")
    if json:
        return resource

    out = {}
    out["status_code"] = 0
    out["collection"] = collection
    out["id"] = id

    # NOTE: Teater-specific stuff. If relations, format those as well
    if include_relations:
        url = f"https://openaws.appspot.com/relations?f_id={id}"
        r = client.get(url)
        if r.status_code == 200:
            # If succesful request that has relations-content
            resp = r.json()
            if resp["status_code"] == 0 and resp.get("result"):
                resource["relations"] = format_relations(resp.get("result"))

    if collection == "creators":
        collection = resource.get("domain")
    out["is_subject"] = has_references(collection, id)
    if collection == "people":
        out["is_creator"] = has_references("creators", id)

    out["resource"] = resource

    return out


def create_relation(form: FormData) -> dict:
    def generate_relation(datalist: FormData):
        print("Datalist passed to generate_relation:\n", flush=True)
        print(datalist, flush=True)

        subject_id = (
            subject_domain
        ) = object_id = object_domain = rel_label = rel_start = rel_end = None

        for tup in datalist.multi_items():
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

        if subject_id and subject_domain and object_id and object_domain and rel_label:

            if subject_domain == "people" and object_domain == "events":
                rel_base_type = 7
                object_url = f"https://openaws.appspot.com/entities/{object_id}"
                try:
                    rel_start, rel_end = get_dates(object_url)
                except Exception:
                    return False
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
            print("returning False from generate_relation()", flush=True)
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

    def get_dates(url: URL):
        r = client.get(url, follow_redirects=True)
        print(f"get_dates() request return status_code: {r.status_code}", flush=True)
        r.raise_for_status()
        entity: dict = r.json()
        date_from = entity.get("date_from")
        date_to = entity.get("date_to")
        return [date_from, date_to]

    relation = generate_relation(form)
    if relation:
        reverse = generate_reverse_relation(relation)

        url = "https://openaws.appspot.com/relation_tools"
        payload: dict = {
            "token": settings.config("API_KEY", cast=str),
            "operation": "create",
            "data": json.dumps({"rel_data": [relation, reverse]}),
        }
        headers: dict = {"Content-Type": "application/x-www-form-urlencoded"}

        r = client.post(url, data=payload, headers=headers)
        try:
            response_to_dict = r.json()
            return response_to_dict
        except ValueError as e:
            return {"status_code": 5, "status_msg": e}
    else:
        return {"status_code": 5, "status_msg": "Unable to generate relation."}


def delete_relation(id: int) -> dict:
    url = "https://openaws.appspot.com/relation_tools"
    payload: dict = {
        "token": settings.config("API_KEY", cast=str),
        "operation": "remove",
        "data": json.dumps({"rel_id": int(id)}),
    }
    headers: dict = {"Content-Type": "application/x-www-form-urlencoded"}

    r = client.post(url, data=payload, headers=headers)
    try:
        response_to_dict = r.json()
        return response_to_dict
    except ValueError as e:
        return {"status_code": 5, "status_msg": e}


def autocomplete(term: str) -> dict:
    """Queries autocomplete from aarhusiana

    Args:
        term (str): string-value of 'q'

    Returns:
        payload (list)
    """
    query_params: dict = {"t": term, "auto_group": "2", "limit": "25"}
    url: str = "https://aarhusiana.appspot.com/autocomplete_v3"
    response = client.get(url, params=query_params, follow_redirects=True, timeout=10)
    return response.json()
