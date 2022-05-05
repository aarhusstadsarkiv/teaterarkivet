# Aarhus Teater Arkiv

## Datamodel
The client.py module must always publish data in the following form:

```
{
    "data": list or dict of {"id", "type"...}
    "errors": list of {"code", "source", "detail"}
    "links": dict of links, most often pagination links
    "meta": dict if necessary extra info is needed
}
```