import urllib.parse

from . import settings


def generate_add_link(currentFilters, newFilter, repeatable=False):
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
    # return _urlencode(output)
    return urllib.parse.urlencode(output)


def generate_remove_link(query_params, remove_param):
    """
    Removes param from list of params and return urlencoded string
    """
    return urllib.parse.urlencode(query_params - remove_param)


def generate_new_link(key, value=None):
    """Takes one dict of key(s) and value(s) OR two strings"""
    if value:
        return urllib.parse.urlencode({key: value})
    else:
        return urllib.parse.urlencode(key)


def generate_facets(query_params=None):
    def generate_facet(facet_file, facet_name, query_params=None):
        def recursive(facet_obj, filterParams):
            repeatable = settings.FILTERS[facet_name].get("repeatable")
            for item in facet_obj:
                if settings.FILTERS[facet_name].get("endpoint") == "literal":
                    currentParam = (facet_name, item.get("display_label"))
                else:
                    currentParam = (facet_name, item.get("id"))

                if filterParams:
                    if currentParam in filterParams:
                        item["remove_link"] = generate_remove_link(
                            filterParams, currentParam
                        )
                    else:
                        item["add_link"] = generate_add_link(
                            filterParams, currentParam, repeatable=repeatable
                        )
                else:
                    item["add_link"] = generate_add_link(
                        currentFilters=None,
                        newFilter=currentParam,
                        repeatable=repeatable,
                    )

                if item.get("children"):
                    recursive(item["children"], filterParams)

            return facet_obj

        if query_params:
            filterParams = [
                (e[0], e[1]) for e in query_params if e[0] in settings.FILTERS
            ]
        else:
            filterParams = None

        return recursive(facet_file, filterParams)

    out = {}
    for facet in settings.FACETS:
        label = facet.get("label")
        structure = facet.get("structure")
        field = facet.get("field")
        out[label] = generate_facet(structure, field, query_params)

    return out
