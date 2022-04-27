from pathlib import Path
from starlette.config import Config

config = Config(".env")

DEBUG = config("DEBUG", cast=bool, default=False)

HTTPS_ONLY = config("HTTPS_ONLY", cast=bool, default=True)

SECRET = config("SECRET", cast=str)

BASE_DIR = Path(__file__).parent.parent

TEMPLATES_DIR = BASE_DIR / "templates"

STATIC_DIR = BASE_DIR / "static"

CLIENT = {
    "api_key": config("API_KEY"),
    "title": "Aarhus Teaters Arkiv",
    "name": "aarhusteater",
    "description": "Aarhus Teater arkiv og historie",
    "host": "https://aarhusteaterarkiv-web.appspot.com",
    # Contact info
    "homepage": "https://www.aarhusteater.dk/om-teatret/om-huset/",
    "telephone": "+45 89 33 23 59",
    "mail": "arkivar@aarhusteater.dk",
    "address": "Teatergaden 1, 8000 Aarhus C",
    "map": "https://www.openstreetmap.org/way/51265304",
    "facebook": "https://www.facebook.com/Teaterarkivaren",
    # View settings
    "excluded_query_params": [],
    "excluded_keys": [
        "identification",
        "admin_tags",
        "organisations",
        "programme",
        "poster",
        "curators",
        "locations",
    ],
    # Query settings
    "curator": "Aarhus Teater Arkiv",
    "default_query_params": [("curators", "4")],
    "collections": [
        "records",
        "events",
        "people",
        "organisations",
        "poster",
        "programme",
        "collections",
        "creators",
        "relations",
    ]
}

FILTERS = {
    "creators": {
        "display_label": "Skaber",
        "repeatable": True,
        "type": "integer",
        "endpoint": "creators",
        "filter": True,
    },
    "locations": {
        "display_label": "Stedsangivelse",
        "repeatable": True,
        "type": "integer",
        "endpoint": "locations",
        "filter": True,
    },
    "events": {
        "display_label": "Forestilling",
        "repeatable": True,
        "type": "integer",
        "endpoint": "events",
        "filter": True,
    },
    "people": {
        "display_label": "Person",
        "repeatable": True,
        "type": "integer",
        "endpoint": "people",
        "filter": True,
    },
    "organisations": {
        "display_label": "Organisation",
        "repeatable": True,
        "type": "integer",
        "endpoint": "organisations",
        "filter": True,
    },
    "collection": {
        "display_label": "Samling",
        "repeatable": False,
        "type": "integer",
        "endpoint": "collections",
        "filter": True,
    },
    "start_date": {
        "display_label": "Startdato",
        "repeatable": False,
        "type": "string",
        "endpoint": "literal",
        "filter": True,
    },
    "end_date": {
        "display_label": "Slutdato",
        "repeatable": False,
        "type": "string",
        "endpoint": "literal",
        "filter": True,
    },
    "subjects": {
        "display_label": "Emnekategori",
        "repeatable": True,
        "type": "integer",
        "endpoint": "subjects",
        "filter": True,
    },
    "series": {
        "display_label": "Serie",
        "repeatable": False,
        "type": "string",
        "endpoint": "literal",
        "filter": True,
    },
    "tags": {
        "display_label": "Tag",
        "repeatable": True,
        "type": "integer",
        "endpoint": "tags",
        "filter": True,
    },
    "collection_tags": {
        "display_label": "Samlingstags",
        "repeatable": True,
        "type": "string",
        "endpoint": "literal",
        "filter": True,
    },
    "content_type": {
        "display_label": "Arkivalietype",
        "repeatable": False,
        "type": "integer",
        "endpoint": "content_types",
        "filter": True,
    },
    "content_types": {
        "display_label": "Arkivalietype",
        "repeatable": True,
        "type": "integer",
        "endpoint": "content_types",
        "filter": True,
    },
    "license": {
        "display_label": "Brugslicens",
        "repeatable": False,
        "type": "integer",
        "endpoint": "licenses",
        "filter": True,
    },
    "online_only": {
        "display_label": "Kun online arkivalier",
        "repeatable": False,
        "type": "boolean",
        "endpoint": "system",
        "filter": True,
    },
    "limit": {
        "display_label": "Hits per side",
        "repeatable": False,
        "type": "literal",
        "endpoint": "system",
        "filter": False,
    },
    "admin_tags": {
        "display_label": "Administrative tags",
        "repeatable": True,
        "type": "string",
        "endpoint": "literal",
        "filter": True,
    }
}

FACETS = [
    {
        "label": "Forestillinger",
        "field": "series",
        "structure": [
            {
                "display_label": "Sæson 1900-01",
                "children": [
                {
                    "display_label": "Erasmus Montanus",
                    "id": "111818"
                },
                {
                    "display_label": "Prinsessen på ærten",
                    "id": "112045"
                },
                {
                    "display_label": "Nej",
                    "id": "111978"
                },
                {
                    "display_label": "Sparekassen",
                    "id": "112124"
                },
                {
                    "display_label": "Harlekins Omvendelse",
                    "id": "112316"
                },
                {
                    "display_label": "En Tilståelse",
                    "id": "112157"
                },
                {
                    "display_label": "Et Sølvbryllup",
                    "id": "112158"
                },
                {
                    "display_label": "Den indbildt syge",
                    "id": "112357"
                },
                {
                    "display_label": "Anna Raage",
                    "id": "111710"
                },
                {
                    "display_label": "Genboerne",
                    "id": "118165"
                },
                {
                    "display_label": "Guldhornene",
                    "id": "153767"
                },
                {
                    "display_label": "Amoriner",
                    "id": "111705"
                },
                {
                    "display_label": "Den krøllede Fritz",
                    "id": "153768"
                },
                {
                    "display_label": "Et dukkehjem",
                    "id": "153500"
                },
                {
                    "display_label": "Redaktionssekretæren",
                    "id": "112052"
                },
                {
                    "display_label": "Correggio",
                    "id": "111767"
                },
                {
                    "display_label": "Arbejderliv",
                    "id": "111715"
                },
                {
                    "display_label": "César Girodots Testamente",
                    "id": "111757"
                },
                {
                    "display_label": "Wuthhorn",
                    "id": "112238"
                },
                {
                    "display_label": "Da han var ung",
                    "id": "111768"
                },
                {
                    "display_label": "Capriciosa eller Familien i Nyboder",
                    "id": "111754"
                },
                {
                    "display_label": "En Bryllupsdag",
                    "id": "111738"
                },
                {
                    "display_label": "Gamle Minder",
                    "id": "112266"
                },
                {
                    "display_label": "Bæverskindspelsen",
                    "id": "111752"
                },
                {
                    "display_label": "Feriegæsterne",
                    "id": "111855"
                },
                {
                    "display_label": "Kvinder",
                    "id": "112411"
                },
                {
                    "display_label": "Den hvide handske",
                    "id": "118146"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "111892"
                },
                {
                    "display_label": "Tordenskjold",
                    "id": "112171"
                },
                {
                    "display_label": "Meer end Perler og Guld",
                    "id": "111946"
                },
                {
                    "display_label": "Thummelumsen",
                    "id": "112190"
                },
                {
                    "display_label": "Søstre",
                    "id": "112169"
                },
                {
                    "display_label": "Maria Magdalene",
                    "id": "111941"
                },
                {
                    "display_label": "Inden Døre",
                    "id": "112361"
                }
                ]
            },
            {
                "display_label": "Sæson 1901-02",
                "children": [
                {
                    "display_label": "Frøken Nitouche",
                    "id": "111893"
                },
                {
                    "display_label": "Genboerne",
                    "id": "112281"
                },
                {
                    "display_label": "Inden Døre",
                    "id": "112362"
                },
                {
                    "display_label": "Intrigerne",
                    "id": "112762"
                },
                {
                    "display_label": "Sommerfuglevinger",
                    "id": "118287"
                },
                {
                    "display_label": "En Bryllupsdag",
                    "id": "111739"
                },
                {
                    "display_label": "Kvinder",
                    "id": "112412"
                },
                {
                    "display_label": "Den hvide handske",
                    "id": "118147"
                },
                {
                    "display_label": "Den indbildt syge",
                    "id": "150041"
                },
                {
                    "display_label": "Dalgas-Hymne",
                    "id": "153772"
                },
                {
                    "display_label": "Dalgas",
                    "id": "153774"
                },
                {
                    "display_label": "Anna Raage",
                    "id": "150042"
                },
                {
                    "display_label": "Fra Lyngens Land",
                    "id": "118112"
                },
                {
                    "display_label": "Mester og Lærling",
                    "id": "111947"
                },
                {
                    "display_label": "For Alvor",
                    "id": "111871"
                },
                {
                    "display_label": "Wolle Krogh",
                    "id": "112235"
                },
                {
                    "display_label": "Det lykkelige skibbrud",
                    "id": "111922"
                },
                {
                    "display_label": "Mara",
                    "id": "111940"
                },
                {
                    "display_label": "Et Sølvbryllup",
                    "id": "120609"
                },
                {
                    "display_label": "Formående Venner",
                    "id": "111875"
                },
                {
                    "display_label": "Kabale og Kærlighed",
                    "id": "112391"
                },
                {
                    "display_label": "En ægteskabsfjende",
                    "id": "112243"
                },
                {
                    "display_label": "Julestuen",
                    "id": "112384"
                },
                {
                    "display_label": "Man tænker da først på sig selv",
                    "id": "111939"
                },
                {
                    "display_label": "Adolf og Henriette",
                    "id": "118113"
                },
                {
                    "display_label": "Hakon Jarl",
                    "id": "112305"
                },
                {
                    "display_label": "Mikadoen",
                    "id": "111949"
                },
                {
                    "display_label": "Tordenvejr",
                    "id": "112175"
                },
                {
                    "display_label": "Elverhøj",
                    "id": "111809"
                },
                {
                    "display_label": "Agnes Jordan",
                    "id": "111694"
                },
                {
                    "display_label": "Den forbudne Frugt",
                    "id": "118115"
                },
                {
                    "display_label": "Kameliadamen",
                    "id": "118143"
                },
                {
                    "display_label": "Sherlock Holmes",
                    "id": "112081"
                },
                {
                    "display_label": "Nemesis",
                    "id": "111981"
                },
                {
                    "display_label": "Lad os skilles",
                    "id": "118189"
                },
                {
                    "display_label": "Pak",
                    "id": "112025"
                },
                {
                    "display_label": "Røverne",
                    "id": "112073"
                },
                {
                    "display_label": "En Forlovelse",
                    "id": "111874"
                },
                {
                    "display_label": "Fru Mimi",
                    "id": "111887"
                }
                ]
            },
            {
                "display_label": "Sæson 1902-03",
                "children": [
                {
                    "display_label": "Erasmus Montanus",
                    "id": "111819"
                },
                {
                    "display_label": "Fru Mimi",
                    "id": "111888"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "111894"
                },
                {
                    "display_label": "Genboerne",
                    "id": "112282"
                },
                {
                    "display_label": "Den indbildt syge",
                    "id": "112358"
                },
                {
                    "display_label": "Lad os skilles",
                    "id": "112430"
                },
                {
                    "display_label": "Røverne",
                    "id": "118192"
                },
                {
                    "display_label": "Gnisten",
                    "id": "118222"
                },
                {
                    "display_label": "Soldaterløjer",
                    "id": "112110"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "112372"
                },
                {
                    "display_label": "De stille Stuer",
                    "id": "112138"
                },
                {
                    "display_label": "En Bryllupsaften",
                    "id": "111736"
                },
                {
                    "display_label": "Eventyr på fodrejsen",
                    "id": "111830"
                },
                {
                    "display_label": "Håbet",
                    "id": "112302"
                },
                {
                    "display_label": "Orfeus i Underverdenen",
                    "id": "112014"
                },
                {
                    "display_label": "Den gamle Pavillon",
                    "id": "112267"
                },
                {
                    "display_label": "Dronning Margareta",
                    "id": "111793"
                },
                {
                    "display_label": "Moderate Løjer",
                    "id": "111959"
                },
                {
                    "display_label": "En Fallit",
                    "id": "111839"
                },
                {
                    "display_label": "En spurv i tranedans",
                    "id": "112130"
                },
                {
                    "display_label": "En Vilje",
                    "id": "112231"
                },
                {
                    "display_label": "Tak",
                    "id": "118174"
                },
                {
                    "display_label": "Hedda Gabler",
                    "id": "118168"
                },
                {
                    "display_label": "Kong Erik og de Fredløse",
                    "id": "112407"
                },
                {
                    "display_label": "Hans Højhed",
                    "id": "112309"
                },
                {
                    "display_label": "Flachsmanns Skole",
                    "id": "111859"
                },
                {
                    "display_label": "Cornevilles Klokker",
                    "id": "111765"
                },
                {
                    "display_label": "Advokat Scarli",
                    "id": "111690"
                },
                {
                    "display_label": "Hjemme igen",
                    "id": "112329"
                },
                {
                    "display_label": "Teaterbanditterne",
                    "id": "118220"
                },
                {
                    "display_label": "Brødre",
                    "id": "111740"
                },
                {
                    "display_label": "Gæsteoptræden af Koncertsangerinde Fru Holstein-Berg",
                    "id": "154127"
                }
                ]
            },
            {
                "display_label": "Sæson 1903-04",
                "children": [
                {
                    "display_label": "En Bryllupsaften",
                    "id": "111737"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "111895"
                },
                {
                    "display_label": "Et Sølvbryllup",
                    "id": "112159"
                },
                {
                    "display_label": "Håbet",
                    "id": "112303"
                },
                {
                    "display_label": "Hans Højhed",
                    "id": "112310"
                },
                {
                    "display_label": "Maskerade",
                    "id": "112786"
                },
                {
                    "display_label": "Kameliadamen",
                    "id": "118172"
                },
                {
                    "display_label": "Gøngehøvdingen",
                    "id": "118223"
                },
                {
                    "display_label": "En fløjtesolo",
                    "id": "118240"
                },
                {
                    "display_label": "Lykkebarnet",
                    "id": "111920"
                },
                {
                    "display_label": "Grøns Fødselsdag",
                    "id": "118227"
                },
                {
                    "display_label": "De fattiges Dyrehave",
                    "id": "111850"
                },
                {
                    "display_label": "En Guldbryllupsaften",
                    "id": "112288"
                },
                {
                    "display_label": "Røverne",
                    "id": "112074"
                },
                {
                    "display_label": "Fangen paa Zenda",
                    "id": "111847"
                },
                {
                    "display_label": "Geografi og kærlighed",
                    "id": "153502"
                },
                {
                    "display_label": "Baldevins bryllup",
                    "id": "153503"
                },
                {
                    "display_label": "En Skandale",
                    "id": "112088"
                },
                {
                    "display_label": "En Forbryder",
                    "id": "111873"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "111992"
                },
                {
                    "display_label": "Gamle Ungkarle",
                    "id": "112274"
                },
                {
                    "display_label": "Svend Dyrings Hus",
                    "id": "112153"
                },
                {
                    "display_label": "Hverdagsfolk",
                    "id": "112341"
                },
                {
                    "display_label": "Madkærester",
                    "id": "111933"
                },
                {
                    "display_label": "Højgaards Pensionat",
                    "id": "112347"
                },
                {
                    "display_label": "Tante Cramers Testamente",
                    "id": "112174"
                },
                {
                    "display_label": "Flagermusen",
                    "id": "111860"
                },
                {
                    "display_label": "Under Snefog",
                    "id": "112209"
                },
                {
                    "display_label": "Den kære familie",
                    "id": "112414"
                },
                {
                    "display_label": "Forretning er Forretning",
                    "id": "111876"
                },
                {
                    "display_label": "De to Armringe",
                    "id": "112168"
                },
                {
                    "display_label": "De Usynlige",
                    "id": "112219"
                },
                {
                    "display_label": "Guldkareten",
                    "id": "118152"
                },
                {
                    "display_label": "Brødre",
                    "id": "111741"
                },
                {
                    "display_label": "Brødre",
                    "id": "154134"
                },
                {
                    "display_label": "Oplæsning ved Herman Bang",
                    "id": "154135"
                },
                {
                    "display_label": "Guldkareten",
                    "id": "118152"
                },
                {
                    "display_label": "Operasanger Frederik Brun og Fru Johanne Brun",
                    "id": "154138"
                }
                ]
            },
            {
                "display_label": "Sæson 1904-05",
                "children": [
                {
                    "display_label": "Frøken Nitouche",
                    "id": "111896"
                },
                {
                    "display_label": "De Usynlige",
                    "id": "112220"
                },
                {
                    "display_label": "Genboerne",
                    "id": "112283"
                },
                {
                    "display_label": "Den kære familie",
                    "id": "112415"
                },
                {
                    "display_label": "Ungdomsleg",
                    "id": "112824"
                },
                {
                    "display_label": "Tromb-al.Cazar eller Teaterbanditterne",
                    "id": "118219"
                },
                {
                    "display_label": "Den pantsatte bondedreng",
                    "id": "112027"
                },
                {
                    "display_label": "Sylfiden",
                    "id": "112155"
                },
                {
                    "display_label": "Med det gode",
                    "id": "111943"
                },
                {
                    "display_label": "Et Opgør",
                    "id": "112010"
                },
                {
                    "display_label": "Familien Jensen",
                    "id": "111842"
                },
                {
                    "display_label": "Huset Bonardon",
                    "id": "112334"
                },
                {
                    "display_label": "Ridderen af Randers Bro",
                    "id": "112064"
                },
                {
                    "display_label": "Anne Lise",
                    "id": "111709"
                },
                {
                    "display_label": "Dronningens jagtslot",
                    "id": "111794"
                },
                {
                    "display_label": "En Pokkers Tøs",
                    "id": "118134"
                },
                {
                    "display_label": "Axel og Valborg",
                    "id": "111718"
                },
                {
                    "display_label": "Tvillinger",
                    "id": "112201"
                },
                {
                    "display_label": "Den lille Pige med Svovlstikkerne",
                    "id": "111903"
                },
                {
                    "display_label": "Der var engang",
                    "id": "111780"
                },
                {
                    "display_label": "Et københavnsk Hjem",
                    "id": "112426"
                },
                {
                    "display_label": "Landmandsliv",
                    "id": "112433"
                },
                {
                    "display_label": "Tersløsegård",
                    "id": "112188"
                },
                {
                    "display_label": "Byens Stolthed",
                    "id": "111750"
                },
                {
                    "display_label": "Den skønne Helene",
                    "id": "112106"
                },
                {
                    "display_label": "Radikaleren",
                    "id": "112049"
                },
                {
                    "display_label": "Den fattige Drengs Eventyr",
                    "id": "111849"
                },
                {
                    "display_label": "Den ny Barselstue",
                    "id": "111989"
                },
                {
                    "display_label": "De Usynlige paa Sprogø",
                    "id": "112221"
                },
                {
                    "display_label": "Landlov",
                    "id": "112432"
                },
                {
                    "display_label": "Anders Tikjøb",
                    "id": "111707"
                },
                {
                    "display_label": "Gulddåsen",
                    "id": "112291"
                },
                {
                    "display_label": "Livselixiren",
                    "id": "111915"
                },
                {
                    "display_label": "Aarhus-Forfatternes Aftenunderholdning",
                    "id": "154144"
                },
                {
                    "display_label": "Konference af Hr. Herman Bang",
                    "id": "154145"
                },
                {
                    "display_label": "Gæsteoptræden. Koncertsangerinden Frk. Thora Lund",
                    "id": "154146"
                },
                {
                    "display_label": "Gæsteoptræden af Fru Charlotte Wiehe-Berény",
                    "id": "154148"
                },
                {
                    "display_label": "Tamperretscenen af Maskerade",
                    "id": "154151"
                },
                {
                    "display_label": "Pas de deux af Blomsterfesten i Genzano",
                    "id": "154152"
                },
                {
                    "display_label": "Musikalsk-deklamatorisk Afdeling",
                    "id": "154153"
                }
                ]
            },
            {
                "display_label": "Sæson 1905-06",
                "children": [
                {
                    "display_label": "Capriciosa eller Familien i Nyboder",
                    "id": "111755"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "111897"
                },
                {
                    "display_label": "Et Sølvbryllup",
                    "id": "112160"
                },
                {
                    "display_label": "Gulddåsen",
                    "id": "112292"
                },
                {
                    "display_label": "Et københavnsk Hjem",
                    "id": "112427"
                },
                {
                    "display_label": "Lad os skilles",
                    "id": "112431"
                },
                {
                    "display_label": "Min egen dreng",
                    "id": "112779"
                },
                {
                    "display_label": "En Lektion",
                    "id": "112441"
                },
                {
                    "display_label": "Rosa og Rosita",
                    "id": "112070"
                },
                {
                    "display_label": "De Forlovede",
                    "id": "118120"
                },
                {
                    "display_label": "Livets Maskerade",
                    "id": "111914"
                },
                {
                    "display_label": "Forhus og Baghus",
                    "id": "118114"
                },
                {
                    "display_label": "Domklokkerne",
                    "id": "111789"
                },
                {
                    "display_label": "Lynggaard & Co",
                    "id": "111923"
                },
                {
                    "display_label": "De små Landstrygere",
                    "id": "118217"
                },
                {
                    "display_label": "Efter Middagen",
                    "id": "111805"
                },
                {
                    "display_label": "Farinelli",
                    "id": "111848"
                },
                {
                    "display_label": "Erik og Abel",
                    "id": "111822"
                },
                {
                    "display_label": "Scenens Børn",
                    "id": "112079"
                },
                {
                    "display_label": "Fader og Søn",
                    "id": "111837"
                },
                {
                    "display_label": "Tordenskjold i Dynekilen",
                    "id": "112172"
                },
                {
                    "display_label": "Byen ved Havet",
                    "id": "111751"
                },
                {
                    "display_label": "Mor har Ret",
                    "id": "111967"
                },
                {
                    "display_label": "Haneben",
                    "id": "118139"
                },
                {
                    "display_label": "Agnete",
                    "id": "111695"
                },
                {
                    "display_label": "Geishaens Hævn",
                    "id": "154154"
                },
                {
                    "display_label": "Hari-Kiri",
                    "id": "154155"
                },
                {
                    "display_label": "Koncert af Lady Hallé og Ernst von Dohnànyi",
                    "id": "154158"
                },
                {
                    "display_label": "Muntre Musikanters koncert",
                    "id": "154159"
                },
                {
                    "display_label": "Aarhus Koncert-Orkester, 1ste Koncert",
                    "id": "154160"
                },
                {
                    "display_label": "Faddergaven",
                    "id": "154165"
                },
                {
                    "display_label": "Sigurd Slembe",
                    "id": "154166"
                },
                {
                    "display_label": "Kapelmester Bähnckes afskedskoncert",
                    "id": "154187"
                }
                ]
            },
            {
                "display_label": "Sæson 1906-07",
                "children": [
                {
                    "display_label": "Anders Tikjøb",
                    "id": "111708"
                },
                {
                    "display_label": "Landmandsliv",
                    "id": "112434"
                },
                {
                    "display_label": "Den gode borger",
                    "id": "112746"
                },
                {
                    "display_label": "Trold kan tæmmes",
                    "id": "112198"
                },
                {
                    "display_label": "Et enfoldigt pigebarn",
                    "id": "111816"
                },
                {
                    "display_label": "Gringoire",
                    "id": "112280"
                },
                {
                    "display_label": "Lette Dragoner",
                    "id": "112442"
                },
                {
                    "display_label": "Strandby Folk",
                    "id": "112146"
                },
                {
                    "display_label": "Den mystiske Arv",
                    "id": "111970"
                },
                {
                    "display_label": "Niels Nielsen",
                    "id": "111984"
                },
                {
                    "display_label": "Tappenstreg",
                    "id": "112176"
                },
                {
                    "display_label": "Mefistofeles",
                    "id": "118110"
                },
                {
                    "display_label": "Boccaccio",
                    "id": "111732"
                },
                {
                    "display_label": "Skærsild",
                    "id": "112097"
                },
                {
                    "display_label": "Oliver Twist",
                    "id": "112008"
                },
                {
                    "display_label": "De danske i Paris",
                    "id": "111776"
                },
                {
                    "display_label": "Tjenestefolk",
                    "id": "112165"
                },
                {
                    "display_label": "Under Enevælden",
                    "id": "112208"
                },
                {
                    "display_label": "Ranke Viljer",
                    "id": "112050"
                },
                {
                    "display_label": "Aprilsnarrene",
                    "id": "111713"
                },
                {
                    "display_label": "Stor i Skrøbelighed",
                    "id": "112145"
                },
                {
                    "display_label": "Løgnens Ansigter",
                    "id": "111927"
                },
                {
                    "display_label": "Den politiske kandestøber",
                    "id": "112036"
                },
                {
                    "display_label": "Den fortabte søn",
                    "id": "154198"
                },
                {
                    "display_label": "Den glade enke",
                    "id": "154199"
                },
                {
                    "display_label": "Aarhus Orkesterforenings Velgørenhedskoncert og Forestilling",
                    "id": "154203"
                },
                {
                    "display_label": "En børnekomedie",
                    "id": "154204"
                },
                {
                    "display_label": "Folkeviser ved Anna Bald og Violoncelkoncert ved Hr. Geisler",
                    "id": "154208"
                },
                {
                    "display_label": "Koncert - uddrag af Den lille pige med svovlstikkerne",
                    "id": "154211"
                },
                {
                    "display_label": "Deklamation ved Maya Bjerre-Jensen",
                    "id": "154212"
                },
                {
                    "display_label": "Aarhus Orkesterforenings Symfonikoncert",
                    "id": "154214"
                },
                {
                    "display_label": "Stor Symfoni-Koncert",
                    "id": "154219"
                }
                ]
            },
            {
                "display_label": "Sæson 1907-08",
                "children": [
                {
                    "display_label": "Eventyr på fodrejsen",
                    "id": "111831"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "111898"
                },
                {
                    "display_label": "Nej",
                    "id": "111979"
                },
                {
                    "display_label": "Sparekassen",
                    "id": "112125"
                },
                {
                    "display_label": "Morbus Tellermann",
                    "id": "112782"
                },
                {
                    "display_label": "Charleys Tante",
                    "id": "111758"
                },
                {
                    "display_label": "Livet på Hegnsgård",
                    "id": "111911"
                },
                {
                    "display_label": "Den Kærlighed, den Kærlighed",
                    "id": "112420"
                },
                {
                    "display_label": "Deklarationen",
                    "id": "111779"
                },
                {
                    "display_label": "Standens ære",
                    "id": "112136"
                },
                {
                    "display_label": "Sportsmænd",
                    "id": "112128"
                },
                {
                    "display_label": "De blaa Husarer",
                    "id": "111731"
                },
                {
                    "display_label": "Huset i Orden",
                    "id": "112335"
                },
                {
                    "display_label": "Den eneste redning",
                    "id": "111815"
                },
                {
                    "display_label": "Den bestøvlede Kat",
                    "id": "118109"
                },
                {
                    "display_label": "Clairettes 28 Dage",
                    "id": "111764"
                },
                {
                    "display_label": "Brødrene Hansen",
                    "id": "111742"
                },
                {
                    "display_label": "Elskovsleg",
                    "id": "111808"
                },
                {
                    "display_label": "Ludwig Wüllner-Koncert",
                    "id": "154247"
                },
                {
                    "display_label": "Bygmester Solness",
                    "id": "154250"
                },
                {
                    "display_label": "Gengangere",
                    "id": "154252"
                },
                {
                    "display_label": "Rosmersholm",
                    "id": "154253"
                },
                {
                    "display_label": "Et dukkehjem",
                    "id": "154254"
                },
                {
                    "display_label": "Første symfonikoncert",
                    "id": "154255"
                },
                {
                    "display_label": "Kathleen Parlow Koncert",
                    "id": "154258"
                },
                {
                    "display_label": "Mindefest for Holger Drachmann",
                    "id": "154261"
                },
                {
                    "display_label": "Kathleen Parlow og Magnus Laing Koncert",
                    "id": "154262"
                },
                {
                    "display_label": "Den hollandske trio koncert",
                    "id": "154264"
                },
                {
                    "display_label": "Symfonikoncert",
                    "id": "154267"
                },
                {
                    "display_label": "Mitja Itkis Koncert",
                    "id": "154306"
                },
                {
                    "display_label": "I foyeren",
                    "id": "154308"
                },
                {
                    "display_label": "Barn i kirken",
                    "id": "154309"
                }
                ]
            },
            {
                "display_label": "Sæson 1908-09",
                "children": [
                {
                    "display_label": "Brødrene Hansen",
                    "id": "111743"
                },
                {
                    "display_label": "Et enfoldigt pigebarn",
                    "id": "111817"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "111899"
                },
                {
                    "display_label": "Syvsoverdag",
                    "id": "112156"
                },
                {
                    "display_label": "Tappenstreg",
                    "id": "112177"
                },
                {
                    "display_label": "Huset i Orden",
                    "id": "112336"
                },
                {
                    "display_label": "Den gamle Præst",
                    "id": "112737"
                },
                {
                    "display_label": "Pigernes Alfred",
                    "id": "112794"
                },
                {
                    "display_label": "Den røde Hane",
                    "id": "112071"
                },
                {
                    "display_label": "Ideale magter",
                    "id": "112353"
                },
                {
                    "display_label": "Hvor man keder sig",
                    "id": "112342"
                },
                {
                    "display_label": "Madame Sherry",
                    "id": "111931"
                },
                {
                    "display_label": "Rivaler",
                    "id": "112068"
                },
                {
                    "display_label": "Ambrosius",
                    "id": "111700"
                },
                {
                    "display_label": "Da vi var enogtyve",
                    "id": "111769"
                },
                {
                    "display_label": "Den Glade Enke",
                    "id": "112297"
                },
                {
                    "display_label": "Pierrot og Pierrette",
                    "id": "118136"
                },
                {
                    "display_label": "Første Violin",
                    "id": "112260"
                },
                {
                    "display_label": "Bertran de Born",
                    "id": "111725"
                },
                {
                    "display_label": "Hvem er hun?",
                    "id": "112340"
                },
                {
                    "display_label": "Daniel Hertz",
                    "id": "111771"
                },
                {
                    "display_label": "Cajus Bruun: Monolog og oplæsning",
                    "id": "154310"
                },
                {
                    "display_label": "Den kære husfred",
                    "id": "154312"
                },
                {
                    "display_label": "Antonies fristelser",
                    "id": "154313"
                },
                {
                    "display_label": "Vise-Afdeling med kgl. skuespillerinde Oda Nielsen (1)",
                    "id": "154318"
                },
                {
                    "display_label": "Vise-Afdeling med kgl. skuespillerinde Oda Nielsen (2)",
                    "id": "154319"
                },
                {
                    "display_label": "Den grimme kone",
                    "id": "154321"
                },
                {
                    "display_label": "Frie hænder",
                    "id": "154322"
                },
                {
                    "display_label": "Harlekins millioner",
                    "id": "154323"
                },
                {
                    "display_label": "Kameliadamen",
                    "id": "154324"
                },
                {
                    "display_label": "På gale veje",
                    "id": "154325"
                }
                ]
            },
            {
                "display_label": "Sæson 1909-10",
                "children": [
                {
                    "display_label": "Ambrosius",
                    "id": "111701"
                },
                {
                    "display_label": "Bertran de Born",
                    "id": "111726"
                },
                {
                    "display_label": "Brødrene Hansen",
                    "id": "111744"
                },
                {
                    "display_label": "Eventyr på fodrejsen",
                    "id": "111832"
                },
                {
                    "display_label": "Madame Sherry",
                    "id": "111932"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "111993"
                },
                {
                    "display_label": "Den politiske kandestøber",
                    "id": "112037"
                },
                {
                    "display_label": "Den røde Hane",
                    "id": "112072"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "112244"
                },
                {
                    "display_label": "Genboerne",
                    "id": "112284"
                },
                {
                    "display_label": "Hans Højhed",
                    "id": "112311"
                },
                {
                    "display_label": "Gøngehøvdingen",
                    "id": "112451"
                },
                {
                    "display_label": "Paria",
                    "id": "112804"
                },
                {
                    "display_label": "Efterspil",
                    "id": "118404"
                },
                {
                    "display_label": "Kongen",
                    "id": "112405"
                },
                {
                    "display_label": "Dollarprinsessen",
                    "id": "111788"
                },
                {
                    "display_label": "Når den ny Vin blomstrer",
                    "id": "111973"
                },
                {
                    "display_label": "Renæssance",
                    "id": "112059"
                },
                {
                    "display_label": "Ulvens Søn",
                    "id": "112207"
                },
                {
                    "display_label": "En fattig ung Mands Eventyr",
                    "id": "111852"
                },
                {
                    "display_label": "Kean",
                    "id": "118145"
                },
                {
                    "display_label": "Karen Bornemann",
                    "id": "112392"
                },
                {
                    "display_label": "Sne",
                    "id": "112109"
                },
                {
                    "display_label": "Regimentets Datter",
                    "id": "112055"
                },
                {
                    "display_label": "Fruentimmerskolen",
                    "id": "111884"
                },
                {
                    "display_label": "Hans og Grethe",
                    "id": "112315"
                },
                {
                    "display_label": "Koncert med Tivolis Orkester",
                    "id": "154328"
                },
                {
                    "display_label": "Gæsteoptræden af Det Kgl. Teaters Ballet",
                    "id": "154329"
                },
                {
                    "display_label": "Vise-Afdeling med Fru Oda Nielsen",
                    "id": "154330"
                },
                {
                    "display_label": "Martinius Nielsen Aften",
                    "id": "154331"
                },
                {
                    "display_label": "La Ventana",
                    "id": "154332"
                },
                {
                    "display_label": "Den politiske kandestøber",
                    "id": "154333"
                },
                {
                    "display_label": "Bjørn Bjørnson Aften",
                    "id": "154334"
                },
                {
                    "display_label": "Når den ny vin blomstrer (Mindeforestilling)",
                    "id": "154337"
                },
                {
                    "display_label": "Et efterspil",
                    "id": "154338"
                },
                {
                    "display_label": "Vise-Afdeling ved fhv. Kgl. Skuespiller Carl Meyer",
                    "id": "154339"
                },
                {
                    "display_label": "Efterårsmanøvrer",
                    "id": "154340"
                },
                {
                    "display_label": "Et Sølvbryllup",
                    "id": "154341"
                },
                {
                    "display_label": "Harlekins Millioner",
                    "id": "154342"
                }
                ]
            },
            {
                "display_label": "Sæson 1910-11",
                "children": [
                {
                    "display_label": "En børsbaron",
                    "id": "111753"
                },
                {
                    "display_label": "Elverhøj",
                    "id": "111810"
                },
                {
                    "display_label": "Fruentimmerskolen",
                    "id": "111885"
                },
                {
                    "display_label": "Den politiske kandestøber",
                    "id": "112038"
                },
                {
                    "display_label": "En Skærsild",
                    "id": "112098"
                },
                {
                    "display_label": "Tjenestefolk",
                    "id": "112166"
                },
                {
                    "display_label": "Karen Bornemann",
                    "id": "112393"
                },
                {
                    "display_label": "Landmandsliv",
                    "id": "112435"
                },
                {
                    "display_label": "Pigernes Alfred",
                    "id": "112795"
                },
                {
                    "display_label": "Trilby",
                    "id": "112829"
                },
                {
                    "display_label": "Pierrot og Pierrette",
                    "id": "118137"
                },
                {
                    "display_label": "Greven af Luxembourg",
                    "id": "112271"
                },
                {
                    "display_label": "Niels Peter Svane",
                    "id": "111985"
                },
                {
                    "display_label": "Moral",
                    "id": "111965"
                },
                {
                    "display_label": "Pigernes Jens",
                    "id": "112034"
                },
                {
                    "display_label": "Faldgruben",
                    "id": "111838"
                },
                {
                    "display_label": "Betroede Midler",
                    "id": "111728"
                },
                {
                    "display_label": "Niniche",
                    "id": "111986"
                },
                {
                    "display_label": "Dønvig Præstegård",
                    "id": "111803"
                },
                {
                    "display_label": "Landsoldaten",
                    "id": "112438"
                },
                {
                    "display_label": "Den sjette Sans",
                    "id": "112087"
                },
                {
                    "display_label": "I Blinde",
                    "id": "112349"
                },
                {
                    "display_label": "Skilsmissens Overraskelser",
                    "id": "112089"
                },
                {
                    "display_label": "Skærmydsler",
                    "id": "112095"
                },
                {
                    "display_label": "Rejsen til China",
                    "id": "118144"
                },
                {
                    "display_label": "Alexander den Store",
                    "id": "111698"
                },
                {
                    "display_label": "Carmen",
                    "id": "120823"
                },
                {
                    "display_label": "Den lille havfrue",
                    "id": "154346"
                },
                {
                    "display_label": "Samson og Dalila",
                    "id": "154348"
                },
                {
                    "display_label": "Greven af Luxembourg",
                    "id": "154349"
                },
                {
                    "display_label": "Wienerblod",
                    "id": "154350"
                },
                {
                    "display_label": "Odette",
                    "id": "154351"
                },
                {
                    "display_label": "Daniel Hertz",
                    "id": "154362"
                },
                {
                    "display_label": "Geografi og kærlighed",
                    "id": "154352"
                }
                ]
            },
            {
                "display_label": "Sæson 1911-12",
                "children": [
                {
                    "display_label": "Cornevilles Klokker",
                    "id": "111766"
                },
                {
                    "display_label": "Elverhøj",
                    "id": "111811"
                },
                {
                    "display_label": "Den lille Pige med Svovlstikkerne",
                    "id": "111904"
                },
                {
                    "display_label": "Livet på Hegnsgård",
                    "id": "111912"
                },
                {
                    "display_label": "Lynggaard & Co",
                    "id": "111924"
                },
                {
                    "display_label": "En spurv i tranedans",
                    "id": "112131"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "112245"
                },
                {
                    "display_label": "Hans Højhed",
                    "id": "112312"
                },
                {
                    "display_label": "Prinsessen af Trapezunt",
                    "id": "112044"
                },
                {
                    "display_label": "Hjælpen",
                    "id": "112331"
                },
                {
                    "display_label": "Portnerens Datter",
                    "id": "112041"
                },
                {
                    "display_label": "Et Eventyr i Rosenborg Have",
                    "id": "111829"
                },
                {
                    "display_label": "Recitation og viser ved Poul Reumert",
                    "id": "153498"
                },
                {
                    "display_label": "Hvo, som elsker sin Fader",
                    "id": "112343"
                },
                {
                    "display_label": "Den stærkeste",
                    "id": "112149"
                },
                {
                    "display_label": "Madame sans Géne",
                    "id": "111930"
                },
                {
                    "display_label": "Når bønder elsker",
                    "id": "111972"
                },
                {
                    "display_label": "Kærlighedens Øjne",
                    "id": "112424"
                },
                {
                    "display_label": "Den grimme Kone",
                    "id": "118166"
                },
                {
                    "display_label": "En Dag ved Hoffet",
                    "id": "111770"
                },
                {
                    "display_label": "Mo´er og Datter",
                    "id": "111968"
                },
                {
                    "display_label": "Kongen morer sig",
                    "id": "112406"
                },
                {
                    "display_label": "Gutter om Bord",
                    "id": "112299"
                },
                {
                    "display_label": "Den store Afdøde",
                    "id": "118193"
                },
                {
                    "display_label": "Stjålen lykke",
                    "id": "154363"
                },
                {
                    "display_label": "Fru Majas Hævn",
                    "id": "154364"
                },
                {
                    "display_label": "Carmen",
                    "id": "154365"
                },
                {
                    "display_label": "Fætter Georg",
                    "id": "118216"
                }
                ]
            },
            {
                "display_label": "Sæson 1912-13",
                "children": [
                {
                    "display_label": "Charleys Tante",
                    "id": "111759"
                },
                {
                    "display_label": "Der var engang",
                    "id": "111781"
                },
                {
                    "display_label": "Livselixiren",
                    "id": "111916"
                },
                {
                    "display_label": "Ridderen af Randers Bro",
                    "id": "112065"
                },
                {
                    "display_label": "Svend Dyrings Hus",
                    "id": "112154"
                },
                {
                    "display_label": "Et Sølvbryllup",
                    "id": "112161"
                },
                {
                    "display_label": "Huset i Orden",
                    "id": "112337"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "112373"
                },
                {
                    "display_label": "Julestue",
                    "id": "112385"
                },
                {
                    "display_label": "Den kære familie",
                    "id": "112416"
                },
                {
                    "display_label": "Pigernes Alfred",
                    "id": "112796"
                },
                {
                    "display_label": "Pierrot og Pierrette",
                    "id": "118135"
                },
                {
                    "display_label": "Tidens Mand",
                    "id": "112192"
                },
                {
                    "display_label": "Samfundets Støtter",
                    "id": "112076"
                },
                {
                    "display_label": "Herren ser dine Veje",
                    "id": "112326"
                },
                {
                    "display_label": "Annemaries Giftermål",
                    "id": "111711"
                },
                {
                    "display_label": "Milepæle",
                    "id": "111951"
                },
                {
                    "display_label": "De flotte Drenge",
                    "id": "111864"
                },
                {
                    "display_label": "Hans eneste Kone",
                    "id": "112308"
                },
                {
                    "display_label": "Fædrenes Jord",
                    "id": "112253"
                },
                {
                    "display_label": "Erotik",
                    "id": "111825"
                },
                {
                    "display_label": "En ideal ægtemand",
                    "id": "112356"
                },
                {
                    "display_label": "Revolte",
                    "id": "112062"
                },
                {
                    "display_label": "Zaza",
                    "id": "112242"
                },
                {
                    "display_label": "Martha",
                    "id": "154366"
                },
                {
                    "display_label": "Sorteper",
                    "id": "154367"
                },
                {
                    "display_label": "La Traviata",
                    "id": "154368"
                },
                {
                    "display_label": "Den mystiske Arv",
                    "id": "154369"
                },
                {
                    "display_label": "Den skønne Helene",
                    "id": "154370"
                },
                {
                    "display_label": "Indenfor murene",
                    "id": "154371"
                },
                {
                    "display_label": "Pierrot og Pierette",
                    "id": "154372"
                },
                {
                    "display_label": "Opstandelse",
                    "id": "112011"
                }
                ]
            },
            {
                "display_label": "Sæson 1913-14",
                "children": [
                {
                    "display_label": "De små Landstrygere",
                    "id": "112108"
                },
                {
                    "display_label": "Teaterbanditterne",
                    "id": "112182"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "112246"
                },
                {
                    "display_label": "Dansen på Koldinghus",
                    "id": "111774"
                },
                {
                    "display_label": "Henrik og Pernille",
                    "id": "112324"
                },
                {
                    "display_label": "Miss Helyett",
                    "id": "111957"
                },
                {
                    "display_label": "Gammel Kærlighed",
                    "id": "112279"
                },
                {
                    "display_label": "Den sorte Panter",
                    "id": "112122"
                },
                {
                    "display_label": "Min Ven Teddy",
                    "id": "111955"
                },
                {
                    "display_label": "Bjærg-Eyvind og hans Hustru",
                    "id": "111729"
                },
                {
                    "display_label": "Et Folkesagn",
                    "id": "111869"
                },
                {
                    "display_label": "Jacob von Thyboe",
                    "id": "112368"
                },
                {
                    "display_label": "En Kvinde af Folket",
                    "id": "112410"
                },
                {
                    "display_label": "Lovens Arm",
                    "id": "111919"
                },
                {
                    "display_label": "Skovridergården",
                    "id": "112091"
                },
                {
                    "display_label": "Lille Eva",
                    "id": "111902"
                },
                {
                    "display_label": "Mikkel Larsens Drenge",
                    "id": "111950"
                },
                {
                    "display_label": "Skyldig eller uskyldig",
                    "id": "112094"
                },
                {
                    "display_label": "Excellencen Max",
                    "id": "111836"
                },
                {
                    "display_label": "Man dør ikke af Glæde",
                    "id": "111938"
                },
                {
                    "display_label": "En søndag på Amager",
                    "id": "112163"
                },
                {
                    "display_label": "Et Vajsenhusbarn",
                    "id": "112222"
                },
                {
                    "display_label": "Dollarprinsessen",
                    "id": "154373"
                },
                {
                    "display_label": "Pariser-Tango",
                    "id": "154377"
                },
                {
                    "display_label": "Som i ungdommens vår",
                    "id": "154378"
                },
                {
                    "display_label": "Filmens Dronning",
                    "id": "154379"
                },
                {
                    "display_label": "Flugten til Amerika",
                    "id": "111865"
                }
                ]
            },
            {
                "display_label": "Sæson 1914-15",
                "children": [
                {
                    "display_label": "Capriciosa eller Familien i Nyboder",
                    "id": "111756"
                },
                {
                    "display_label": "For Alvor",
                    "id": "111872"
                },
                {
                    "display_label": "Fra den anden Bred",
                    "id": "112021"
                },
                {
                    "display_label": "En søndag på Amager",
                    "id": "112164"
                },
                {
                    "display_label": "I høstnatten",
                    "id": "112764"
                },
                {
                    "display_label": "Den gamle Pianist",
                    "id": "112268"
                },
                {
                    "display_label": "Bolettes Bryllupsfærd",
                    "id": "111733"
                },
                {
                    "display_label": "Vildanden",
                    "id": "112229"
                },
                {
                    "display_label": "Pygmalion",
                    "id": "118171"
                },
                {
                    "display_label": "På den anden Bred",
                    "id": "112020"
                },
                {
                    "display_label": "Tyven",
                    "id": "112203"
                },
                {
                    "display_label": "Rede Penge",
                    "id": "112054"
                },
                {
                    "display_label": "Jorden rundt i 80 dage",
                    "id": "112382"
                },
                {
                    "display_label": "Elskovs guld",
                    "id": "111807"
                },
                {
                    "display_label": "Elverskud",
                    "id": "120924"
                },
                {
                    "display_label": "I Rungsted Kro",
                    "id": "150163"
                },
                {
                    "display_label": "Lazarus",
                    "id": "112439"
                },
                {
                    "display_label": "Husmandstøsen",
                    "id": "112338"
                },
                {
                    "display_label": "Kærlighedens Ret",
                    "id": "112423"
                },
                {
                    "display_label": "Molboerne",
                    "id": "111964"
                },
                {
                    "display_label": "Manden på Højriis",
                    "id": "111936"
                },
                {
                    "display_label": "Revolutionsbryllup",
                    "id": "112063"
                },
                {
                    "display_label": "Fattig og Rig",
                    "id": "111851"
                },
                {
                    "display_label": "Et dukkehjem",
                    "id": "154381"
                },
                {
                    "display_label": "Mignon",
                    "id": "154384"
                },
                {
                    "display_label": "Når storken kommer",
                    "id": "154386"
                },
                {
                    "display_label": "Ungdom og galskab",
                    "id": "154391"
                },
                {
                    "display_label": "Jægerbruden",
                    "id": "118175"
                }
                ]
            },
            {
                "display_label": "Sæson 1915-16",
                "children": [
                {
                    "display_label": "Møntergade 39",
                    "id": "111971"
                },
                {
                    "display_label": "Den Anden",
                    "id": "111706"
                },
                {
                    "display_label": "Petersen og hendes Søstre",
                    "id": "112032"
                },
                {
                    "display_label": "Paul Lange og Tora Parsberg",
                    "id": "112029"
                },
                {
                    "display_label": "Fred på jorden",
                    "id": "111880"
                },
                {
                    "display_label": "Gurli",
                    "id": "112296"
                },
                {
                    "display_label": "London i Lygteskær",
                    "id": "111917"
                },
                {
                    "display_label": "Tornerose",
                    "id": "112178"
                },
                {
                    "display_label": "Tartuffe",
                    "id": "112179"
                },
                {
                    "display_label": "Stridens æble",
                    "id": "112147"
                },
                {
                    "display_label": "Dunungen",
                    "id": "111799"
                },
                {
                    "display_label": "Benefice for Hr. Kapelmester A. John Gutfeld",
                    "id": "154392"
                },
                {
                    "display_label": "Polsk blod",
                    "id": "154398"
                },
                {
                    "display_label": "Figaros bryllup",
                    "id": "154399"
                },
                {
                    "display_label": "Cornevilles klokker",
                    "id": "154400"
                },
                {
                    "display_label": "Den lille havfrue",
                    "id": "154402"
                },
                {
                    "display_label": "Det gamle spil om enhver",
                    "id": "154403"
                },
                {
                    "display_label": "Genboerne",
                    "id": "154404"
                },
                {
                    "display_label": "På den anden bred",
                    "id": "154405"
                },
                {
                    "display_label": "Under Værgerådet",
                    "id": "112210"
                }
                ]
            },
            {
                "display_label": "Sæson 1916-17",
                "children": [
                {
                    "display_label": "London i Lygteskær",
                    "id": "111918"
                },
                {
                    "display_label": "Pygmalion",
                    "id": "112046"
                },
                {
                    "display_label": "Tartuffe",
                    "id": "112180"
                },
                {
                    "display_label": "Under Værgerådet",
                    "id": "112211"
                },
                {
                    "display_label": "Lazarus",
                    "id": "112440"
                },
                {
                    "display_label": "Prinsessen og den hele Verden",
                    "id": "112450"
                },
                {
                    "display_label": "Ungdomsleg",
                    "id": "112825"
                },
                {
                    "display_label": "Troubaduren",
                    "id": "112827"
                },
                {
                    "display_label": "Fædreland",
                    "id": "112252"
                },
                {
                    "display_label": "Fangen på Kalø",
                    "id": "111846"
                },
                {
                    "display_label": "Jean de France",
                    "id": "112370"
                },
                {
                    "display_label": "De Unges Forbund",
                    "id": "112216"
                },
                {
                    "display_label": "Avertér!",
                    "id": "111717"
                },
                {
                    "display_label": "Sigurd Braa",
                    "id": "112085"
                },
                {
                    "display_label": "På Anklagebænken",
                    "id": "112018"
                },
                {
                    "display_label": "Ballet-Divertissement",
                    "id": "154409"
                },
                {
                    "display_label": "Czardasfyrstinden",
                    "id": "154412"
                },
                {
                    "display_label": "Den skønne Helene",
                    "id": "154413"
                },
                {
                    "display_label": "Jeppe på Bjerget (2.akt)",
                    "id": "154414"
                },
                {
                    "display_label": "Elverhøj",
                    "id": "154415"
                },
                {
                    "display_label": "Eventyr på fodrejsen",
                    "id": "145516"
                },
                {
                    "display_label": "Gulddåsen",
                    "id": "154417"
                },
                {
                    "display_label": "Købt og betalt",
                    "id": "112429"
                }
                ]
            },
            {
                "display_label": "Sæson 1917-18",
                "children": [
                {
                    "display_label": "Familien Jensen",
                    "id": "111843"
                },
                {
                    "display_label": "Ukrudt",
                    "id": "150215"
                },
                {
                    "display_label": "De Våbenløse",
                    "id": "150216"
                },
                {
                    "display_label": "Feriegæsterne",
                    "id": "111856"
                },
                {
                    "display_label": "Faust",
                    "id": "112751"
                },
                {
                    "display_label": "Du skal ære",
                    "id": "150217"
                },
                {
                    "display_label": "Harlekins millioner",
                    "id": "112760"
                },
                {
                    "display_label": "Alverdens Synd",
                    "id": "111699"
                },
                {
                    "display_label": "Det store forlis",
                    "id": "112142"
                },
                {
                    "display_label": "Fanden i Gammelby",
                    "id": "111844"
                },
                {
                    "display_label": "Scapins Skalkestykker",
                    "id": "112077"
                },
                {
                    "display_label": "Det sorte får",
                    "id": "112121"
                },
                {
                    "display_label": "Klokken, der sank",
                    "id": "112399"
                },
                {
                    "display_label": "Uden for Murene",
                    "id": "112205"
                },
                {
                    "display_label": "Den sidste Nat",
                    "id": "112082"
                },
                {
                    "display_label": "Skjulte Kampe: Ukrudt, De våbenløse, Du skal ære",
                    "id": "112090"
                },
                {
                    "display_label": "Geografi og Kærlighed",
                    "id": "112289"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "154418"
                },
                {
                    "display_label": "Flagermusen",
                    "id": "154419"
                },
                {
                    "display_label": "Kameliadamen",
                    "id": "154420"
                },
                {
                    "display_label": "Kvindedjævelen",
                    "id": "154421"
                },
                {
                    "display_label": "Kunstnernaturer",
                    "id": "112409"
                }
                ]
            },
            {
                "display_label": "Sæson 1918-19",
                "children": [
                {
                    "display_label": "Den kære familie",
                    "id": "112417"
                },
                {
                    "display_label": "Bajadser",
                    "id": "112727"
                },
                {
                    "display_label": "Jeanettes bryllup",
                    "id": "112773"
                },
                {
                    "display_label": "Drengene fra Amerika",
                    "id": "111791"
                },
                {
                    "display_label": "Fanevagt",
                    "id": "111845"
                },
                {
                    "display_label": "Som et menneske sår",
                    "id": "112114"
                },
                {
                    "display_label": "Over Evne I",
                    "id": "112016"
                },
                {
                    "display_label": "Født Andersen",
                    "id": "112254"
                },
                {
                    "display_label": "Barken Margrethe af Danmark",
                    "id": "111721"
                },
                {
                    "display_label": "Folkene på Dangården",
                    "id": "111868"
                },
                {
                    "display_label": "Den Vægelsindede",
                    "id": "112239"
                },
                {
                    "display_label": "Hausse",
                    "id": "112317"
                },
                {
                    "display_label": "Fru Dulskas moral",
                    "id": "154422"
                },
                {
                    "display_label": "Dollarprinsessen",
                    "id": "154423"
                },
                {
                    "display_label": "Madame Sherry",
                    "id": "154424"
                },
                {
                    "display_label": "Heksebålet",
                    "id": "154425"
                },
                {
                    "display_label": "Første Abonnements-Koncert",
                    "id": "154426"
                },
                {
                    "display_label": "Anden Abonnements-Koncert",
                    "id": "154427"
                },
                {
                    "display_label": "Tredje Abonnements-Koncert",
                    "id": "154428"
                },
                {
                    "display_label": "Paria",
                    "id": "154429"
                },
                {
                    "display_label": "Skærmydsler",
                    "id": "154430"
                },
                {
                    "display_label": "Faderen",
                    "id": "154450"
                },
                {
                    "display_label": "Gøgen",
                    "id": "112301"
                }
                ]
            },
            {
                "display_label": "Sæson 1919-20",
                "children": [
                {
                    "display_label": "Moderate Løjer",
                    "id": "111960"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "112374"
                },
                {
                    "display_label": "Tyrannens Fald",
                    "id": "112202"
                },
                {
                    "display_label": "En Folkefjende",
                    "id": "111866"
                },
                {
                    "display_label": "Hendes type",
                    "id": "112323"
                },
                {
                    "display_label": "En Skærsomrnernatsdrøm",
                    "id": "112099"
                },
                {
                    "display_label": "Dybet",
                    "id": "111802"
                },
                {
                    "display_label": "Springende Løver. Hjerter i Brand",
                    "id": "112129"
                },
                {
                    "display_label": "Den erotiske hamster",
                    "id": "154465"
                },
                {
                    "display_label": "Kvartet",
                    "id": "154467"
                },
                {
                    "display_label": "Romantik",
                    "id": "54469"
                },
                {
                    "display_label": "Løjtnantens civile Bror",
                    "id": "111928"
                }
                ]
            },
            {
                "display_label": "Sæson 1920-21",
                "children": [
                {
                    "display_label": "Annemaries Giftermål",
                    "id": "111712"
                },
                {
                    "display_label": "Daniel Hertz",
                    "id": "111773"
                },
                {
                    "display_label": "Elverhøj",
                    "id": "111812"
                },
                {
                    "display_label": "En Folkefjende",
                    "id": "111867"
                },
                {
                    "display_label": "Løjtnantens civile Bror",
                    "id": "111929"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "111994"
                },
                {
                    "display_label": "Der var en Svend med sin Pigelil",
                    "id": "111785"
                },
                {
                    "display_label": "Hævnen",
                    "id": "112345"
                },
                {
                    "display_label": "Kringleby",
                    "id": "112408"
                },
                {
                    "display_label": "Vi Mordere",
                    "id": "112234"
                },
                {
                    "display_label": "Danser De ?",
                    "id": "111775"
                },
                {
                    "display_label": "Kærlighedens Farce",
                    "id": "112421"
                },
                {
                    "display_label": "Portnerens datter",
                    "id": "154455"
                },
                {
                    "display_label": "Jomfruburet",
                    "id": "154456"
                },
                {
                    "display_label": "Mignon",
                    "id": "154457"
                },
                {
                    "display_label": "Lady Frederick",
                    "id": "154458"
                },
                {
                    "display_label": "Kiki",
                    "id": "154459"
                },
                {
                    "display_label": "Den grønne elevator",
                    "id": "154461"
                },
                {
                    "display_label": "Musikalsk-deklamatorisk afdeling",
                    "id": "154462"
                },
                {
                    "display_label": "Munken går i enge",
                    "id": "154463"
                },
                {
                    "display_label": "Heksedans: Munken går i enge, Aftenvisit, Komplet uskyldig",
                    "id": "112319"
                }
                ]
            },
            {
                "display_label": "Sæson 1921-22",
                "children": [
                {
                    "display_label": "Ambrosius",
                    "id": "111702"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "111995"
                },
                {
                    "display_label": "En spurv i tranedans",
                    "id": "112132"
                },
                {
                    "display_label": "I Rungsted Kro",
                    "id": "112768"
                },
                {
                    "display_label": "Borgmesteren i Stilemonde",
                    "id": "113071"
                },
                {
                    "display_label": "Phi-Phi",
                    "id": "118462"
                },
                {
                    "display_label": "Brødrene Østermanns Huskors",
                    "id": "111745"
                },
                {
                    "display_label": "Skruen",
                    "id": "112093"
                },
                {
                    "display_label": "Den nøgne Sandhed",
                    "id": "112005"
                },
                {
                    "display_label": "Det gamle Hjem",
                    "id": "112264"
                },
                {
                    "display_label": "Lyse Camilla",
                    "id": "111926"
                },
                {
                    "display_label": "Jakob og Kristoffer",
                    "id": "112369"
                },
                {
                    "display_label": "De havarerede",
                    "id": "154470"
                },
                {
                    "display_label": "Musik- og Balletsoiré",
                    "id": "154471"
                },
                {
                    "display_label": "Flamme",
                    "id": "154476"
                },
                {
                    "display_label": "Mr. Wu",
                    "id": "154478"
                },
                {
                    "display_label": "Ballet-Forestilling",
                    "id": "154479"
                },
                {
                    "display_label": "Fruentimmerskolen - Molière-Festforestilling",
                    "id": "154480"
                },
                {
                    "display_label": "Den hvide dame",
                    "id": "154481"
                },
                {
                    "display_label": "Faldgruben",
                    "id": "154482"
                },
                {
                    "display_label": "Femina",
                    "id": "154483"
                },
                {
                    "display_label": "Det tredje Skud",
                    "id": "112189"
                }
                ]
            },
            {
                "display_label": "Sæson 1922-23",
                "children": [
                {
                    "display_label": "Milepæle",
                    "id": "111952"
                },
                {
                    "display_label": "Paul Lange og Tora Parsberg",
                    "id": "112030"
                },
                {
                    "display_label": "Petersen og hendes Søstre",
                    "id": "112033"
                },
                {
                    "display_label": "Skovridergården",
                    "id": "112092"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "112247"
                },
                {
                    "display_label": "Ideale magter",
                    "id": "112354"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "112375"
                },
                {
                    "display_label": "En børsbaron",
                    "id": "112745"
                },
                {
                    "display_label": "Verdensry",
                    "id": "112225"
                },
                {
                    "display_label": "Gamle Melodier",
                    "id": "112265"
                },
                {
                    "display_label": "Frøken Bodil og hendes Broder",
                    "id": "111889"
                },
                {
                    "display_label": "Bureauslaven",
                    "id": "111749"
                },
                {
                    "display_label": "Mands Vilje",
                    "id": "111937"
                },
                {
                    "display_label": "Den lille Rødhætte",
                    "id": "111906"
                },
                {
                    "display_label": "Russisk Ballet",
                    "id": "154492"
                },
                {
                    "display_label": "Russisk Ballet",
                    "id": "154493"
                },
                {
                    "display_label": "Bajaderen",
                    "id": "154494"
                },
                {
                    "display_label": "Som i ungdommens vår",
                    "id": "154495"
                },
                {
                    "display_label": "Ungdomskilden",
                    "id": "112214"
                }
                ]
            },
            {
                "display_label": "Sæson 1923-24",
                "children": [
                {
                    "display_label": "Der var engang",
                    "id": "111782"
                },
                {
                    "display_label": "Livet på Hegnsgård",
                    "id": "111913"
                },
                {
                    "display_label": "Første Violin",
                    "id": "112261"
                },
                {
                    "display_label": "Landmandsliv",
                    "id": "112436"
                },
                {
                    "display_label": "Min egen dreng",
                    "id": "112780"
                },
                {
                    "display_label": "Den Stundesløse",
                    "id": "112148"
                },
                {
                    "display_label": "Wienerbarnet",
                    "id": "112227"
                },
                {
                    "display_label": "Jomfruburet",
                    "id": "112379"
                },
                {
                    "display_label": "Den første Morgen",
                    "id": "112258"
                },
                {
                    "display_label": "Abekatten",
                    "id": "111689"
                },
                {
                    "display_label": "Den blå Fugl",
                    "id": "111730"
                },
                {
                    "display_label": "Konen, der lærte at gyse",
                    "id": "112403"
                },
                {
                    "display_label": "Kobberbryllup",
                    "id": "112400"
                },
                {
                    "display_label": "Pantomimeteatret i Tivoli",
                    "id": "154501"
                },
                {
                    "display_label": "Den sorte Domino",
                    "id": "112120"
                }
                ]
            },
            {
                "display_label": "Sæson 1924-25",
                "children": [
                {
                    "display_label": "Et Folkesagn",
                    "id": "111870"
                },
                {
                    "display_label": "Tordenskjold i Dynekilen",
                    "id": "112173"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "112376"
                },
                {
                    "display_label": "Tante Cramers Testamente",
                    "id": "118173"
                },
                {
                    "display_label": "I den syvende Himmel",
                    "id": "112351"
                },
                {
                    "display_label": "Mod den fremmede Kyst",
                    "id": "111958"
                },
                {
                    "display_label": "Hanne",
                    "id": "112306"
                },
                {
                    "display_label": "Støvlet=Cathrine",
                    "id": "112150"
                },
                {
                    "display_label": "Snehvide",
                    "id": "118218"
                },
                {
                    "display_label": "Den store Stemme",
                    "id": "112144"
                },
                {
                    "display_label": "Slægten",
                    "id": "112107"
                },
                {
                    "display_label": "Helligtrekongersaften",
                    "id": "112321"
                },
                {
                    "display_label": "Grevinde Maritza",
                    "id": "112275"
                },
                {
                    "display_label": "Grevinde Mariza, anden akt",
                    "id": "154513"
                },
                {
                    "display_label": "Den store Scene",
                    "id": "112143"
                }
                ]
            },
            {
                "display_label": "Sæson 1925-26",
                "children": [
                {
                    "display_label": "Erasmus Montanus",
                    "id": "111820"
                },
                {
                    "display_label": "Soldaterløjer",
                    "id": "112111"
                },
                {
                    "display_label": "Grevinde Maritza",
                    "id": "112276"
                },
                {
                    "display_label": "Epilog",
                    "id": "113070"
                },
                {
                    "display_label": "På Bjerget",
                    "id": "112019"
                },
                {
                    "display_label": "Det gamle Guld",
                    "id": "112263"
                },
                {
                    "display_label": "De Uadskillelige",
                    "id": "112204"
                },
                {
                    "display_label": "Fru Beates Regnskab",
                    "id": "111883"
                },
                {
                    "display_label": "Erobrerne",
                    "id": "111824"
                },
                {
                    "display_label": "Julestormen",
                    "id": "112383"
                },
                {
                    "display_label": "Wienervalsen",
                    "id": "112228"
                },
                {
                    "display_label": "Store Claus og Lille Claus",
                    "id": "112140"
                },
                {
                    "display_label": "Premieren",
                    "id": "112042"
                },
                {
                    "display_label": "Ingmarsgaarden",
                    "id": "112366"
                },
                {
                    "display_label": "Revisoren",
                    "id": "112061"
                },
                {
                    "display_label": "Nordmanden",
                    "id": "111987"
                }
                ]
            },
            {
                "display_label": "Sæson 1926-27",
                "children": [
                {
                    "display_label": "Erasmus Montanus",
                    "id": "111821"
                },
                {
                    "display_label": "Eventyr på fodrejsen",
                    "id": "111833"
                },
                {
                    "display_label": "En Fallit",
                    "id": "111840"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "111996"
                },
                {
                    "display_label": "Det skønne eventyr",
                    "id": "112104"
                },
                {
                    "display_label": "Hans Højhed",
                    "id": "112313"
                },
                {
                    "display_label": "Husmandstøsen",
                    "id": "112339"
                },
                {
                    "display_label": "De første Violer",
                    "id": "112259"
                },
                {
                    "display_label": "Dommeren",
                    "id": "111790"
                },
                {
                    "display_label": "Frøken Hook van Holland",
                    "id": "111890"
                },
                {
                    "display_label": "David Copperfield",
                    "id": "111777"
                },
                {
                    "display_label": "Victorias Mænd",
                    "id": "112226"
                },
                {
                    "display_label": "Hagbarth og Signe",
                    "id": "112304"
                },
                {
                    "display_label": "Det gamle spil om enhver",
                    "id": "112272"
                },
                {
                    "display_label": "Koncert med Prager Lærer-Sangerforening",
                    "id": "154518"
                },
                {
                    "display_label": "Aarhus Teaters Symfonikoncert",
                    "id": "154519"
                },
                {
                    "display_label": "Uschi",
                    "id": "112217"
                }
                ]
            },
            {
                "display_label": "Sæson 1927-28",
                "children": [
                {
                    "display_label": "Charleys Tante",
                    "id": "111760"
                },
                {
                    "display_label": "Der var engang",
                    "id": "111783"
                },
                {
                    "display_label": "Den politiske kandestøber",
                    "id": "112039"
                },
                {
                    "display_label": "Trold kan tæmmes",
                    "id": "112199"
                },
                {
                    "display_label": "Uschi",
                    "id": "112218"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "112248"
                },
                {
                    "display_label": "Genboerne",
                    "id": "112285"
                },
                {
                    "display_label": "Gulddåsen",
                    "id": "112293"
                },
                {
                    "display_label": "Hedda Gabler",
                    "id": "112318"
                },
                {
                    "display_label": "Skænk mig fjender",
                    "id": "153499"
                },
                {
                    "display_label": "Vandmøllen",
                    "id": "112223"
                },
                {
                    "display_label": "Julegave-Aften",
                    "id": "150167"
                },
                {
                    "display_label": "Sol står op",
                    "id": "112113"
                },
                {
                    "display_label": "Komedien på Slottet",
                    "id": "112402"
                },
                {
                    "display_label": "Ebberød Bank",
                    "id": "111804"
                },
                {
                    "display_label": "Tegnebogen",
                    "id": "112186"
                },
                {
                    "display_label": "Klods Hans",
                    "id": "112398"
                },
                {
                    "display_label": "Bajaderen",
                    "id": "154524"
                },
                {
                    "display_label": "Dollarprinsessen",
                    "id": "154525"
                },
                {
                    "display_label": "Cirkusprinsessen",
                    "id": "154526"
                },
                {
                    "display_label": "Nej Nej Nanette",
                    "id": "154527"
                },
                {
                    "display_label": "Det dødbringende kys",
                    "id": "154528"
                },
                {
                    "display_label": "Aarhus Teaters Første Folkekoncert",
                    "id": "154531"
                },
                {
                    "display_label": "Aarhus Teaters Anden Folkekoncert",
                    "id": "154532"
                },
                {
                    "display_label": "Aarhus Teaters Tredje Folkekoncert",
                    "id": "154534"
                },
                {
                    "display_label": "Aarhus Teaters Fjerde Folkekoncert",
                    "id": "154535"
                },
                {
                    "display_label": "Geografi og Kærlighed",
                    "id": "154536"
                },
                {
                    "display_label": "Erik Ejegods Pilgrimsfærd",
                    "id": "154537"
                },
                {
                    "display_label": "Helga Egdøs Danseinstitut Elevopvisning",
                    "id": "154542"
                },
                {
                    "display_label": "Landeværn",
                    "id": "154543"
                },
                {
                    "display_label": "Skibet er ladet med",
                    "id": "154545"
                },
                {
                    "display_label": "Skænk mig fjender",
                    "id": "154546"
                },
                {
                    "display_label": "Tre små piger",
                    "id": "154547"
                },
                {
                    "display_label": "Lily Ishøys Balletskole-Elevopvisning",
                    "id": "154548"
                },
                {
                    "display_label": "Graven under Triumfbuen",
                    "id": "154550"
                },
                {
                    "display_label": "Når den ny vin blomstrer",
                    "id": "154551"
                },
                {
                    "display_label": "Ungdom og Galskab",
                    "id": "154552"
                },
                {
                    "display_label": "White Cargo",
                    "id": "154553"
                },
                {
                    "display_label": "Hopla, vi lever!",
                    "id": "112333"
                }
                ]
            },
            {
                "display_label": "Sæson 1928-29",
                "children": [
                {
                    "display_label": "Den lille Rødhætte",
                    "id": "111907"
                },
                {
                    "display_label": "En spurv i tranedans",
                    "id": "112133"
                },
                {
                    "display_label": "Henrik og Pernille",
                    "id": "112325"
                },
                {
                    "display_label": "Jomfruburet",
                    "id": "112380"
                },
                {
                    "display_label": "Krateret",
                    "id": "112777"
                },
                {
                    "display_label": "Skuespilleren",
                    "id": "112810"
                },
                {
                    "display_label": "Den gamle Præstegaard",
                    "id": "112269"
                },
                {
                    "display_label": "Kærlighed uden Strømper",
                    "id": "112425"
                },
                {
                    "display_label": "Er Mary Dugan skyldig?",
                    "id": "111823"
                },
                {
                    "display_label": "Bedre folks børn",
                    "id": "111723"
                },
                {
                    "display_label": "Julegaveforestilling",
                    "id": "150166"
                },
                {
                    "display_label": "I Norske Selskab",
                    "id": "112352"
                },
                {
                    "display_label": "Fra Rold til Ræbild",
                    "id": "111878"
                },
                {
                    "display_label": "Den Gerrige",
                    "id": "118167"
                },
                {
                    "display_label": "Hokuspokus",
                    "id": "112332"
                },
                {
                    "display_label": "Frøken Julie",
                    "id": "111891"
                },
                {
                    "display_label": "Aarhus Teaters tredje folkekoncert",
                    "id": "154554"
                },
                {
                    "display_label": "Aarhus Teaters første Folkekoncert",
                    "id": "154555"
                },
                {
                    "display_label": "Aarhus Teaters anden Folkekoncert",
                    "id": "154556"
                },
                {
                    "display_label": "Aarhus Teaters fjerde Folkekoncert",
                    "id": "154557"
                },
                {
                    "display_label": "Krateret",
                    "id": "154558"
                },
                {
                    "display_label": "Julegave-Aften",
                    "id": "154571"
                },
                {
                    "display_label": "Hjerter Dame",
                    "id": "112330"
                }
                ]
            },
            {
                "display_label": "Sæson 1929-30",
                "children": [
                {
                    "display_label": "Elverhøj",
                    "id": "111813"
                },
                {
                    "display_label": "Nej",
                    "id": "111980"
                },
                {
                    "display_label": "Pak",
                    "id": "112026"
                },
                {
                    "display_label": "Sparekassen",
                    "id": "112126"
                },
                {
                    "display_label": "Liselotte",
                    "id": "111909"
                },
                {
                    "display_label": "Falske Nøgler",
                    "id": "111841"
                },
                {
                    "display_label": "Aladdin",
                    "id": "111696"
                },
                {
                    "display_label": "Emilies Hjertebanken",
                    "id": "118111"
                },
                {
                    "display_label": "Ja",
                    "id": "118141"
                },
                {
                    "display_label": "Julegaveaften",
                    "id": "150168"
                },
                {
                    "display_label": "Bunbury",
                    "id": "111746"
                },
                {
                    "display_label": "Mordet på anden sal",
                    "id": "111966"
                },
                {
                    "display_label": "Som i Ungdommens Vår",
                    "id": "112116"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskabs første Koncert",
                    "id": "154559"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskabs anden Koncert",
                    "id": "154560"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskabs tredje Koncert",
                    "id": "154561"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskabs fjerde Koncert",
                    "id": "154562"
                },
                {
                    "display_label": "Swedenhjelms",
                    "id": "154563"
                },
                {
                    "display_label": "Lilly Ishøys Balletsoiré",
                    "id": "154564"
                },
                {
                    "display_label": "Aarhus Teaters Første Folkekoncert",
                    "id": "154565"
                },
                {
                    "display_label": "Aarhus Teaters anden Folkekoncert",
                    "id": "154566"
                },
                {
                    "display_label": "Aarhus Teaters tredje Folkekoncert",
                    "id": "154567"
                },
                {
                    "display_label": "Aarhus Teaters fjerde Folkekoncert",
                    "id": "154568"
                },
                {
                    "display_label": "Fra Vestfronten",
                    "id": "154576"
                },
                {
                    "display_label": "Frøken Kirkemus Frøken",
                    "id": "154577"
                },
                {
                    "display_label": "Klovnen",
                    "id": "154578"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "157579"
                },
                {
                    "display_label": "Styrmand Karlsens flammer",
                    "id": "154580"
                },
                {
                    "display_label": "Tordenskjolds Tøs",
                    "id": "154581"
                },
                {
                    "display_label": "Sælsomt mellemspil",
                    "id": "154582"
                },
                {
                    "display_label": "Betty Thejll Matiné",
                    "id": "154584"
                },
                {
                    "display_label": "Underholdning i Aarhus Teater",
                    "id": "1545885"
                },
                {
                    "display_label": "Balletskolens 12. elevopvisning",
                    "id": "154586"
                },
                {
                    "display_label": "årgang 1929",
                    "id": "154587"
                },
                {
                    "display_label": "Aarhus Musikforenings første koncert",
                    "id": "154588"
                },
                {
                    "display_label": "Aarhus Musikforenings anden koncert",
                    "id": "154590"
                },
                {
                    "display_label": "Aarhus Musikforenings tredje koncert",
                    "id": "154591"
                },
                {
                    "display_label": "Aarhus Musikforenings fjerde koncert",
                    "id": "154592"
                },
                {
                    "display_label": "Jomfruburet",
                    "id": "154593"
                },
                {
                    "display_label": "Journey´s End",
                    "id": "154594"
                },
                {
                    "display_label": "Julegave-Aften",
                    "id": "154595"
                },
                {
                    "display_label": "Et Sommeraftensspil",
                    "id": "154596"
                },
                {
                    "display_label": "Fru Dulskas Moral",
                    "id": "154598"
                },
                {
                    "display_label": "Lille Rosemarie",
                    "id": "154599"
                },
                {
                    "display_label": "Mascot",
                    "id": "154600"
                },
                {
                    "display_label": "Jeans Eventyr",
                    "id": "154601"
                },
                {
                    "display_label": "Hamlet",
                    "id": "118140"
                }
                ]
            },
            {
                "display_label": "Sæson 1930-31",
                "children": [
                {
                    "display_label": "Ambrosius",
                    "id": "111703"
                },
                {
                    "display_label": "Pygmalion",
                    "id": "112047"
                },
                {
                    "display_label": "De gamles Oprør",
                    "id": "112270"
                },
                {
                    "display_label": "Drengene fra Amerika",
                    "id": "111792"
                },
                {
                    "display_label": "Rejsen endt",
                    "id": "112057"
                },
                {
                    "display_label": "Bedre folks børn",
                    "id": "111724"
                },
                {
                    "display_label": "Fyrtøjet",
                    "id": "112251"
                },
                {
                    "display_label": "Flagermusen",
                    "id": "111861"
                },
                {
                    "display_label": "På Frierfødder",
                    "id": "112023"
                },
                {
                    "display_label": "Den indbildt syge",
                    "id": "112359"
                },
                {
                    "display_label": "Julegaveaften",
                    "id": "150169"
                },
                {
                    "display_label": "Hjem og Jord",
                    "id": "112328"
                },
                {
                    "display_label": "Charleys Tante",
                    "id": "111761"
                },
                {
                    "display_label": "Patsy",
                    "id": "112028"
                },
                {
                    "display_label": "Affæren i Mølleby",
                    "id": "111691"
                },
                {
                    "display_label": "Geisha eller Thehuset i Japan",
                    "id": "154736"
                },
                {
                    "display_label": "Hjemkomsten",
                    "id": "154737"
                },
                {
                    "display_label": "Hos Grevinden",
                    "id": "154738"
                },
                {
                    "display_label": "Indenfor murene",
                    "id": "154739"
                },
                {
                    "display_label": "Jorden rundt i 80 dage",
                    "id": "154741"
                },
                {
                    "display_label": "Lilly Ishøys Balletmatiné",
                    "id": "154742"
                },
                {
                    "display_label": "Balletskolens 13. Elevopvisning",
                    "id": "154743"
                },
                {
                    "display_label": "Co-Optimisternes Revy-Tourné",
                    "id": "154744"
                },
                {
                    "display_label": "Den første Mrs. Fraser",
                    "id": "154745"
                },
                {
                    "display_label": "Den store scene",
                    "id": "154746"
                },
                {
                    "display_label": "Den Stundesløse",
                    "id": "154747"
                },
                {
                    "display_label": "Aarhus Oliefabrik A/S´ Holberg Aften",
                    "id": "154749"
                },
                {
                    "display_label": "Dunungen",
                    "id": "154750"
                },
                {
                    "display_label": "Eurythmi-Forestilling",
                    "id": "154752"
                },
                {
                    "display_label": "Fruen har fri",
                    "id": "154753"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "154756"
                },
                {
                    "display_label": "Kor-recitation og Dramabilleder",
                    "id": "154758"
                },
                {
                    "display_label": "Talekor-Koncert",
                    "id": "154763"
                },
                {
                    "display_label": "Aarhus Teaters Anden Folkekoncert",
                    "id": "154764"
                },
                {
                    "display_label": "Aarhus Teaters Fjerde Folkekoncert",
                    "id": "154765"
                },
                {
                    "display_label": "Aarhus Teaters første folkekoncert",
                    "id": "154766"
                },
                {
                    "display_label": "Aarhus Teaters Tredje Folkekoncert",
                    "id": "154767"
                },
                {
                    "display_label": "Aarhus Teaters Julegave-Aften",
                    "id": "154768"
                },
                {
                    "display_label": "Stikkeren",
                    "id": "112137"
                }
                ]
            },
            {
                "display_label": "Sæson 1931-32",
                "children": [
                {
                    "display_label": "Flagermusen",
                    "id": "111862"
                },
                {
                    "display_label": "Næsten gift",
                    "id": "111991"
                },
                {
                    "display_label": "Feriegæsterne",
                    "id": "111857"
                },
                {
                    "display_label": "Den sidste Nat",
                    "id": "112083"
                },
                {
                    "display_label": "Landmandsliv",
                    "id": "112437"
                },
                {
                    "display_label": "Faust",
                    "id": "111853"
                },
                {
                    "display_label": "Geografi og Kærlighed",
                    "id": "112290"
                },
                {
                    "display_label": "Den bestøvlede Kat",
                    "id": "111727"
                },
                {
                    "display_label": "Sommer i Tyrol",
                    "id": "112118"
                },
                {
                    "display_label": "Moderate Løjer",
                    "id": "111961"
                },
                {
                    "display_label": "Julegaveaften",
                    "id": "150170"
                },
                {
                    "display_label": "Bundne Kræfter",
                    "id": "111747"
                },
                {
                    "display_label": "Jacob",
                    "id": "112367"
                },
                {
                    "display_label": "Soldat Svejk",
                    "id": "154782"
                },
                {
                    "display_label": "Aarhus Teaters første folkekoncert",
                    "id": "154784"
                },
                {
                    "display_label": "Aarhus Teaters anden folkekoncert",
                    "id": "154785"
                },
                {
                    "display_label": "Aarhus Teaters sidste folkekoncert",
                    "id": "154786"
                },
                {
                    "display_label": "Aarhus Teaters Julegave-Aften",
                    "id": "154787"
                },
                {
                    "display_label": "Skål Gipsy!",
                    "id": "154788"
                },
                {
                    "display_label": "Hvordan bliver jeg rig og lykkelig?",
                    "id": "154789"
                },
                {
                    "display_label": "Frederikkes Gæstespil",
                    "id": "154790"
                },
                {
                    "display_label": "Husmandstøsen",
                    "id": "154791"
                },
                {
                    "display_label": "Balletskolens 14. Elevopvisning",
                    "id": "154792"
                },
                {
                    "display_label": "Cant",
                    "id": "154793"
                },
                {
                    "display_label": "Elverhøj",
                    "id": "154794"
                },
                {
                    "display_label": "Fra Kap til Kronborg",
                    "id": "154795"
                },
                {
                    "display_label": "Povla Frijsh Koncert",
                    "id": "154796"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskab, 1. Koncert",
                    "id": "154797"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskab, 2. Koncert",
                    "id": "154798"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskab, 3.Koncert",
                    "id": "154799"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskab, 4. Koncert",
                    "id": "154800"
                },
                {
                    "display_label": "Aarhus Musikforening, 1ste Koncert",
                    "id": "154801"
                },
                {
                    "display_label": "Aarhus Musikforenings 2den Koncert",
                    "id": "154804"
                },
                {
                    "display_label": "Aarhus Musikforenings 4de Koncert",
                    "id": "154806"
                },
                {
                    "display_label": "Lavendelsøstrene",
                    "id": "118188"
                }
                ]
            },
            {
                "display_label": "Sæson 1932-33",
                "children": [
                {
                    "display_label": "Du og jeg",
                    "id": "111801"
                },
                {
                    "display_label": "Held i Spil",
                    "id": "112320"
                },
                {
                    "display_label": "Bundne Kræfter",
                    "id": "111748"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "112377"
                },
                {
                    "display_label": "Ordet",
                    "id": "112012"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "111997"
                },
                {
                    "display_label": "Når Violen blomstrer",
                    "id": "111976"
                },
                {
                    "display_label": "Axel og Valborg",
                    "id": "111719"
                },
                {
                    "display_label": "Forretning med Amerika",
                    "id": "111877"
                },
                {
                    "display_label": "Afsporet",
                    "id": "111693"
                },
                {
                    "display_label": "Tre gamle jomfruer",
                    "id": "112193"
                }
                ]
            },
            {
                "display_label": "Sæson 1933-34",
                "children": [
                {
                    "display_label": "Epilog",
                    "id": "112743"
                },
                {
                    "display_label": "Tre gamle jomfruer",
                    "id": "112194"
                },
                {
                    "display_label": "Vores lille Kone",
                    "id": "112237"
                },
                {
                    "display_label": "Høsten",
                    "id": "112348"
                },
                {
                    "display_label": "Etienne",
                    "id": "111826"
                },
                {
                    "display_label": "Lynggaard & Co",
                    "id": "111925"
                },
                {
                    "display_label": "Ti Minutters Alibi",
                    "id": "112162"
                },
                {
                    "display_label": "Rolfs Juleferie (senere titel: Rolfs Påskeferie)",
                    "id": "112069"
                },
                {
                    "display_label": "De tre Musketerer",
                    "id": "112196"
                },
                {
                    "display_label": "Maskinen",
                    "id": "111942"
                },
                {
                    "display_label": "Købmanden i Venezia",
                    "id": "112428"
                },
                {
                    "display_label": "Lille mand - hvad nu?",
                    "id": "112452"
                },
                {
                    "display_label": "Julegaveaften",
                    "id": "150172"
                },
                {
                    "display_label": "Grevinde Danner",
                    "id": "154943"
                },
                {
                    "display_label": "Dollarprinsessen",
                    "id": "154944"
                },
                {
                    "display_label": "Bajaderen",
                    "id": "154945"
                },
                {
                    "display_label": "Huset i orden",
                    "id": "154947"
                },
                {
                    "display_label": "Soldat Schweijk",
                    "id": "154949"
                },
                {
                    "display_label": "Landmandsliv ",
                    "id": "154976"
                },
                {
                    "display_label": "Familien Hallam",
                    "id": "154977"
                },
                {
                    "display_label": "Søn og Far",
                    "id": "154978"
                },
                {
                    "display_label": "Julegave-Aften",
                    "id": "154980"
                },
                {
                    "display_label": "Festforestilling ved indvielsen af Aarhus Universitet",
                    "id": "154981"
                },
                {
                    "display_label": "De tre fra det kongelige",
                    "id": "154982"
                },
                {
                    "display_label": "Liva-Revyen",
                    "id": "154983"
                },
                {
                    "display_label": "Koncert",
                    "id": "154984"
                },
                {
                    "display_label": "Propaganda-Koncert",
                    "id": "154986"
                },
                {
                    "display_label": "Ninon",
                    "id": "154987"
                },
                {
                    "display_label": "Koncert – Dybbøldagen",
                    "id": "154988"
                },
                {
                    "display_label": "Aarhus Teaters tredje Folkekoncert",
                    "id": "154989"
                },
                {
                    "display_label": "Balletskolens 16. Elevopvisning",
                    "id": "154990"
                },
                {
                    "display_label": "Ham, I søger",
                    "id": "155017"
                },
                {
                    "display_label": "Det er aldrig nok –",
                    "id": "155024"
                },
                {
                    "display_label": "Du skønne ungdom",
                    "id": "155025"
                },
                {
                    "display_label": "Søn af Zeus",
                    "id": "155026"
                },
                {
                    "display_label": "Ludvig Holbergs Fødsel",
                    "id": "155027"
                },
                {
                    "display_label": "Leonora Christina",
                    "id": "155028"
                },
                {
                    "display_label": "Aarhus Teaters Tredje Folkekoncert",
                    "id": "155029"
                },
                {
                    "display_label": "Aarhus Teaters Første Folkekoncert",
                    "id": "155030"
                },
                {
                    "display_label": "Fest-Koncert",
                    "id": "155031"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskabs Fjerde Koncert",
                    "id": "155032"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskabs Tredje Koncert",
                    "id": "155033"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskabs Første Koncert",
                    "id": "155034"
                },
                {
                    "display_label": "Aarhus Musikforenings 4de Koncert",
                    "id": "155035"
                },
                {
                    "display_label": "Aarhus Musikforenings 2den Koncert",
                    "id": "155036"
                },
                {
                    "display_label": "Pas på malingen",
                    "id": "154991"
                },
                {
                    "display_label": "Kameliadamen",
                    "id": "154992"
                },
                {
                    "display_label": "Orfeus i Underverdenen",
                    "id": "155001"
                },
                {
                    "display_label": "Det evigt kvindelige",
                    "id": "155003"
                },
                {
                    "display_label": "Julegave-Aften",
                    "id": "155004"
                },
                {
                    "display_label": "Cabaret med varmt",
                    "id": "155005"
                },
                {
                    "display_label": "Pigernes Jens ",
                    "id": "155007"
                },
                {
                    "display_label": "Kongeligt blod",
                    "id": "155008"
                },
                {
                    "display_label": "Leonora Christina",
                    "id": "155009"
                },
                {
                    "display_label": "Ninon",
                    "ID": "154024"
                }
                ]
            },
            {
                "display_label": "Sæson 1934-35",
                "children": [
                {
                    "display_label": "Katten i Sækken",
                    "id": "112396"
                },  
                {
                    "display_label": "Søndagsparadiset",
                    "id": "112167"
                },
                {
                    "display_label": "Gert Westphaler",
                    "id": "112295"
                },
                {
                    "display_label": "Intrigerne",
                    "id": "112769"
                },
                {
                    "display_label": "Før Syndfloden",
                    "id": "112257"
                },
                {
                    "display_label": "Ungdommen frem",
                    "id": "112212"
                },
                {
                    "display_label": "Den lille Pige med Svovlstikkerne",
                    "id": "111905"
                },
                {
                    "display_label": "Skærmydsler",
                    "id": "112096"
                },
                {
                    "display_label": "Tovaritch",
                    "id": "112184"
                },
                {
                    "display_label": "Som Fuglene sang",
                    "id": "112115"
                },
                {
                    "display_label": "Värmländingene",
                    "id": "112241"
                },
                {
                    "display_label": "Jurister",
                    "id": "112388"
                },
                {
                    "display_label": "Paaske",
                    "id": "112024"
                },
                {
                    "display_label": "Det er aldrig nok –",
                    "id": "155024"
                },
                {
                    "display_label": "Du skønne ungdom",
                    "id": "155025"
                },
                {
                    "display_label": "Søn af Zeus",
                    "id": "155026"
                },
                {
                    "display_label": "Ludvig Holbergs Fødsel",
                    "id": "155027"
                },
                {
                    "display_label": "Leonora Christina",
                    "id": "155028"
                },
                {
                    "display_label": "Aarhus Teaters Tredje Folkekoncert",
                    "id": "155029"
                },
                {
                    "display_label": "Aarhus Teaters Første Folkekoncert",
                    "id": "155030"
                },
                {
                    "display_label": "Fest-Koncert",
                    "id": "155031"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskabs Fjerde Koncert",
                    "id": "155032"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskabs Tredje Koncert",
                    "id": "155033"
                },
                {
                    "display_label": "Aarhus Philharmoniske Selskabs Første Koncert",
                    "id": "155034"
                },
                {
                    "display_label": "Aarhus Musikforenings 4de Koncert",
                    "id": "155035"
                },
                {
                    "display_label": "Aarhus Musikforenings 2den Koncert",
                    "id": "155036"
                },
                {
                    "display_label": "Julegaveforestilling",
                    "id": "150173"
                }
                ]
            },
            {
                "display_label": "Sæson 1935-36",
                "children": [
                {
                    "display_label": "Grevinde Maritza",
                    "id": "112277"
                },
                {
                    "display_label": "Co-Optimisterne kommer –",
                    "id": "155530"
                },	  
                {
                    "display_label": "Hansen-Bramslev, Medlem af Folketinget",
                    "id": "112307"
                },
                {
                    "display_label": "Tovaritch",
                    "id": "112185"
                },
                {
                    "display_label": "Nu er det Morgen",
                    "id": "111988"
                },
                {
                    "display_label": "Genboerne",
                    "id": "112286"
                },
                {
                    "display_label": "Peer Gynt",
                    "id": "112031"
                },
                {
                    "display_label": "Regnen",
                    "id": "112056"
                },
                {
                    "display_label": "Elverhøj",
                    "id": "111814"
                },
                {
                    "display_label": "Hyklere",
                    "id": "112344"
                },
                {
                    "display_label": "Melodien, der blev væk",
                    "id": "111944"
                },
                {
                    "display_label": "Julegaveaften",
                    "id": "150176"
                }
                ]
            },
            {
                "display_label": "Sæson 1936-37",
                "children": [
                {
                    "display_label": "Eventyr på fodrejsen",
                    "id": "111834"
                },
                {
                    "display_label": "Sommer i Tyrol",
                    "id": "112119"
                },
                {
                    "display_label": "Melodien, der blev væk",
                    "id": "111945"
                },
                {
                    "display_label": "Barnet",
                    "id": "111722"
                },
                {
                    "display_label": "Galgemanden",
                    "id": "112262"
                },
                {
                    "display_label": "Den indbildt syge",
                    "id": "112360"
                },
                {
                    "display_label": "Salome",
                    "id": "112075"
                },
                {
                    "display_label": "Den sidste Time",
                    "id": "112084"
                },
                {
                    "display_label": "Genboerne",
                    "id": "118225"
                },
                {
                    "display_label": "Aldrig et Kys",
                    "id": "111697"
                },
                {
                    "display_label": "Kongeloge",
                    "id": "112404"
                },
                {
                    "display_label": "Kærlighedens Kavalkade",
                    "id": "112422"
                },
                {
                    "display_label": "Når det går løs",
                    "id": "111974"
                },
                {
                    "display_label": "Moderglæder - Fadersorger",
                    "id": "111962"
                },
                {
                    "display_label": "Eva aftjener sin Barnepligt",
                    "id": "111828"
                },
                {
                    "display_label": "Gengangere",
                    "id": "118226"
                },
                {
                    "display_label": "Midnatscabaret",
                    "id": "150174"
                },
                {
                    "display_label": "Julegaveaften",
                    "id": "150175"
                }
                ]
            },
            {
                "display_label": "Sæson 1937-38",
                "children": [
                {
                    "display_label": "Laser og pjalter",
                    "id": "118322"
                },
                {
                    "display_label": "Penge som græs",
                    "id": "118323"
                },
                {
                    "display_label": "Eventyret",
                    "id": "118324"
                },
                {
                    "display_label": "Madame",
                    "id": "118325"
                },
                {
                    "display_label": "En dejlig dag",
                    "id": "118326"
                },
                {
                    "display_label": "Jeg kender Dem ikke",
                    "id": "118327"
                },
                {
                    "display_label": "Wienerbarnet",
                    "id": "118330"
                },
                {
                    "display_label": "Valsedrømme",
                    "id": "118331"
                },
                {
                    "display_label": "Karriere",
                    "id": "118548"
                },
                {
                    "display_label": "Hvo som forarger",
                    "id": "118549"
                },
                {
                    "display_label": "Sejren",
                    "id": "118550"
                },
                {
                    "display_label": "Piger paa Kostskole",
                    "id": "112035"
                },
                {
                    "display_label": "Manden fra Gaden",
                    "id": "111935"
                },
                {
                    "display_label": "I Brændingen",
                    "id": "112350"
                },
                {
                    "display_label": "Frihed",
                    "id": "111881"
                },
                {
                    "display_label": "En Skærsomrnernatsdrøm",
                    "id": "112100"
                },
                {
                    "display_label": "Fraskilt",
                    "id": "111879"
                },
                {
                    "display_label": "En spurv i tranedans",
                    "id": "112134"
                },
                {
                    "display_label": "Surt og Sødt",
                    "id": "112151"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "112249"
                },
                {
                    "display_label": "Kejseren af Portugalien",
                    "id": "112397"
                },
                {
                    "display_label": "Champagne",
                    "id": "150178"
                },
                {
                    "display_label": "En Idealist",
                    "id": "121269"
                },
                {
                    "display_label": "Julegaveaften",
                    "id": "150177"
                }
                ]
            },
            {
                "display_label": "Sæson 1938-39",
                "children": [
                {
                    "display_label": "Hvem som helst",
                    "id": "118328"
                },
                {
                    "display_label": "Lazarus & Fugl Fønix",
                    "id": "118329"
                },
                {
                    "display_label": "Diktatorinden",
                    "id": "118418"
                },
                {
                    "display_label": "Den lille verden",
                    "id": "118419"
                },
                {
                    "display_label": "En tosset Familie",
                    "id": "112181"
                },
                {
                    "display_label": "Han sidder ved Smeltediglen",
                    "id": "112314"
                },
                {
                    "display_label": "Søstrene på Kinnekullen",
                    "id": "112170"
                },
                {
                    "display_label": "Jul i købmandsgården",
                    "id": "112386"
                },
                {
                    "display_label": "Der var engang",
                    "id": "111784"
                },
                {
                    "display_label": "Kvinderne paa Niskavuori",
                    "id": "112413"
                },
                {
                    "display_label": "Indenfor Murene",
                    "id": "112365"
                },
                {
                    "display_label": "High Tor",
                    "id": "112327"
                },
                {
                    "display_label": "Moderne Idyl",
                    "id": "111963"
                },
                {
                    "display_label": "Charleys Tante",
                    "id": "111762"
                },
                {
                    "display_label": "Jomfruburet",
                    "id": "112381"
                },
                {
                    "display_label": "aprilsnarrene",
                    "id": "150183"
                },
                {
                    "display_label": "Julegaveaften",
                    "id": "150177"
                }
                ]
            },
            {
                "display_label": "Sæson 1939-40",
                "children": [
                {
                    "display_label": "Ved landevejen",
                    "id": "118410"
                },
                {
                    "display_label": "Anna Sophie Hedvig",
                    "id": "118412"
                },
                {
                    "display_label": "Ebberød Bank",
                    "id": "118413"
                },
                {
                    "display_label": "Portnerens Datter",
                    "id": "118415"
                },
                {
                    "display_label": "Puslespil",
                    "id": "118416"
                },
                {
                    "display_label": "Ungdommen kommer med årene",
                    "id": "112213"
                },
                {
                    "display_label": "Candida",
                    "id": "112730"
                },
                {
                    "display_label": "Bravo Tobias",
                    "id": "111735"
                },
                {
                    "display_label": "Bryllup i stilhed",
                    "id": "112721"
                },
                {
                    "display_label": "Oliver Twist",
                    "id": "112009"
                },
                {
                    "display_label": "Jul på Ravnsholt",
                    "id": "112387"
                },
                {
                    "display_label": "Julekavalkade",
                    "id": "118414"
                },
                {
                    "display_label": "De lykkelige Dage",
                    "id": "111921"
                },
                {
                    "display_label": "Charleys Tante",
                    "id": "111763"
                },
                {
                    "display_label": "Natten til 16. Januar",
                    "id": "111977"
                },
                {
                    "display_label": "Mindeforestilling for Kai Paaske",
                    "id": "118417"
                },
                {
                    "display_label": "Tre små piger",
                    "id": "112197"
                },
                {
                    "display_label": "Et rigtigt Mandfolk",
                    "id": "112067"
                },
                {
                    "display_label": "Du kan ikke ta' det med dig",
                    "id": "111796"
                }
                ]
            },
            {
                "display_label": "Sæson 1940-41",
                "children": [
                {
                    "display_label": "Lad os skilles",
                    "id": "118398"
                },
                {
                    "display_label": "Morgen, middag og aften",
                    "id": "118400"
                },
                {
                    "display_label": "Kvinder",
                    "id": "118406"
                },
                {
                    "display_label": "Cirkusrevyen",
                    "id": "118395"
                },
                {
                    "display_label": "Du kan ikke ta' det med dig",
                    "id": "111797"
                },
                {
                    "display_label": "Festaften i anledning af Chr. X' 70 års fødselsdag",
                    "id": "118401"
                },
                {
                    "display_label": "Egelykke",
                    "id": "111806"
                },
                {
                    "display_label": "Thea Jolles & Miskow Makwarth",
                    "id": "118402"
                },
                {
                    "display_label": "Atomsmedien",
                    "id": "111716"
                },
                {
                    "display_label": "Den store Fest",
                    "id": "112141"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "111998"
                },
                {
                    "display_label": "Julegave-aften",
                    "id": "118396"
                },
                {
                    "display_label": "Flagermusen",
                    "id": "111863"
                },
                {
                    "display_label": "Fruentimmerskolen",
                    "id": "111886"
                },
                {
                    "display_label": "Balance",
                    "id": "111720"
                },
                {
                    "display_label": "Spøgelsessonaten, Mordet i værtshuset",
                    "id": "118397"
                },
                {
                    "display_label": "Det gamle spil om enhver",
                    "id": "112273"
                },
                {
                    "display_label": "Et Dukkehjem",
                    "id": "111798"
                },
                {
                    "display_label": "Heinrich George-aften",
                    "id": "118475"
                },
                {
                    "display_label": "Min kone fra Paris",
                    "id": "111953"
                },
                {
                    "display_label": "Pilatus",
                    "id": "118407"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "118411"
                }
                ]
            },
            {
                "display_label": "Sæson 1941-42",
                "children": [
                {
                    "display_label": "Komplekser",
                    "id": "118518"
                },
                {
                    "display_label": "Hendes gamle Nåde",
                    "id": "118519"
                },
                {
                    "display_label": "Dyveke",
                    "id": "118507"
                },
                {
                    "display_label": "Tre Mænd i Sneen",
                    "id": "112195"
                },
                {
                    "display_label": "Ullabella",
                    "id": "112206"
                },
                {
                    "display_label": "Min kone fra Paris",
                    "id": "111954"
                },
                {
                    "display_label": "Sangaften med Emmi Leisner",
                    "id": "118399"
                },
                {
                    "display_label": "Helligtrekongersaften",
                    "id": "112322"
                },
                {
                    "display_label": "Premieren",
                    "id": "112043"
                },
                {
                    "display_label": "Aprilsnarrene",
                    "id": "111714"
                },
                {
                    "display_label": "Orfeus i Underverdenen",
                    "id": "112015"
                },
                {
                    "display_label": "Pygmalion",
                    "id": "112048"
                },
                {
                    "display_label": "Et Drømmespil",
                    "id": "111795"
                },
                {
                    "display_label": "- Og Guderne ler",
                    "id": "112006"
                },
                {
                    "display_label": "Venskab er violet",
                    "id": "112224"
                }
                ]
            },
            {
                "display_label": "Sæson 1942-43",
                "children": [
                {
                    "display_label": "Kampen om F. 6",
                    "id": "118509"
                },
                {
                    "display_label": "Den Kærlighed, Døden, Der brænder en ild",
                    "id": "118510"
                },
                {
                    "display_label": "Et spil, Frøken Julie",
                    "id": "118511"
                },
                {
                    "display_label": "Eventyret",
                    "id": "112105"
                },
                {
                    "display_label": "Sort Projektør",
                    "id": "112123"
                },
                {
                    "display_label": "Dunungen",
                    "id": "111800"
                },
                {
                    "display_label": "Vor By",
                    "id": "112236"
                },
                {
                    "display_label": "Helligtrekongersspillet",
                    "id": "112759"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "111999"
                },
                {
                    "display_label": "Som i Ungdommens Vår",
                    "id": "112117"
                },
                {
                    "display_label": "Brand",
                    "id": "111734"
                },
                {
                    "display_label": "Myrtekransen",
                    "id": "111969"
                },
                {
                    "display_label": "Det brænder i Sneen",
                    "id": "111786"
                },
                {
                    "display_label": "Kærlighed",
                    "id": "118142"
                },
                {
                    "display_label": "Julegaveaften",
                    "id": "150184"
                }
                ]
            },
            {
                "display_label": "Sæson 1943-44",
                "children": [
                {
                    "display_label": "Balletaften",
                    "id": "118512"
                },
                {
                    "display_label": "Amphitryon 38",
                    "id": "118513"
                },
                {
                    "display_label": "Cirkusrevyen",
                    "id": "118514"
                },
                {
                    "display_label": "Hornbæk Revyen",
                    "id": "118584"
                },
                {
                    "display_label": "Henning Schrams One Man Show",
                    "id": "118585"
                },
                {
                    "display_label": "En dejlig dag",
                    "id": "111778"
                },
                {
                    "display_label": "Livet er jo dejligt",
                    "id": "111910"
                },
                {
                    "display_label": "Eventyr på fodrejsen",
                    "id": "111835"
                },
                {
                    "display_label": "Det levende Lig",
                    "id": "112443"
                },
                {
                    "display_label": "Syndebukken, eller Var det retfærdigt?",
                    "id": "112805"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "112000"
                },
                {
                    "display_label": "Trold kan tæmmes",
                    "id": "112200"
                },
                {
                    "display_label": "Faust",
                    "id": "111854"
                },
                {
                    "display_label": "Tre finder en Kro",
                    "id": "112191"
                },
                {
                    "display_label": "To tråde",
                    "id": "112183"
                },
                {
                    "display_label": "Bladet og byen. Billeder fra Aarhus i fortid og nutid.",
                    "id": "150187"
                },
                {
                    "display_label": "Vildanden",
                    "id": "112230"
                },
                {
                    "display_label": "Julegaveaften",
                    "id": "150186"
                }
                ]
            },
            {
                "display_label": "Sæson 1944-45",
                "children": [
                {
                    "display_label": "Helsingør Revyen",
                    "id": "118580"
                },
                {
                    "display_label": "Cirkusrevyen",
                    "id": "118581"
                },
                {
                    "display_label": "Bajaderen",
                    "id": "118582"
                },
                {
                    "display_label": "Livet er jo dejligt",
                    "id": "118583"
                },
                {
                    "display_label": "Rebecca",
                    "id": "112051"
                },
                {
                    "display_label": "Når Mørket sænker sig",
                    "id": "111975"
                },
                {
                    "display_label": "Stjernevognen",
                    "id": "112139"
                },
                {
                    "display_label": "Høfeber",
                    "id": "112346"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "112001"
                },
                {
                    "display_label": "Middag Kl. 8",
                    "id": "111948"
                },
                {
                    "display_label": "Sparekassen",
                    "id": "112127"
                },
                {
                    "display_label": "Over Evne I",
                    "id": "112017"
                }
                ]
            },
            {
                "display_label": "Sæson 1945-46",
                "children": [
                {
                    "display_label": "Fra 9. April 1940 til 26. September 1945",
                    "id": "112749"
                },
                {
                    "display_label": "Tale for Kaj Munk",
                    "id": "112833"
                },
                {
                    "display_label": "Henning Schrams One Man Show",
                    "id": "118348"
                },
                {
                    "display_label": "Ebberød Bank",
                    "id": "118349"
                },
                {
                    "display_label": "Hamlet",
                    "id": "118350"
                },
                {
                    "display_label": "Cirkusrevyen",
                    "id": "118351"
                },
                {
                    "display_label": "Helsingør Revyen",
                    "id": "118355"
                },
                {
                    "display_label": "Bunbury",
                    "id": "118356"
                },
                {
                    "display_label": "Bodil Ipsen",
                    "id": "118357"
                },
                {
                    "display_label": "Bagtalelsens Skole",
                    "id": "118576"
                },
                {
                    "display_label": "Privatliv",
                    "id": "118577"
                },
                {
                    "display_label": "Den Vægelsindede",
                    "id": "112240"
                },
                {
                    "display_label": "Niels Ebbesen",
                    "id": "111982"
                },
                {
                    "display_label": "Festaften Chr. X",
                    "id": "118354"
                },
                {
                    "display_label": "Tre valse",
                    "id": "112828"
                },
                {
                    "display_label": "Ambrosius",
                    "id": "111704"
                },
                {
                    "display_label": "Nathan den vise",
                    "id": "118353"
                },
                {
                    "display_label": "Af Hjertens Lyst",
                    "id": "111692"
                },
                {
                    "display_label": "Før Canae",
                    "id": "112256"
                },
                {
                    "display_label": "Don Juan",
                    "id": "118352"
                },
                {
                    "display_label": "Rigtige Mennesker",
                    "id": "112066"
                },
                {
                    "display_label": "Den Glade Enke",
                    "id": "112298"
                },
                {
                    "display_label": "Bravo Tobias",
                    "id": "112722"
                },
                {
                    "display_label": "Midnats-Cabaret",
                    "id": "118578"
                },
                {
                    "display_label": "Midnatscabaret",
                    "id": "150189"
                },
                {
                    "display_label": "Skyggen af en sabotør",
                    "id": "118579"
                },
                {
                    "display_label": "I Rungsted Kro",
                    "id": "150190"
                },
                {
                    "display_label": "Julegaveaften",
                    "id": "150188"
                }
                ]
            },
            {
                "display_label": "Sæson 1946-47",
                "children": [
                {
                    "display_label": "Ballet- og Musikaften",
                    "id": "118385"
                },
                {
                    "display_label": "Teater",
                    "id": "118386"
                },
                {
                    "display_label": "Min kone spøger",
                    "id": "118387"
                },
                {
                    "display_label": "Fifferrevyen 1946",
                    "id": "118388"
                },
                {
                    "display_label": "Lukkede døre",
                    "id": "118389"
                },
                {
                    "display_label": "Drengen Fritz",
                    "id": "118391"
                },
                {
                    "display_label": "Indenfor Murene",
                    "id": "118392"
                },
                {
                    "display_label": "Helsingør Revyen",
                    "id": "118393"
                },
                {
                    "display_label": "Cirkusrevyen",
                    "id": "118394"
                },
                {
                    "display_label": "Den finske operaballet",
                    "id": "118620"
                },
                {
                    "display_label": "Tobaksvejen",
                    "id": "118623"
                },
                {
                    "display_label": "Den grønne elevator",
                    "id": "118624"
                },
                {
                    "display_label": "Seks kammerater",
                    "id": "112080"
                },
                {
                    "display_label": "Silkeborg",
                    "id": "112086"
                },
                {
                    "display_label": "Jean de France",
                    "id": "112371"
                },
                {
                    "display_label": "Ordet",
                    "id": "112013"
                },
                {
                    "display_label": "Grevinde Maritza",
                    "id": "112278"
                },
                {
                    "display_label": "En spurv i tranedans",
                    "id": "112135"
                },
                {
                    "display_label": "Eurydike",
                    "id": "111827"
                },
                {
                    "display_label": "Jægerbruden",
                    "id": "118390"
                },
                {
                    "display_label": "Det er Politiet",
                    "id": "111787"
                },
                {
                    "display_label": "På et hængende hår",
                    "id": "112022"
                },
                {
                    "display_label": "Julegaveaften",
                    "id": "150192"
                }
                ]
            },
            {
                "display_label": "Sæson 1947-48",
                "children": [
                {
                    "display_label": "Maskerade",
                    "id": "112787"
                },
                {
                    "display_label": "Uden ansigt",
                    "id": "118341"
                },
                {
                    "display_label": "Hornbæk Revyen",
                    "id": "118344"
                },
                {
                    "display_label": "I anstændighedens navn",
                    "id": "118345"
                },
                {
                    "display_label": "Privatchaufføren",
                    "id": "118615"
                },
                {
                    "display_label": "Efter",
                    "id": "118616"
                },
                {
                    "display_label": "Helsingør Revyen",
                    "id": "118617"
                },
                {
                    "display_label": "Den kloge mand",
                    "id": "118618"
                },
                {
                    "display_label": "Onkel Toms hytte",
                    "id": "118619"
                },
                {
                    "display_label": "Hos Grevinden",
                    "id": "118621"
                },
                {
                    "display_label": "Hende vi glemmer (livet er skønt, Rødt og gråt, Krista",
                    "id": "118622"
                },
                {
                    "display_label": "Født i går",
                    "id": "112255"
                },
                {
                    "display_label": "Elskovsdrikken",
                    "id": "118342"
                },
                {
                    "display_label": "Den svages ret",
                    "id": "112152"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "112002"
                },
                {
                    "display_label": "Kære Ruth",
                    "id": "112418"
                },
                {
                    "display_label": "Soldaterløjer",
                    "id": "112112"
                },
                {
                    "display_label": "Redaktionssekretæren",
                    "id": "112053"
                },
                {
                    "display_label": "Frit Valg",
                    "id": "111882"
                },
                {
                    "display_label": "En Idealist",
                    "id": "112355"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "112250"
                },
                {
                    "display_label": "Lige siden Adam og Eva",
                    "id": "111900"
                },
                {
                    "display_label": "Julegaveaften",
                    "id": "150193"
                }
                ]
            },
            {
                "display_label": "Sæson 1948-49",
                "children": [
                {
                    "display_label": "Jalousi (Hr. Lamberthier)",
                    "id": "118428"
                },
                {
                    "display_label": "Den svages ret",
                    "id": "118429"
                },
                {
                    "display_label": "Den Stundesløse",
                    "id": "118431"
                },
                {
                    "display_label": "Georgiske nationaldanse og sange",
                    "id": "118434"
                },
                {
                    "display_label": "Helsingør Revyen",
                    "id": "118435"
                },
                {
                    "display_label": "De fire små",
                    "id": "111858"
                },
                {
                    "display_label": "Glasmenageriet",
                    "id": "112300"
                },
                {
                    "display_label": "30 års henstand",
                    "id": "112187"
                },
                {
                    "display_label": "En Skærsomrnernatsdrøm",
                    "id": "112101"
                },
                {
                    "display_label": "Barberen i Sevilla",
                    "id": "112729"
                },
                {
                    "display_label": "Den dødsdømte",
                    "id": "118432"
                },
                {
                    "display_label": "F. N.-Hjælpens Humør-Nattiné",
                    "id": "118433"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "112003"
                },
                {
                    "display_label": "æventyrforestilling",
                    "id": "118430"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "112378"
                },
                {
                    "display_label": "Den rene Galskab eller Guds Fred",
                    "id": "112058"
                },
                {
                    "display_label": "Scapins Skalkestykker",
                    "id": "112078"
                },
                {
                    "display_label": "Carmen",
                    "id": "113005"
                },
                {
                    "display_label": "De urene hænder",
                    "id": "112823"
                },
                {
                    "display_label": "Unge mennesker",
                    "id": "112215"
                },
                {
                    "display_label": "Stedet er indhyllet i røg",
                    "id": "150194"
                },
                {
                    "display_label": "Magi",
                    "id": "111934"
                }
                ]
            },
            {
                "display_label": "Sæson 1949-50",
                "children": [
                {
                    "display_label": "Bajadser",
                    "id": "112728"
                },
                {
                    "display_label": "Omstigning til Paradis",
                    "id": "118436"
                },
                {
                    "display_label": "Helsingør Revyen",
                    "id": "118606"
                },
                {
                    "display_label": "For kærlighed eller penge",
                    "id": "118607"
                },
                {
                    "display_label": "Paaske",
                    "id": "118608"
                },
                {
                    "display_label": "Le spectacle Molière-Holberg",
                    "id": "118609"
                },
                {
                    "display_label": "Spansk dans",
                    "id": "118610"
                },
                {
                    "display_label": "Bortførelsen fra seraillet",
                    "id": "118611"
                },
                {
                    "display_label": "Parasitterne",
                    "id": "118614"
                },
                {
                    "display_label": "Regimentets Datter",
                    "id": "118613"
                },
                {
                    "display_label": "Liggende Gæster",
                    "id": "111901"
                },
                {
                    "display_label": "Ny Tid",
                    "id": "111990"
                },
                {
                    "display_label": "Rettens Pleje",
                    "id": "112060"
                },
                {
                    "display_label": "I de gamles vold",
                    "id": "150196"
                },
                {
                    "display_label": "Genboerne",
                    "id": "112287"
                },
                {
                    "display_label": "Solbadet",
                    "id": "118612"
                },
                {
                    "display_label": "Misforståelsen",
                    "id": "111956"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "112004"
                },
                {
                    "display_label": "Den lille Rødhætte",
                    "id": "111908"
                },
                {
                    "display_label": "Oklahoma!",
                    "id": "112007"
                },
                {
                    "display_label": "Gulddåsen",
                    "id": "112294"
                },
                {
                    "display_label": "Antigone",
                    "id": "112720"
                },
                {
                    "display_label": "Red Barnets festforestilling",
                    "id": "118605"
                },
                {
                    "display_label": "Kærlighed",
                    "id": "112419"
                },
                {
                    "display_label": "Nielsen",
                    "id": "111983"
                },
                {
                    "display_label": "Den politiske kandestøber",
                    "id": "112040"
                },
                {
                    "display_label": "5. Maj festen",
                    "id": "118437"
                }
                ]
            },
            {
                "display_label": "Sæson 1950-51",
                "children": [
                {
                    "display_label": "Juanna",
                    "id": "118491"
                },
                {
                    "display_label": "Gulddåsen",
                    "id": "118492"
                },
                {
                    "display_label": "José Greco Balletten",
                    "id": "112923"
                },
                {
                    "display_label": "Olivia",
                    "id": "118494"
                },
                {
                    "display_label": "Helsingør Revyen",
                    "id": "118587"
                },
                {
                    "display_label": "Ungdom og Galskab",
                    "id": "118588"
                },
                {
                    "display_label": "Høst & Teaterdirektøren",
                    "id": "118589"
                },
                {
                    "display_label": "Don Juan",
                    "id": "118590"
                },
                {
                    "display_label": "Flyvende sommer",
                    "id": "112607"
                },
                {
                    "display_label": "Sankt Hansaftens-spil",
                    "id": "112608"
                },
                {
                    "display_label": "50 år",
                    "id": "112880"
                },
                {
                    "display_label": "Den Vægelsindede",
                    "id": "112609"
                },
                {
                    "display_label": "Maskerade",
                    "id": "112610"
                },
                {
                    "display_label": "Jean de France",
                    "id": "112611"
                },
                {
                    "display_label": "Den politiske kandestøber",
                    "id": "112612"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "112613"
                },
                {
                    "display_label": "Erasmus Montanus",
                    "id": "112614"
                },
                {
                    "display_label": "Kærlighedens narre",
                    "id": "112615"
                },
                {
                    "display_label": "Hjemme kl. syv",
                    "id": "112616"
                },
                {
                    "display_label": "Den lille Rødhætte",
                    "id": "112617"
                },
                {
                    "display_label": "Annie Get Your Gun",
                    "id": "112618"
                },
                {
                    "display_label": "Tjavs og Mis på skovtur , senere Mis og Mads på skovtur",
                    "id": "118288"
                },
                {
                    "display_label": "Den indbildt syge",
                    "id": "112619"
                },
                {
                    "display_label": "En sælgers død",
                    "id": "112620"
                },
                {
                    "display_label": "Det fortryllede slot",
                    "id": "112623"
                },
                {
                    "display_label": "Bare man tror det",
                    "id": "112621"
                },
                {
                    "display_label": "Swedenhielms",
                    "id": "112622"
                }
                ]
            },
            {
                "display_label": "Sæson 1951-52",
                "children": [
                {
                    "display_label": "Bryllupsrejsen",
                    "id": "118360"
                },
                {
                    "display_label": "La Traviata",
                    "id": "118369"
                },
                {
                    "display_label": "Cirkusprinsessen",
                    "id": "118591"
                },
                {
                    "display_label": "Tordenskjolds tøs",
                    "id": "118592"
                },
                {
                    "display_label": "Dans under stjernerne",
                    "id": "112624"
                },
                {
                    "display_label": "En kvinde er overflødig",
                    "id": "112625"
                },
                {
                    "display_label": "Eventyr på fodrejsen",
                    "id": "112626"
                },
                {
                    "display_label": "Tony tegner en hest",
                    "id": "112627"
                },
                {
                    "display_label": "Bohème",
                    "id": "118368"
                },
                {
                    "display_label": "Jomfruburet",
                    "id": "112628"
                },
                {
                    "display_label": "Charleys Tante",
                    "id": "112629"
                },
                {
                    "display_label": "Damen vil nødig brændes",
                    "id": "112630"
                },
                {
                    "display_label": "Manden i månen",
                    "id": "112631"
                },
                {
                    "display_label": "Giv kejseren støvet",
                    "id": "112632"
                },
                {
                    "display_label": "Det fortryllede slot",
                    "id": "112635"
                },
                {
                    "display_label": "Kærlighedens sidespring",
                    "id": "112633"
                },
                {
                    "display_label": "Mis og Mads på skovtur",
                    "id": "112634"
                }
                ]
            },
            {
                "display_label": "Sæson 1952-53",
                "children": [
                {
                    "display_label": "Familien Chantrels ære",
                    "id": "118497"
                },
                {
                    "display_label": "Den fjerde mand",
                    "id": "112636"
                },
                {
                    "display_label": "Søskende",
                    "id": "112637"
                },
                {
                    "display_label": "Cant",
                    "id": "112638"
                },
                {
                    "display_label": "Figaros Bryllup",
                    "id": "118332"
                },
                {
                    "display_label": "Snedronningen",
                    "id": "112639"
                },
                {
                    "display_label": "Elverhøj",
                    "id": "112640"
                },
                {
                    "display_label": "I dagens lys",
                    "id": "112641"
                },
                {
                    "display_label": "Den forvandlede brudgom",
                    "id": "112642"
                },
                {
                    "display_label": "Nej",
                    "id": "112791"
                },
                {
                    "display_label": "Du skønne ungdom",
                    "id": "112643"
                },
                {
                    "display_label": "Rigoletto",
                    "id": "118537"
                },
                {
                    "display_label": "Landmandsliv",
                    "id": "112644"
                }
                ]
            },
            {
                "display_label": "Sæson 1953-54",
                "children": [
                {
                    "display_label": "Albert Herring",
                    "id": "118533"
                },
                {
                    "display_label": "Gengangere",
                    "id": "118534"
                },
                {
                    "display_label": "Frøken Julie",
                    "id": "118535"
                },
                {
                    "display_label": "Helsingør Revyen",
                    "id": "118538"
                },
                {
                    "display_label": "Kærlighed uden Strømper",
                    "id": "118539"
                },
                {
                    "display_label": "Eskapade",
                    "id": "118540"
                },
                {
                    "display_label": "Barberen i Sevilla",
                    "id": "118536"
                },
                {
                    "display_label": "Bedre folks børn",
                    "id": "112645"
                },
                {
                    "display_label": "Egelykke",
                    "id": "112646"
                },
                {
                    "display_label": "Hamlet",
                    "id": "112647"
                },
                {
                    "display_label": "Cosi fan tutte",
                    "id": "118531"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "112648"
                },
                {
                    "display_label": "Surbrødsdage",
                    "id": "112649"
                },
                {
                    "display_label": "Det lykkelige skibbrud",
                    "id": "112650"
                },
                {
                    "display_label": "Det gamle spil om enhver",
                    "id": "112651"
                },
                {
                    "display_label": "Maskerade",
                    "id": "118532"
                },
                {
                    "display_label": "Den kære familie",
                    "id": "112652"
                },
                {
                    "display_label": "Indenfor Murene",
                    "id": "112653"
                }
                ]
            },
            {
                "display_label": "Sæson 1954-55",
                "children": [
                {
                    "display_label": "Retten på vrangen",
                    "id": "112955"
                },
                {
                    "display_label": "Liden Kirsten og Den kongelige gæst",
                    "id": "118196"
                },
                {
                    "display_label": "Bajaderen",
                    "id": "118197"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "118198"
                },
                {
                    "display_label": "I Brændingen",
                    "id": "118199"
                },
                {
                    "display_label": "Et Dukkehjem",
                    "id": "118200"
                },
                {
                    "display_label": "Vor by",
                    "id": "118553"
                },
                {
                    "display_label": "Hustruleg",
                    "id": "118554"
                },
                {
                    "display_label": "Cosi fan tutte",
                    "id": "118555"
                },
                {
                    "display_label": "Jordens salt",
                    "id": "118556"
                },
                {
                    "display_label": "En måned på landet",
                    "id": "118557"
                },
                {
                    "display_label": "Kvartetten der sprængtes",
                    "id": "112654"
                },
                {
                    "display_label": "Parasitterne",
                    "id": "112655"
                },
                {
                    "display_label": "Vildanden",
                    "id": "112656"
                },
                {
                    "display_label": "Som man behager",
                    "id": "112657"
                },
                {
                    "display_label": "Krybskytten",
                    "id": "118208"
                },
                {
                    "display_label": "Jul i købmandsgården",
                    "id": "112658"
                },
                {
                    "display_label": "Teater",
                    "id": "112659"
                },
                {
                    "display_label": "Viften",
                    "id": "112660"
                },
                {
                    "display_label": "En spurv i tranedans",
                    "id": "112661"
                },
                {
                    "display_label": "Cavalleria Rusticana & Il Signor Bruschino",
                    "id": "118209"
                },
                {
                    "display_label": "Masser af guld",
                    "id": "112662"
                },
                {
                    "display_label": "Gedeøen",
                    "id": "112663"
                },
                {
                    "display_label": "Anklage mod en ukendt",
                    "id": "112664"
                },
                {
                    "display_label": "Thea Jolles Ballet",
                    "id": "118207"
                }
                ]
            },
            {
                "display_label": "Sæson 1955-56",
                "children": [
                {
                    "display_label": "Ximenez-Vargas Ensemblet",
                    "id": "112954"
                },
                {
                    "display_label": "Et Dukkehjem",
                    "id": "118203"
                },
                {
                    "display_label": "Den gode fregat Pinafore",
                    "id": "118204"
                },
                {
                    "display_label": "Dårskabens time",
                    "id": "118205"
                },
                {
                    "display_label": "Privatsekretæren",
                    "id": "118206"
                },
                {
                    "display_label": "Magtens brød",
                    "id": "112665"
                },
                {
                    "display_label": "Russisk Balletaften",
                    "id": "118211"
                },
                {
                    "display_label": "Don Pasquale",
                    "id": "118210"
                },
                {
                    "display_label": "Kammerballetten fra Det kgl. Teater",
                    "id": "118212"
                },
                {
                    "display_label": "En tjener - to herrer",
                    "id": "118286"
                },
                {
                    "display_label": "Gedeøen",
                    "id": "112666"
                },
                {
                    "display_label": "Mørket er lyst nok",
                    "id": "112667"
                },
                {
                    "display_label": "Det kinesiske klassiske operaselskab",
                    "id": "118130"
                },
                {
                    "display_label": "Champagnegaloppen",
                    "id": "112668"
                },
                {
                    "display_label": "Det lille thehus",
                    "id": "112455"
                },
                {
                    "display_label": "Vores egen ø",
                    "id": "112456"
                },
                {
                    "display_label": "Don Carlos",
                    "id": "113086"
                },
                {
                    "display_label": "Måne for de mislykkede",
                    "id": "112457"
                },
                {
                    "display_label": "Mens vi venter på Godot",
                    "id": "112458"
                },
                {
                    "display_label": "Det er her det sker",
                    "id": "112459"
                }
                ]
            },
            {
                "display_label": "Sæson 1956-57",
                "children": [
                {
                    "display_label": "Dollarprinsessen",
                    "id": "118123"
                },
                {
                    "display_label": "Regnmageren",
                    "id": "118124"
                },
                {
                    "display_label": "Født i går",
                    "id": "118125"
                },
                {
                    "display_label": "Det store bal",
                    "id": "118126"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "118127"
                },
                {
                    "display_label": "Lang dags rejse mod nat",
                    "id": "118128"
                },
                {
                    "display_label": "Mr. Pennypacker",
                    "id": "118129"
                },
                {
                    "display_label": "Ninotchka",
                    "id": "112460"
                },
                {
                    "display_label": "Eneren",
                    "id": "112461"
                },
                {
                    "display_label": "Den gale fra Chaillot",
                    "id": "112462"
                },
                {
                    "display_label": "Candida",
                    "id": "112463"
                },
                {
                    "display_label": "Tosca",
                    "id": "118132"
                },
                {
                    "display_label": "Aladdin",
                    "id": "112464"
                },
                {
                    "display_label": "Arsenik og gamle kniplinger",
                    "id": "112465"
                },
                {
                    "display_label": "Fru Inger til Østråt",
                    "id": "112466"
                },
                {
                    "display_label": "Bagtalelsens Skole",
                    "id": "112467"
                },
                {
                    "display_label": "Paaske",
                    "id": "112468"
                },
                {
                    "display_label": "Don Juan",
                    "id": "118131"
                },
                {
                    "display_label": "Bryllup i stilhed",
                    "id": "112469"
                },
                {
                    "display_label": "En søndag på Amager",
                    "id": "112470"
                }
                ]
            },
            {
                "display_label": "Sæson 1957-58",
                "children": [
                {
                    "display_label": "Sommer i Tyrol",
                    "id": "118153"
                },
                {
                    "display_label": "Iphigenia paa Tauris",
                    "id": "155696"
                },
                {
                    "display_label": "Ungdom og Galskab",
                    "id": "118154"
                },
                {
                    "display_label": "Den sovende prins",
                    "id": "118156"
                },
                {
                    "display_label": "Valsedrømme",
                    "id": "118157"
                },
                {
                    "display_label": "Den indbildt syge",
                    "id": "118158"
                },
                {
                    "display_label": "La Ventana, Søvngængersken, Graduation Ball",
                    "id": "118160"
                },
                {
                    "display_label": "Anne Franks dagbog",
                    "id": "112471"
                },
                {
                    "display_label": "Iphgenie auf Tauris",
                    "id": "118155"
                },
                {
                    "display_label": "Volpone",
                    "id": "118190"
                },
                {
                    "display_label": "Stævnemødet",
                    "id": "118191"
                },
                {
                    "display_label": "Anna Christie",
                    "id": "112472"
                },
                {
                    "display_label": "Carmen",
                    "id": "118159"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "112473"
                },
                {
                    "display_label": "Den politiske kandestøber",
                    "id": "112474"
                },
                {
                    "display_label": "Maria Stuart",
                    "id": "112475"
                },
                {
                    "display_label": "Seks kammerater",
                    "id": "112476"
                },
                {
                    "display_label": "Det hellige eksperiment",
                    "id": "112477"
                },
                {
                    "display_label": "Dage på en sky",
                    "id": "112478"
                },
                {
                    "display_label": "Jægerbruden",
                    "id": "118161"
                },
                {
                    "display_label": "Luften er svanger",
                    "id": "112479"
                }
                ]
            },
            {
                "display_label": "Sæson 1958-59",
                "children": [
                {
                    "display_label": "I forfald",
                    "id": "112766"
                },
                {
                    "display_label": "Som man behager",
                    "id": "112984"
                },
                {
                    "display_label": "Sanglæreren",
                    "id": "150202"
                },
                {
                    "display_label": "Figaros Bryllup",
                    "id": "118162"
                },
                {
                    "display_label": "Annie Get Your Gun",
                    "id": "118185"
                },
                {
                    "display_label": "Ebberød Bank",
                    "id": "118187"
                },
                {
                    "display_label": "Frøken Nitouche",
                    "id": "112480"
                },
                {
                    "display_label": "Ung vrede",
                    "id": "112481"
                },
                {
                    "display_label": "Weekend på landet",
                    "id": "112482"
                },
                {
                    "display_label": "Pygmalion",
                    "id": "112483"
                },
                {
                    "display_label": "Eugen Onegin",
                    "id": "118183"
                },
                {
                    "display_label": "En Skærsommernatsdrøm",
                    "id": "112484"
                },
                {
                    "display_label": "Han, hun og Satyren",
                    "id": "112485"
                },
                {
                    "display_label": "Flygtningen",
                    "id": "112486"
                },
                {
                    "display_label": "Den gamle dame besøger byen",
                    "id": "112487"
                },
                {
                    "display_label": "Mediert, Sanglærken",
                    "id": "118186"
                },
                {
                    "display_label": "Den Glade Enke",
                    "id": "112489"
                },
                {
                    "display_label": "Jacques eller underkastelsen",
                    "id": "112774"
                },
                {
                    "display_label": "Stemmerne",
                    "id": "112806"
                }
                ]
            },
            {
                "display_label": "Sæson 1959-60",
                "children": [
                {
                    "display_label": "Champagnegaloppen",
                    "id": "112987"
                },
                {
                    "display_label": "Min datters far",
                    "id": "118177"
                },
                {
                    "display_label": "Forår i Heidelberg",
                    "id": "118178"
                },
                {
                    "display_label": "Tribunehelten",
                    "id": "118179"
                },
                {
                    "display_label": "En mundsmag lykke",
                    "id": "118180"
                },
                {
                    "display_label": "Concerto Barocco, Chopiniana, Frøken Julie",
                    "id": "118184"
                },
                {
                    "display_label": "Sylfiden, Truffaldino, Irene Holm",
                    "id": "118487"
                },
                {
                    "display_label": "Sommer i Tyrol",
                    "id": "112490"
                },
                {
                    "display_label": "Scapins gavtyvestreger",
                    "id": "112491"
                },
                {
                    "display_label": "Han valgte at tie",
                    "id": "112492"
                },
                {
                    "display_label": "Peking Operaen",
                    "id": "112938"
                },
                {
                    "display_label": "Gal af kærlighed",
                    "id": "112493"
                },
                {
                    "display_label": "Regimentets Datter",
                    "id": "118182"
                },
                {
                    "display_label": "Julerejsen",
                    "id": "112494"
                },
                {
                    "display_label": "Helligtrekongersaften",
                    "id": "118138"
                },
                {
                    "display_label": "En Idealist",
                    "id": "112495"
                },
                {
                    "display_label": "High Tor",
                    "id": "118604"
                },
                {
                    "display_label": "Besøgstid",
                    "id": "112496"
                },
                {
                    "display_label": "Fædra",
                    "id": "112988"
                },
                {
                    "display_label": "Fidelio",
                    "id": "118181"
                },
                {
                    "display_label": "Stolene og Krapps sidste bånd",
                    "id": "112497"
                },
                {
                    "display_label": "Krapps sidste bånd",
                    "id": "112498"
                },
                {
                    "display_label": "Et Dukkehjem",
                    "id": "112499"
                }
                ]
            },
            {
                "display_label": "Sæson 1960-61",
                "children": [
                {
                    "display_label": "Nej",
                    "id": "112792"
                },
                {
                    "display_label": "Adolf Wantzins 50 års jubilæumsfest",
                    "id": "155710"
                },  
                {
                    "display_label": "To på vippen",
                    "id": "118213"
                },
                {
                    "display_label": "Vintergatan",
                    "id": "118488"
                },
                {
                    "display_label": "Grevinde Maritza",
                    "id": "118201"
                },
                {
                    "display_label": "Änkeman Jarl",
                    "id": "118202"
                },
                {
                    "display_label": "Der må være en grænse",
                    "id": "112500"
                },
                {
                    "display_label": "En Idealist",
                    "id": "112501"
                },
                {
                    "display_label": "Der var engang",
                    "id": "112502"
                },
                {
                    "display_label": "Stolene og Krapps sidste bånd",
                    "id": "112504"
                },
                {
                    "display_label": "Besættelse",
                    "id": "112503"
                },
                {
                    "display_label": "Macbeth",
                    "id": "118214"
                },
                {
                    "display_label": "Barberen i Sevilla",
                    "id": "118215"
                },
                {
                    "display_label": "Folk og røvere i Kardemommeby",
                    "id": "112505"
                },
                {
                    "display_label": "Når engle elsker",
                    "id": "112506"
                },
                {
                    "display_label": "Landmandsliv",
                    "id": "118148"
                },
                {
                    "display_label": "Fra bord til bord",
                    "id": "112507"
                },
                {
                    "display_label": "Mutter Courage",
                    "id": "118170"
                },
                {
                    "display_label": "Tiger-Harry",
                    "id": "112508"
                },
                {
                    "display_label": "Den grønne elevator",
                    "id": "118164"
                },
                {
                    "display_label": "Lastens vej",
                    "id": "118163"
                },
                {
                    "display_label": "Natteherberget",
                    "id": "112509"
                },
                {
                    "display_label": "Skærmydsler",
                    "id": "112510"
                },
                {
                    "display_label": "Flagermusen",
                    "id": "112512"
                },
                {
                    "display_label": "Morfin",
                    "id": "112511"
                },
                {
                    "display_label": "Paddehatten",
                    "id": "112799"
                }
                ]
            },
            {
                "display_label": "Sæson 1961-62",
                "children": [
                {
                    "display_label": "Paria",
                    "id": "112802"
                },
                {
                    "display_label": "Bajaderen",
                    "id": "118303"
                },
                {
                    "display_label": "Die Hochzeit des Figaro",
                    "id": "118304"
                },
                {
                    "display_label": "Privatliv",
                    "id": "118305"
                },
                {
                    "display_label": "Pauken und Trompeten",
                    "id": "118307"
                },
                {
                    "display_label": "Fuglekræmmeren",
                    "id": "118308"
                },
                {
                    "display_label": "De der sejrede",
                    "id": "118485"
                },
                {
                    "display_label": "Koncert",
                    "id": "118486"
                },
                {
                    "display_label": "Rose Marie",
                    "id": "112513"
                },
                {
                    "display_label": "Biedermann og brandstifterne",
                    "id": "112514"
                },
                {
                    "display_label": "Værs'go og spis",
                    "id": "112515"
                },
                {
                    "display_label": "Den farlige leg",
                    "id": "112516"
                },
                {
                    "display_label": "Faust",
                    "id": "118302"
                },
                {
                    "display_label": "Elverhøj",
                    "id": "112517"
                },
                {
                    "display_label": "Ulysses von Ithacia",
                    "id": "112518"
                },
                {
                    "display_label": "Trappen",
                    "id": "112519"
                },
                {
                    "display_label": "La Traviata",
                    "id": "118306"
                },
                {
                    "display_label": "Eventyr på fodrejsen",
                    "id": "112520"
                },
                {
                    "display_label": "Pariserkomedie",
                    "id": "112521"
                },
                {
                    "display_label": "De skyldfri",
                    "id": "112522"
                },
                {
                    "display_label": "Den stærkeste",
                    "id": "112734"
                },
                {
                    "display_label": "De to bødler",
                    "id": "112739"
                },
                {
                    "display_label": "Historien fra Zoo",
                    "id": "112753"
                }
                ]
            },
            {
                "display_label": "Sæson 1962-63",
                "children": [
                {
                    "display_label": "Tartuffe",
                    "id": "112525"
                },
                {
                    "display_label": "Kongsemnerne",
                    "id": "112953"
                },
                {
                    "display_label": "Før solnedgang",
                    "id": "150210"
                },
                {
                    "display_label": "Vor Sonnenuntergang",
                    "id": "118276"
                },
                {
                    "display_label": "Maskeballet",
                    "id": "150211"
                },
                {
                    "display_label": "Søvngængersken",
                    "id": "150212"
                },
                {
                    "display_label": "Den skønne Donau",
                    "id": "150213"
                },
                {
                    "display_label": "Tre små piger",
                    "id": "118278"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "118279"
                },
                {
                    "display_label": "Hr. Lamberthier",
                    "id": "118281"
                },
                {
                    "display_label": "Andorra",
                    "id": "118282"
                },
                {
                    "display_label": "Tosca",
                    "id": "118283"
                },
                {
                    "display_label": "Glade dage",
                    "id": "118284"
                },
                {
                    "display_label": "Orfeus i Underverdenen",
                    "id": "118309"
                },
                {
                    "display_label": "Peer Gynt",
                    "id": "118320"
                },
                {
                    "display_label": "Solitaire, Søvngængersken, Den skønne Donau",
                    "id": "118321"
                },
                {
                    "display_label": "Jomfruburet",
                    "id": "118133"
                },
                {
                    "display_label": "Phakavali",
                    "id": "112797"
                },
                {
                    "display_label": "Stakkels Don Juan",
                    "id": "112523"
                },
                {
                    "display_label": "Familiens hvide får",
                    "id": "112524"
                },
                {
                    "display_label": "Sparekassen",
                    "id": "112526"
                },
                {
                    "display_label": "Boris Godunov",
                    "id": "118277"
                },
                {
                    "display_label": "Folk og røvere i Kardemommeby",
                    "id": "112527"
                },
                {
                    "display_label": "Madame",
                    "id": "112528"
                },
                {
                    "display_label": "Rejsen",
                    "id": "112529"
                },
                {
                    "display_label": "Madame Butterfly",
                    "id": "118280"
                },
                {
                    "display_label": "Kattene",
                    "id": "112530"
                },
                {
                    "display_label": "Fødselsdagsselskabet",
                    "id": "112531"
                },
                {
                    "display_label": "Skillingsoperaen eller Laser og Pjalter",
                    "id": "112532"
                }
                ]
            },
            {
                "display_label": "Sæson 1963-64",
                "children": [
                {
                    "display_label": "Den kaukasiske kridtcirkel",
                    "id": "118255"
                },
                {
                    "display_label": "Kildereisen",
                    "id": "112533"
                },
                {
                    "display_label": "Kom ned på jorden",
                    "id": "112534"
                },
                {
                    "display_label": "Rejsen til de grønne skygger",
                    "id": "112535"
                },
                {
                    "display_label": "Romeo og Julie",
                    "id": "118169"
                },
                {
                    "display_label": "Job Klokkemagers datter",
                    "id": "112536"
                },
                {
                    "display_label": "Elektra",
                    "id": "118285"
                },
                {
                    "display_label": "Medea",
                    "id": "112952"
                },
                {
                    "display_label": "Køkkenelevatoren",
                    "id": "112775"
                },
                {
                    "display_label": "Det polske pantomime statsteater",
                    "id": "118254"
                },
                {
                    "display_label": "Kristin Lavransdatter",
                    "id": "112537"
                },
                {
                    "display_label": "Cosi fan tutte",
                    "id": "118257"
                },
                {
                    "display_label": "Lille prinsesse Snefnug",
                    "id": "112538"
                },
                {
                    "display_label": "Gigi",
                    "id": "112539"
                },
                {
                    "display_label": "Stedfortræderen",
                    "id": "112540"
                },
                {
                    "display_label": "Othello",
                    "id": "118256"
                },
                {
                    "display_label": "Den kære afdøde (opført sammen med Woyzeck)",
                    "id": "112541"
                },
                {
                    "display_label": "Woyzeck",
                    "id": "118251"
                },
                {
                    "display_label": "Festaften for Galina Ulanova",
                    "id": "118259"
                },
                {
                    "display_label": "De tre klaphatte",
                    "id": "112542"
                },
                {
                    "display_label": "Friederike",
                    "id": "112543"
                }
                ]
            },
            {
                "display_label": "Sæson 1964-65",
                "children": [
                {
                    "display_label": "Bessie Smith´s død, opført sammen med Også jeg er Amerika",
                    "id": "112724"
                },
                {
                    "display_label": "Drot og marsk",
                    "id": "112735"
                },
                {
                    "display_label": "Western Theatre Ballet",
                    "id": "112937"
                },
                {
                    "display_label": "Bygmester Solness",
                    "id": "118238"
                },
                {
                    "display_label": "Vildanden",
                    "id": "118252"
                },
                {
                    "display_label": "Sommer i Tyrol",
                    "id": "118261"
                },
                {
                    "display_label": "Osvald Helmuth, one-man-show",
                    "id": "118489"
                },
                {
                    "display_label": "Friederike",
                    "id": "112544"
                },
                {
                    "display_label": "Mattan",
                    "id": "112936"
                },
                {
                    "display_label": "Helte",
                    "id": "112545"
                },
                {
                    "display_label": "Forlanger I mirakler",
                    "id": "112546"
                },
                {
                    "display_label": "Huslæreren",
                    "id": "112547"
                },
                {
                    "display_label": "Lille prinsesse Snefnug",
                    "id": "112548"
                },
                {
                    "display_label": "Marcel Marceau",
                    "id": "118260"
                },
                {
                    "display_label": "Ingeborg Brams",
                    "id": "118258"
                },
                {
                    "display_label": "Stakkels Bitos",
                    "id": "112549"
                },
                {
                    "display_label": "En damekomedie",
                    "id": "112550"
                },
                {
                    "display_label": "Lucretia",
                    "id": "118253"
                },
                {
                    "display_label": "Pariserliv",
                    "id": "112552"
                },
                {
                    "display_label": "ærkeengle laver aldrig fiduser",
                    "id": "112551"
                }
                ]
            },
            {
                "display_label": "Sæson 1965-66",
                "children": [
                {
                    "display_label": "Ansøgerne",
                    "id": "112719"
                },
                {
                    "display_label": "Die Irre von Chaillot",
                    "id": "112950"
                },
                {
                    "display_label": "The Maids, Mysteries and other small Pieces",
                    "id": "118230"
                },
                {
                    "display_label": "Det dansende æsel",
                    "id": "118231"
                },
                {
                    "display_label": "Flagermusen",
                    "id": "118232"
                },
                {
                    "display_label": "Et spil om lykke",
                    "id": "118234"
                },
                {
                    "display_label": "Skatteøen",
                    "id": "118235"
                },
                {
                    "display_label": "Udviklinger",
                    "id": "118237"
                },
                {
                    "display_label": "Valsedrømme",
                    "id": "118297"
                },
                {
                    "display_label": "Krybskytten",
                    "id": "118490"
                },
                {
                    "display_label": "Drot og marsk",
                    "id": "118239"
                },
                {
                    "display_label": "Pariserliv",
                    "id": "112798"
                },
                {
                    "display_label": "En kvinde er en straf",
                    "id": "112553"
                },
                {
                    "display_label": "Jenny von Westphalen, Frisk mod, Klassisk spil",
                    "id": "118236"
                },
                {
                    "display_label": "Maskeraden",
                    "id": "112554"
                },
                {
                    "display_label": "Døde sjæle",
                    "id": "112555"
                },
                {
                    "display_label": "Der var engang en kedel",
                    "id": "112556"
                },
                {
                    "display_label": "Jenufa",
                    "id": "118233"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "118195"
                },
                {
                    "display_label": "Dyrene i Hakkebakkeskoven",
                    "id": "112557"
                },
                {
                    "display_label": "Operation Charlie",
                    "id": "112558"
                },
                {
                    "display_label": "Købmanden i Venezia",
                    "id": "118194"
                },
                {
                    "display_label": "Marcel Marceau",
                    "id": "112951"
                },
                {
                    "display_label": "Marcolfa",
                    "id": "112559"
                },
                {
                    "display_label": "Hva' ska' vi lave",
                    "id": "112560"
                },
                {
                    "display_label": "Kiss me Kate",
                    "id": "112561"
                }
                ]
            },
            {
                "display_label": "Sæson 1966-67",
                "children": [
                {
                    "display_label": "Snoren",
                    "id": "112808"
                },
                {
                    "display_label": "Gustav",
                    "id": "112949"
                },
                {
                    "display_label": "Enetime, Carmen, Graduation Ball",
                    "id": "118289"
                },
                {
                    "display_label": "Greven af Luxembourg",
                    "id": "118293"
                },
                {
                    "display_label": "Farinelli",
                    "id": "118295"
                },
                {
                    "display_label": "Glasmenageriet",
                    "id": "118296"
                },
                {
                    "display_label": "Den fine mand",
                    "id": "112562"
                },
                {
                    "display_label": "Hvad siger naboerne",
                    "id": "112563"
                },
                {
                    "display_label": "Tovet",
                    "id": "112564"
                },
                {
                    "display_label": "Særlingen",
                    "id": "112565"
                },
                {
                    "display_label": "Vore torsdage",
                    "id": "112566"
                },
                {
                    "display_label": "Troubaduren",
                    "id": "118294"
                },
                {
                    "display_label": "Dyrene i Hakkebakkeskoven",
                    "id": "112567"
                },
                {
                    "display_label": "Det suser i Sassafras'en",
                    "id": "112568"
                },
                {
                    "display_label": "Djævelens discipel",
                    "id": "112570"
                },
                {
                    "display_label": "Sorgen og ingenting",
                    "id": "112569"
                },
                {
                    "display_label": "Bohème",
                    "id": "118292"
                },
                {
                    "display_label": "Pas på malingen",
                    "id": "112571"
                },
                {
                    "display_label": "Boy Friend",
                    "id": "112572"
                }
                ]
            },
            {
                "display_label": "Sæson 1967-68",
                "children": [
                {
                    "display_label": "Av for katten",
                    "id": "112946"
                },
                {
                    "display_label": "The Skin of our Teeth",
                    "id": "112948"
                },
                {
                    "display_label": "Dollarprinsessen",
                    "id": "118268"
                },
                {
                    "display_label": "Forår i Heidelberg",
                    "id": "118271"
                },
                {
                    "display_label": "Fordi vi elsker dig",
                    "id": "118290"
                },
                {
                    "display_label": "Die Entführung aus dem Serail",
                    "id": "118373"
                },
                {
                    "display_label": "Balletgæstespil",
                    "id": "118374"
                },
                {
                    "display_label": "Boy Friend",
                    "id": "112573"
                },
                {
                    "display_label": "Richard den Anden",
                    "id": "112574"
                },
                {
                    "display_label": "Narrene",
                    "id": "118291"
                },
                {
                    "display_label": "Djævelens discipel",
                    "id": "112575"
                },
                {
                    "display_label": "Det tvungne ægteskab",
                    "id": "112576"
                },
                {
                    "display_label": "Den pantsatte bondedreng, opført sammen med Det tvungne ægteskab",
                    "id": "112747"
                },
                {
                    "display_label": "Frøken Julie",
                    "id": "112945"
                },
                {
                    "display_label": "Tango",
                    "id": "112577"
                },
                {
                    "display_label": "Lille Malcolm og hans kamp mod Eunukkerne",
                    "id": "112578"
                },
                {
                    "display_label": "Carmen",
                    "id": "118269"
                },
                {
                    "display_label": "Jorden rundt i 80 dage",
                    "id": "112579"
                },
                {
                    "display_label": "Penge i kisten",
                    "id": "112580"
                },
                {
                    "display_label": "Tryllefløjten",
                    "id": "118270"
                },
                {
                    "display_label": "Kean",
                    "id": "112581"
                },
                {
                    "display_label": "Bal i Den Borgerlige",
                    "id": "112582"
                }
                ]
            },
            {
                "display_label": "Sæson 1968-69",
                "children": [
                {
                    "display_label": "Den usynlige hund",
                    "id": "112947"
                },
                {
                    "display_label": "Skat, du ved, jeg ikke kan høre, hvad du siger, når vandet løber",
                    "id": "118262"
                },
                {
                    "display_label": "Konservatoriet, Tango Chikane, Galla-Variationer",
                    "id": "118264"
                },
                {
                    "display_label": "Balletaften",
                    "id": "150237"
                },
                {
                    "display_label": "Cosi fan tutte",
                    "id": "118265"
                },
                {
                    "display_label": "Grevinde Maritza",
                    "id": "118267"
                },
                {
                    "display_label": "Den solgte brud",
                    "id": "118380"
                },
                {
                    "display_label": "Bal i Den Borgerlige",
                    "id": "112583"
                },
                {
                    "display_label": "Othello",
                    "id": "112584"
                },
                {
                    "display_label": "Marcel Marceau",
                    "id": "118266"
                },
                {
                    "display_label": "Sangen om fugleskræmslet",
                    "id": "112591"
                },
                {
                    "display_label": "Utryg balance",
                    "id": "112585"
                },
                {
                    "display_label": "De kloge damer og Charlie",
                    "id": "112586"
                },
                {
                    "display_label": "Musikanterne kommer til byen",
                    "id": "112587"
                },
                {
                    "display_label": "Molière har travlt. Se også Forspil i Versailles og Den Gerrige",
                    "id": "112588"
                },
                {
                    "display_label": "Manden i glasburet",
                    "id": "112589"
                },
                {
                    "display_label": "Mordernes nat",
                    "id": "112592"
                },
                {
                    "display_label": "Besøgeren & Bryllupsrejse",
                    "id": "118263"
                },
                {
                    "display_label": "Livsens ondskab",
                    "id": "112590"
                }
                ]
            },
            {
                "display_label": "Sæson 1969-70",
                "children": [
                {
                    "display_label": "Ferai",
                    "id": "118242"
                },
                {
                    "display_label": "Prisen",
                    "id": "118246"
                },
                {
                    "display_label": "Jomfruburet",
                    "id": "118247"
                },
                {
                    "display_label": "Komedie i mørke",
                    "id": "118250"
                },
                {
                    "display_label": "Se kvinder",
                    "id": "118379"
                },
                {
                    "display_label": "Canterbury fortællinger",
                    "id": "112593"
                },
                {
                    "display_label": "Silkestigen",
                    "id": "118248"
                },
                {
                    "display_label": "Svinedrengen, Pierrot Lunaire, La ventana",
                    "id": "118245"
                },
                {
                    "display_label": "Medea fra Mbongo",
                    "id": "112602"
                },
                {
                    "display_label": "Hvor smed vi bomber i går?",
                    "id": "112594"
                },
                {
                    "display_label": "Fru Engells Rosenbed",
                    "id": "112595"
                },
                {
                    "display_label": "Dynamit i natten",
                    "id": "118241"
                },
                {
                    "display_label": "Greven af Luxembourg",
                    "id": "118244"
                },
                {
                    "display_label": "Musikanterne kommer til byen",
                    "id": "112596"
                },
                {
                    "display_label": "Erik Mørk",
                    "id": "118243"
                },
                {
                    "display_label": "Jeg vil ikke dø som idiot",
                    "id": "112603"
                },
                {
                    "display_label": "Volpone",
                    "id": "112597"
                },
                {
                    "display_label": "Mahagonny",
                    "id": "118249"
                },
                {
                    "display_label": "I morgen - et vindue til gaden",
                    "id": "112598"
                },
                {
                    "display_label": "Højt spil med tændstikker",
                    "id": "112604"
                },
                {
                    "display_label": "Pang-Pang",
                    "id": "112600"
                },
                {
                    "display_label": "Det åh så gode selskab",
                    "id": "112599"
                },
                {
                    "display_label": "Glade dage",
                    "id": "118228"
                },
                {
                    "display_label": "Spillemand på en tagryg",
                    "id": "112601"
                }
                ]
            },
            {
                "display_label": "Sæson 1970-71",
                "children": [
                {
                    "display_label": "Faser, Bagage, De syv Dødssynder",
                    "id": "118377"
                },
                {
                    "display_label": "En aften med Oscar Wilde",
                    "id": "118378"
                },
                {
                    "display_label": "En sælgers død",
                    "id": "118381"
                },
                {
                    "display_label": "Laser og pjalter",
                    "id": "118382"
                },
                {
                    "display_label": "Christoffer Columbus & Escorial",
                    "id": "118449"
                },
                {
                    "display_label": "Spillemand på en tagryg",
                    "id": "112605"
                },
                {
                    "display_label": "En Folkefjende",
                    "id": "112606"
                },
                {
                    "display_label": "Natten og dukkerne",
                    "id": "112675"
                },
                {
                    "display_label": "Mikadoen",
                    "id": "112956"
                },
                {
                    "display_label": "H. M. S. Pinafore",
                    "id": "112957"
                },
                {
                    "display_label": "Duefesten",
                    "id": "112669"
                },
                {
                    "display_label": "Nu går den på Dagmar",
                    "id": "112676"
                },
                {
                    "display_label": "Rigoletto",
                    "id": "118375"
                },
                {
                    "display_label": "Pang-Pang",
                    "id": "112671"
                },
                {
                    "display_label": "Vennerne",
                    "id": "112670"
                },
                {
                    "display_label": "Harvey",
                    "id": "112672"
                },
                {
                    "display_label": "Agent 0012",
                    "id": "112673"
                },
                {
                    "display_label": "Fra Diavolo",
                    "id": "118376"
                },
                {
                    "display_label": "Gift dig, Bobby",
                    "id": "112674"
                }
                ]
            },
            {
                "display_label": "Sæson 1971-72",
                "children": [
                {
                    "display_label": "Helligtrekongersaften",
                    "id": "112680"
                },
                {
                    "display_label": "Det sete afhænger, opført sammen med Pædagogen som S og S (s. d.)",
                    "id": "112731"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "118448"
                },
                {
                    "display_label": "Victor Borge",
                    "id": "118456"
                },
                {
                    "display_label": "Smilets Land",
                    "id": "118457"
                },
                {
                    "display_label": "Kære Antoine",
                    "id": "112677"
                },
                {
                    "display_label": "Danse fra Indien",
                    "id": "118454"
                },
                {
                    "display_label": "Palach",
                    "id": "112684"
                },
                {
                    "display_label": "Don Pasquale",
                    "id": "118455"
                },
                {
                    "display_label": "Galileis liv",
                    "id": "112678"
                },
                {
                    "display_label": "Katten i Ghettoen",
                    "id": "112679"
                },
                {
                    "display_label": "Falstaff",
                    "id": "118452"
                },
                {
                    "display_label": "Pinocchio",
                    "id": "118229"
                },
                {
                    "display_label": "S og S. Pædagogen og Det sete afhænger af øjnene",
                    "id": "112685"
                },
                {
                    "display_label": "Så bytter vi",
                    "id": "112681"
                },
                {
                    "display_label": "Fidelio",
                    "id": "118453"
                },
                {
                    "display_label": "Kalkunen - en polsk fabel",
                    "id": "112686"
                },
                {
                    "display_label": "Med liget som indsats",
                    "id": "112682"
                },
                {
                    "display_label": "Den italienske stråhat",
                    "id": "112683"
                }
                ]
            },
            {
                "display_label": "Sæson 1972-73",
                "children": [
                {
                    "display_label": "Hvem har ret?",
                    "id": "112755"
                },
                {
                    "display_label": "Prisme",
                    "id": "150271"
                },
                {
                    "display_label": "The Moor's Pavane",
                    "id": "150273"
                },
                {
                    "display_label": "Don Juan",
                    "id": "112931"
                },
                {
                    "display_label": "Faust",
                    "id": "118450"
                },
                {
                    "display_label": "Harap Alb",
                    "id": "118451"
                },
                {
                    "display_label": "Sommer i Tyrol",
                    "id": "118541"
                },
                {
                    "display_label": "The Moor's Pavane, Dødens Triumf, Prisme",
                    "id": "118542"
                },
                {
                    "display_label": "Husker du?",
                    "id": "112687"
                },
                {
                    "display_label": "Uden hoved og hale",
                    "id": "112694"
                },
                {
                    "display_label": "Kugler i Solnedgangen",
                    "id": "112693"
                }
                ]
            },
            {
                "display_label": "Sæson 1973-74",
                "children": [
                {
                    "display_label": "Mutter Courage",
                    "id": "112840"
                },
                {
                    "display_label": "Pigesnak",
                    "id": "118568"
                },
                {
                    "display_label": "Hellere synger jeg end græder",
                    "id": "118569"
                },
                {
                    "display_label": "Balletgæstespil",
                    "id": "118571"
                },
                {
                    "display_label": "Svantes viser",
                    "id": "118572"
                },
                {
                    "display_label": "Cornelis Wreeswijk",
                    "id": "118573"
                },
                {
                    "display_label": "No No Nanette",
                    "id": "112697"
                },
                {
                    "display_label": "Dra-Dra",
                    "id": "112705"
                },
                {
                    "display_label": "Kammerkoncert",
                    "id": "150340"
                },
                {
                    "display_label": "Rollespil",
                    "id": "118301"
                },
                {
                    "display_label": "Büggles flyver vestpå",
                    "id": "112711"
                },
                {
                    "display_label": "Alice i underverdenen",
                    "id": "112712"
                },
                {
                    "display_label": "Skorpionen",
                    "id": "112706"
                },
                {
                    "display_label": "Tosca",
                    "id": "118575"
                },
                {
                    "display_label": "Hjemkomsten",
                    "id": "112698"
                },
                {
                    "display_label": "Askepot",
                    "id": "112710"
                },
                {
                    "display_label": "Agnes",
                    "id": "112699"
                },
                {
                    "display_label": "Til Damsakus",
                    "id": "112842"
                },
                {
                    "display_label": "Hr. Puntila og hans tjener Matti",
                    "id": "112700"
                },
                {
                    "display_label": "Frelst",
                    "id": "112707"
                },
                {
                    "display_label": "Victor",
                    "id": "112701"
                },
                {
                    "display_label": "Bare jeg var som de andre",
                    "id": "112713"
                },
                {
                    "display_label": "Tyrken i Italien",
                    "id": "118574"
                },
                {
                    "display_label": "Serbskij-Instituttet",
                    "id": "112708"
                },
                {
                    "display_label": "Postbudet fra Arles",
                    "id": "112702"
                },
                {
                    "display_label": "Tordenshow",
                    "id": "112841"
                },
                {
                    "display_label": "Hvem er bange for Virginia Woolf?",
                    "id": "112703"
                },
                {
                    "display_label": "Den gyldne By",
                    "id": "112704"
                },
                {
                    "display_label": "Lysistrate eller Kvindernes oprør",
                    "id": "112709"
                }
                ]
            },
            {
                "display_label": "Sæson 1974-75",
                "children": [
                {
                    "display_label": "En stormfuld nat",
                    "id": "112834"
                },
                {
                    "display_label": "Platonov",
                    "id": "112835"
                },
                {
                    "display_label": "Goddag og farvel",
                    "id": "112843"
                },
                {
                    "display_label": "Den kære familie",
                    "id": "112844"
                },
                {
                    "display_label": "Støvler og Sko",
                    "id": "112845"
                },
                {
                    "display_label": "Salome",
                    "id": "112846"
                },
                {
                    "display_label": "Dødsdansen",
                    "id": "112847"
                },
                {
                    "display_label": "Svantes viser",
                    "id": "150341"
                },
                {
                    "display_label": "Røde Mors Rock Teater",
                    "id": "150342"
                },
                {
                    "display_label": "Trille Koncert",
                    "id": "150344"
                },
                {
                    "display_label": "Shit & Chanel",
                    "id": "150226"
                },
                {
                    "display_label": "Cornelis Wreeswijk Koncert",
                    "id": "150345"
                },
                {
                    "display_label": "Daisy koncert",
                    "id": "150346"
                },
                {
                    "display_label": "Østjydsk Musikforsyning",
                    "id": "150347"
                },
                {
                    "display_label": "Felix Luna, Trio, Dreamland",
                    "id": "118545"
                },
                {
                    "display_label": "Lille mand - hvad nu?",
                    "id": "111566"
                },
                {
                    "display_label": "Panik før lukketid",
                    "id": "111680"
                },
                {
                    "display_label": "Hva´så?",
                    "id": "111572"
                },
                {
                    "display_label": "Film Crew",
                    "id": "112848"
                },
                {
                    "display_label": "Må jeg være med",
                    "id": "112716"
                },
                {
                    "display_label": "Gun Man",
                    "id": "113004"
                },
                {
                    "display_label": "Tvillingene",
                    "id": "111567"
                },
                {
                    "display_label": "Forestillingen om kærlighed",
                    "id": "111681"
                },
                {
                    "display_label": "Hoffmanns eventyr",
                    "id": "118544"
                },
                {
                    "display_label": "Genboerne",
                    "id": "118117"
                },
                {
                    "display_label": "Klods Hans",
                    "id": "118118"
                },
                {
                    "display_label": "Tre søstre",
                    "id": "111568"
                },
                {
                    "display_label": "Dødens Triumf",
                    "id": "111682"
                },
                {
                    "display_label": "Wienerblod",
                    "id": "118543"
                },
                {
                    "display_label": "Det er da bare mærk'ligt det ka' ta' så hårdt på én",
                    "id": "112717"
                },
                {
                    "display_label": "Kærlighedsaffæren",
                    "id": "111569"
                },
                {
                    "display_label": "Jaques Brel lever, har det godt og bor i Paris",
                    "id": "112715"
                },
                {
                    "display_label": "Lear",
                    "id": "111570"
                },
                {
                    "display_label": "Can-Can",
                    "id": "111571"
                },
                {
                    "display_label": "De fortabte spillemænd",
                    "id": "111683"
                },
                {
                    "display_label": "Shakespeare og kærligheden",
                    "id": "112714"
                }
                ]
            },
            {
                "display_label": "Sæson 1975-76",
                "children": [
                {
                    "display_label": "Mellem himmel og jord",
                    "id": "112784"
                },
                {
                    "display_label": "Sku' det nu også være et problem?",
                    "id": "112811"
                },
                {
                    "display_label": "De fire årstider, Livjægerne på Amager",
                    "id": "118383"
                },
                {
                    "display_label": "\"I\""
                },
                {
                    "display_label": "The Reindeer Werker",
                    "id": "118500"
                },
                {
                    "display_label": "Lumiere & Son",
                    "id": "118501"
                },
                {
                    "display_label": "Pige-cabaret",
                    "id": "118502"
                },
                {
                    "display_label": "Festuge cabaret",
                    "id": "118504"
                },
                {
                    "display_label": "Preben Neergaard",
                    "id": "118505"
                },
                {
                    "display_label": "Sonja Kehler",
                    "id": "118506"
                },
                {
                    "display_label": "Rose",
                    "id": "111573"
                },
                {
                    "display_label": "Militært Område",
                    "id": "111579"
                },
                {
                    "display_label": "Alligevel",
                    "id": "112904"
                },
                {
                    "display_label": "Ingeborg Brams",
                    "id": "118503"
                },
                {
                    "display_label": "Godspell",
                    "id": "111585"
                },
                {
                    "display_label": "Tartuffe",
                    "id": "118122"
                },
                {
                    "display_label": "Til kamp mod dødbideriet",
                    "id": "111580"
                },
                {
                    "display_label": "En midsommernatsdrøm",
                    "id": "111574"
                },
                {
                    "display_label": "Leif Løvebrøl og hans løjerlige oplevelser i Danmark",
                    "id": "111586"
                },
                {
                    "display_label": "Tango",
                    "id": "112832"
                },
                {
                    "display_label": "Boccaccio",
                    "id": "118384"
                },
                {
                    "display_label": "Røg i køkkenet",
                    "id": "111575"
                },
                {
                    "display_label": "Den skaldede sangerinde",
                    "id": "111581"
                },
                {
                    "display_label": "Jacques eller underkastelsen",
                    "id": "111582"
                },
                {
                    "display_label": "Hakon Jarl",
                    "id": "111576"
                },
                {
                    "display_label": "Ballet-koncert",
                    "id": "112878"
                },
                {
                    "display_label": "Skillingsoperaen",
                    "id": "111584"
                },
                {
                    "display_label": "Det 7. bud: Stjæl lidt mindre",
                    "id": "111577"
                },
                {
                    "display_label": "Hugo på Bjerget",
                    "id": "111583"
                },
                {
                    "display_label": "Cabaret",
                    "id": "111578"
                }
                ]
            },
            {
                "display_label": "Sæson 1976-77",
                "children": [
                {
                    "display_label": "Morten, Mormor og den flinke hr. Jørgensen",
                    "id": "112781"
                },
                {
                    "display_label": "Nola Rae, London Mime Theatre",
                    "id": "112790"
                },
                {
                    "display_label": "Samme tid næste år",
                    "id": "112813"
                },
                {
                    "display_label": "Vil du ha' et kompleks",
                    "id": "112822"
                },
                {
                    "display_label": "Nederlands Dans Theater",
                    "id": "118310"
                },
                {
                    "display_label": "Proximities, Enetime, Hoopla",
                    "id": "118440"
                },
                {
                    "display_label": "Balladen med Jens og Miranda",
                    "id": "118444"
                },
                {
                    "display_label": "John Bull Puncture Repair Kit",
                    "id": "118445"
                },
                {
                    "display_label": "Ven og fjende",
                    "id": "118498"
                },
                {
                    "display_label": "Chicago",
                    "id": "111587"
                },
                {
                    "display_label": "Den politiske glaspuster",
                    "id": "111593"
                },
                {
                    "display_label": "Arkitekten og Kejseren af Assyrien",
                    "id": "111597"
                },
                {
                    "display_label": "Ingeborg Brams",
                    "id": "112800"
                },
                {
                    "display_label": "Købmanden",
                    "id": "111588"
                },
                {
                    "display_label": "La Traviata",
                    "id": "118443"
                },
                {
                    "display_label": "Tribadernes nat",
                    "id": "111594"
                },
                {
                    "display_label": "Pippi Langstrømpe",
                    "id": "111598"
                },
                {
                    "display_label": "Snedronningen",
                    "id": "111589"
                },
                {
                    "display_label": "Den kaukasiske kridtcirkel",
                    "id": "111590"
                },
                {
                    "display_label": "Det voksende slot",
                    "id": "112736"
                },
                {
                    "display_label": "Den skønne Helene",
                    "id": "118442"
                },
                {
                    "display_label": "I Danmark har jeg rod - Et spil om Hansestæderne",
                    "id": "111595"
                },
                {
                    "display_label": "Balkonen",
                    "id": "111591"
                },
                {
                    "display_label": "Wheel of Fire",
                    "id": "112870"
                },
                {
                    "display_label": "Struensee var her",
                    "id": "111596"
                },
                {
                    "display_label": "Jacob von Thyboe",
                    "id": "111592"
                },
                {
                    "display_label": "Bellman, Blomsten, Baby og Bruden",
                    "id": "112725"
                }
                ]
            },
            {
                "display_label": "Sæson 1977-78",
                "children": [
                {
                    "display_label": "Eva´s lange rejse",
                    "id": "111610"
                },
                {
                    "display_label": "Hr. Diller-Daller deler ud",
                    "id": "111611"
                },
                {
                    "display_label": "Lady Bird",
                    "id": "112789"
                },
                {
                    "display_label": "Skærmydsler",
                    "id": "112809"
                },
                {
                    "display_label": "Gengangere",
                    "id": "118438"
                },
                {
                    "display_label": "Glasmenageriet",
                    "id": "118439"
                },
                {
                    "display_label": "Mark Twain i udlandet",
                    "id": "118441"
                },
                {
                    "display_label": "Pippin",
                    "id": "111599"
                },
                {
                    "display_label": "Den guddommelige hverdag",
                    "id": "111604"
                },
                {
                    "display_label": "Folk og røvere i Kardemommeby",
                    "id": "111608"
                },
                {
                    "display_label": "Balletaften - Peter Martins & Suzanne Farell",
                    "id": "112875"
                },
                {
                    "display_label": "Peer Gynt",
                    "id": "111600"
                },
                {
                    "display_label": "Nettet",
                    "id": "111612"
                },
                {
                    "display_label": "Komedie i Grænselandet",
                    "id": "111605"
                },
                {
                    "display_label": "Bolshoi Balletten",
                    "id": "112868"
                },
                {
                    "display_label": "Felix Blaska Balletten",
                    "id": "112877"
                },
                {
                    "display_label": "Høfeber",
                    "id": "111601"
                },
                {
                    "display_label": "Hundene i Casablanca",
                    "id": "111606"
                },
                {
                    "display_label": "Nederlaget",
                    "id": "111602"
                },
                {
                    "display_label": "Cullberg Balletten",
                    "id": "112876"
                },
                {
                    "display_label": "Den poetiske raptus",
                    "id": "111603"
                },
                {
                    "display_label": "Jøsses piger - befrielsen er nær",
                    "id": "111607"
                },
                {
                    "display_label": "Åh, sikke'n herlig krig",
                    "id": "112761"
                },
                {
                    "display_label": "Der er en rock i min suppe",
                    "id": "111609"
                }
                ]
            },
            {
                "display_label": "Sæson 1978-79",
                "children": [
                {
                    "display_label": "Den stærkeste 2",
                    "id": "112733"
                },
                {
                    "display_label": "Hold på dit nu, min sjæl",
                    "id": "112754"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "112771"
                },
                {
                    "display_label": "Jeg gjorde det ikke med vilje, jeg ku' bare ikke la' være",
                    "id": "112772"
                },
                {
                    "display_label": "Night Fall",
                    "id": "112903"
                },
                {
                    "display_label": "Hesitate and demonstrate",
                    "id": "118346"
                },
                {
                    "display_label": "The Ruined Maid",
                    "id": "118347"
                },
                {
                    "display_label": "Strawberry Fields",
                    "id": "111616"
                },
                {
                    "display_label": "Frieriet",
                    "id": "111621"
                },
                {
                    "display_label": "Guys and Dolls",
                    "id": "111685"
                },
                {
                    "display_label": "Fyrtøjet",
                    "id": "111620"
                },
                {
                    "display_label": "Henrik den Fjerde",
                    "id": "111686"
                },
                {
                    "display_label": "Den stærkeste 1",
                    "id": "111617"
                },
                {
                    "display_label": "Mellem venner",
                    "id": "112902"
                },
                {
                    "display_label": "På kant med sengen",
                    "id": "111687"
                },
                {
                    "display_label": "Ballet-koncert",
                    "id": "112867"
                },
                {
                    "display_label": "Malenes drømme",
                    "id": "111618"
                },
                {
                    "display_label": "Miraklet i Kødbyen",
                    "id": "111613"
                },
                {
                    "display_label": "Sommergæster",
                    "id": "111614"
                },
                {
                    "display_label": "Rummene",
                    "id": "111619"
                },
                {
                    "display_label": "Rævestreger",
                    "id": "111615"
                },
                {
                    "display_label": "Den levende vare: Frøken Julie, Anjuta, Den levende vare, Zina",
                    "id": "112816"
                }
                ]
            },
            {
                "display_label": "Sæson 1979-80",
                "children": [
                {
                    "display_label": "Alvin Ailey American Dance Theater",
                    "id": "112863"
                },
                {
                    "display_label": "IOU",
                    "id": "118595"
                },
                {
                    "display_label": "Babettes Gæstebud",
                    "id": "155500"
                },
                {
                    "display_label": "Niels Matthiasens Mindedag",
                    "id": "155523"
                },
                {
                    "display_label": "En gal mands dagbog",
                    "id": "118597"
                },
                {
                    "display_label": "Cunning Stunts",
                    "id": "118598"
                },
                {
                    "display_label": "West Side Story",
                    "id": "111622"
                },
                {
                    "display_label": "I Staunings slagskygge",
                    "id": "111628"
                },
                {
                    "display_label": "Valborg og bænken",
                    "id": "111632"
                },
                {
                    "display_label": "New York City Ballet",
                    "id": "112865"
                },
                {
                    "display_label": "Karlsson på taget",
                    "id": "111633"
                },
                {
                    "display_label": "Amleth",
                    "id": "111623"
                },
                {
                    "display_label": "Vi betaler ikke, vi betaler ikke...",
                    "id": "111629"
                },
                {
                    "display_label": "Mågen",
                    "id": "111624"
                },
                {
                    "display_label": "Du kan ikke ta´ det med dig",
                    "id": "111625"
                },
                {
                    "display_label": "Den pantsatte bondedreng",
                    "id": "111630"
                },
                {
                    "display_label": "Kære løgner",
                    "id": "112901"
                },
                {
                    "display_label": "Matthiasen Matiné",
                    "id": "112871"
                },
                {
                    "display_label": "Alfa og Omega",
                    "id": "111626"
                },
                {
                    "display_label": "Historien om en soldat",
                    "id": "118596"
                },
                {
                    "display_label": "Stodderne",
                    "id": "111631"
                },
                {
                    "display_label": "An der schönen blauen Donau",
                    "id": "111627"
                }
                ]
            },
            {
                "display_label": "Sæson 1980-81",
                "children": [
                {
                    "display_label": "Min ven Tjekhov",
                    "id": "112783"
                },
                {
                    "display_label": "Den kongelige Ballet: Septet Extra, Gærdesanger, Sange uden ord",
                    "id": "118599"
                },
                {
                    "display_label": "Sweet Charity",
                    "id": "111634"
                },
                {
                    "display_label": "Livet er en drøm",
                    "id": "111640"
                },
                {
                    "display_label": "Den besejrede fordom",
                    "id": "111684"
                },
                {
                    "display_label": "Samfundets Støtter",
                    "id": "111635"
                },
                {
                    "display_label": "Dr. Dyregod i Afrika",
                    "id": "111646"
                },
                {
                    "display_label": "Knald eller fald",
                    "id": "111636"
                },
                {
                    "display_label": "Kolde fødder",
                    "id": "111644"
                },
                {
                    "display_label": "En kernesund piges død",
                    "id": "111641"
                },
                {
                    "display_label": "Romulus den Store",
                    "id": "111637"
                },
                {
                    "display_label": "Livet i Danmark",
                    "id": "111638"
                },
                {
                    "display_label": "Giraffen fra New Orleans",
                    "id": "111642"
                },
                {
                    "display_label": "Tør vi elske",
                    "id": "118600"
                },
                {
                    "display_label": "Svejk i Anden Verdenskrig",
                    "id": "111639"
                },
                {
                    "display_label": "Judith",
                    "id": "111643"
                },
                {
                    "display_label": "Fru Mimi",
                    "id": "111645"
                }
                ]
            },
            {
                "display_label": "Sæson 1981-82",
                "children": [
                {
                    "display_label": "Den kongelige Ballet: Five Tangos, Memoria, Vier letzte Lieder",
                    "id": "118602"
                },
                {
                    "display_label": "Annie Get Your Gun",
                    "id": "111647"
                },
                {
                    "display_label": "Rasmus og Jone",
                    "id": "111656"
                },
                {
                    "display_label": "Nancy Spanier Dance Theatre",
                    "id": "112864"
                },
                {
                    "display_label": "Mens vi venter på Godot",
                    "id": "111652"
                },
                {
                    "display_label": "Don Juan",
                    "id": "111648"
                },
                {
                    "display_label": "Dødsdansen",
                    "id": "111653"
                },
                {
                    "display_label": "Recensenten og Dyret",
                    "id": "111655"
                },
                {
                    "display_label": "Tre gange 60'erne: Brian Friel: De elskende, Keinard Melfi: Fuglevinger, LeRoi Jones: I undergrunden",
                    "id": "118603"
                },
                {
                    "display_label": "Gidslet",
                    "id": "111649"
                },
                {
                    "display_label": "Århus Hjælper Polen",
                    "id": "118601"
                },
                {
                    "display_label": "Heksejagt",
                    "id": "111650"
                },
                {
                    "display_label": "Hot'l Baltimore",
                    "id": "112752"
                },
                {
                    "display_label": "Når enden er god...",
                    "id": "111651"
                },
                {
                    "display_label": "Kannibalerne",
                    "id": "111654"
                }
                ]
            },
            {
                "display_label": "Sæson 1982-83",
                "children": [
                {
                    "display_label": "Escorial",
                    "id": "112851"
                },
                {
                    "display_label": "Om krig og kærlighed",
                    "id": "112852"
                },
                {
                    "display_label": "Jeg elsker min kone",
                    "id": "118526"
                },
                {
                    "display_label": "Succes, hvordan... sådan!",
                    "id": "111657"
                },
                {
                    "display_label": "Fortryl mig nu",
                    "id": "111664"
                },
                {
                    "display_label": "Rita",
                    "id": "111665"
                },
                {
                    "display_label": "Roserne bryder ud",
                    "id": "111663"
                },
                {
                    "display_label": "Our Marie",
                    "id": "112850"
                },
                {
                    "display_label": "Fælden",
                    "id": "111667"
                },
                {
                    "display_label": "Ifigenia i Aulis / På Tauris",
                    "id": "111658"
                },
                {
                    "display_label": "Victor",
                    "id": "118525"
                },
                {
                    "display_label": "En kærlighedshistorie",
                    "id": "111666"
                },
                {
                    "display_label": "Bagtalelsens Skole",
                    "id": "111659"
                },
                {
                    "display_label": "Den brændende by",
                    "id": "111660"
                },
                {
                    "display_label": "Pandoras æske",
                    "id": "111668"
                },
                {
                    "display_label": "Herren går på jagt",
                    "id": "111661"
                },
                {
                    "display_label": "Amerigo",
                    "id": "111669"
                },
                {
                    "display_label": "Kameliadamens kærlighed og død",
                    "id": "111662"
                }
                ]
            },
            {
                "display_label": "Sæson 1983-84",
                "children": [
                {
                    "display_label": "Trold kan tæmmes & Woyzeck",
                    "id": "112849"
                },
                {
                    "display_label": "Dæmonernes Dans",
                    "id": "118527"
                },
                {
                    "display_label": "Drømmerne",
                    "id": "118528"
                },
                {
                    "display_label": "My Fair Lady",
                    "id": "111556"
                },
                {
                    "display_label": "Rocky Horror Show",
                    "id": "111673"
                },
                {
                    "display_label": "We who were the Beautiful",
                    "id": "112818"
                },
                {
                    "display_label": "På Skanderborg Station",
                    "id": "111678"
                },
                {
                    "display_label": "Olaf Ussing",
                    "id": "118479"
                },
                {
                    "display_label": "En fugl flyver hvid",
                    "id": "118530"
                },
                {
                    "display_label": "Mutter Courage",
                    "id": "111557"
                },
                {
                    "display_label": "Wien, Wien, nur du allein",
                    "id": "112862"
                },
                {
                    "display_label": "En frygtelig lykke",
                    "id": "111675"
                },
                {
                    "display_label": "Larm i kulissen",
                    "id": "111670"
                },
                {
                    "display_label": "Baal",
                    "id": "112853"
                },
                {
                    "display_label": "Top Girls",
                    "id": "111674"
                },
                {
                    "display_label": "En mand er en mand",
                    "id": "111679"
                },
                {
                    "display_label": "Det´ en skam hun er en mær",
                    "id": "111671"
                },
                {
                    "display_label": "En plads i paradiset",
                    "id": "118529"
                },
                {
                    "display_label": "Børnene derpå",
                    "id": "111676"
                },
                {
                    "display_label": "Messingmusik og galgenlir",
                    "id": "112900"
                },
                {
                    "display_label": "Revisoren",
                    "id": "111672"
                },
                {
                    "display_label": "Fra Bournonville til Pepita",
                    "id": "118484"
                },
                {
                    "display_label": "Et landsted mellem friske grene",
                    "id": "112899"
                },
                {
                    "display_label": "Svejk i Tredje Verdenskrig",
                    "id": "111677"
                },
                {
                    "display_label": "A Wonderful Night",
                    "id": "112854"
                }
                ]
            },
            {
                "display_label": "Sæson 1984-85",
                "children": [
                {
                    "display_label": "Hvem dræbte Lolita",
                    "id": "112898"
                },
                {
                    "display_label": "Kai Norman Andersen Cabaret",
                    "id": "118477"
                },
                {
                    "display_label": "Woyzeck",
                    "id": "118478"
                },
                {
                    "display_label": "Ulysses",
                    "id": "118480"
                },
                {
                    "display_label": "Trold kan tæmmes",
                    "id": "118481"
                },
                {
                    "display_label": "Li'som os",
                    "id": "118482"
                },
                {
                    "display_label": "La Luna",
                    "id": "118483"
                },
                {
                    "display_label": "Damernes Joey",
                    "id": "111544"
                },
                {
                    "display_label": "Den flyvende Holberg",
                    "id": "111555"
                },
                {
                    "display_label": "Godspell",
                    "id": "111549"
                },
                {
                    "display_label": "Jacques og hans herre",
                    "id": "111551"
                },
                {
                    "display_label": "Djævelen og den gode Gud",
                    "id": "111545"
                },
                {
                    "display_label": "Hypokonderne",
                    "id": "118116"
                },
                {
                    "display_label": "Maskerade",
                    "id": "111546"
                },
                {
                    "display_label": "Veje og udveje",
                    "id": "112879"
                },
                {
                    "display_label": "Glade dage",
                    "id": "111552"
                },
                {
                    "display_label": "Dr. Strangula",
                    "id": "111550"
                },
                {
                    "display_label": "Kong Lear",
                    "id": "111547"
                },
                {
                    "display_label": "Trommer i natten",
                    "id": "111554"
                },
                {
                    "display_label": "Columbus",
                    "id": "111548"
                },
                {
                    "display_label": "Her er London",
                    "id": "111553"
                }
                ]
            },
            {
                "display_label": "Sæson 1985-86",
                "children": [
                {
                    "display_label": "Bestialité erotique",
                    "id": "112723"
                },
                {
                    "display_label": "Kvalte suk og sære fagter",
                    "id": "112776"
                },
                {
                    "display_label": "A Chorus Line",
                    "id": "111532"
                },
                {
                    "display_label": "Paladsrevolution",
                    "id": "111537"
                },
                {
                    "display_label": "Ridder Vennelyst vender hjem",
                    "id": "111541"
                },
                {
                    "display_label": "Skillingsoperaen",
                    "id": "112897"
                },
                {
                    "display_label": "Caroline",
                    "id": "111539"
                },
                {
                    "display_label": "Nøddebo Præstegård",
                    "id": "111533"
                },
                {
                    "display_label": "Nancy Spanier Dance Theatre",
                    "id": "112866"
                },
                {
                    "display_label": "Marathondansen",
                    "id": "111538"
                },
                {
                    "display_label": "De Unges Forbund",
                    "id": "111534"
                },
                {
                    "display_label": "Frk. Marguerite",
                    "id": "111543"
                },
                {
                    "display_label": "Vild honning",
                    "id": "111535"
                },
                {
                    "display_label": "Berninis Børn",
                    "id": "111540"
                },
                {
                    "display_label": "Det sidste suk",
                    "id": "111542"
                },
                {
                    "display_label": "Den gale fra Chaillot",
                    "id": "111536"
                }
                ]
            },
            {
                "display_label": "Sæson 1986-87",
                "children": [
                {
                    "display_label": "Kiss me Kate",
                    "id": "111491"
                },
                {
                    "display_label": "Spøgelsessonaten",
                    "id": "111495"
                },
                {
                    "display_label": "Helligtrekongersaften eller Hvad I vil",
                    "id": "155559"
                },
                {
                    "display_label": "Store Ida og Lille Ida",
                    "id": "111500"
                },
                {
                    "display_label": "Giro 413",
                    "id": "112942"
                },
                {
                    "display_label": "I drømmenes spejl",
                    "id": "112765"
                },
                {
                    "display_label": "Krigsspil, 1. og 2. del Rød Sort og Uvidende/Dåsefolket",
                    "id": "111497"
                },
                {
                    "display_label": "Et Juleeventyr",
                    "id": "111492"
                },
                {
                    "display_label": "Krigsspil, 3. del Store Fred",
                    "id": "111498"
                },
                {
                    "display_label": "Nøgne masker",
                    "id": "111493"
                },
                {
                    "display_label": "Dagdrømmerbanden",
                    "id": "111496"
                },
                {
                    "display_label": "Bestialité erotique",
                    "id": "112836"
                },
                {
                    "display_label": "Røde næser",
                    "id": "111494"
                },
                {
                    "display_label": "Farlige forbindelser",
                    "id": "111499"
                },
                {
                    "display_label": "Il Campiello",
                    "id": "111501"
                }
                ]
            },
            {
                "display_label": "Sæson 1987-88",
                "children": [
                {
                    "display_label": "Nattens frelse",
                    "id": "111488"
                },
                {
                    "display_label": "La cage aux folles",
                    "id": "111483"
                },
                {
                    "display_label": "Det er ganske vist",
                    "id": "111490"
                },
                {
                    "display_label": "Det græske projekt",
                    "id": "111486"
                },
                {
                    "display_label": "True West",
                    "id": "112826"
                },
                {
                    "display_label": "La serva padrona",
                    "id": "112940"
                },
                {
                    "display_label": "Udsmiderne",
                    "id": "112895"
                },
                {
                    "display_label": "Et Juleeventyr",
                    "id": "111484"
                },
                {
                    "display_label": "Peters Jul",
                    "id": "112941"
                },
                {
                    "display_label": "No Future",
                    "id": "111487"
                },
                {
                    "display_label": "Lykke Per I",
                    "id": "111485"
                },
                {
                    "display_label": "Lykke Per II",
                    "id": "112454"
                },
                {
                    "display_label": "Beskytteren",
                    "id": "111489"
                }
                ]
            },
            {
                "display_label": "Sæson 1988-89",
                "children": [
                {
                    "display_label": "Thors brudefærd",
                    "id": "111508"
                },
                {
                    "display_label": "Er din kærlighed alt",
                    "id": "112742"
                },
                {
                    "display_label": "Hearbreak Hotel",
                    "id": "112893"
                },
                {
                    "display_label": "Den store Magi",
                    "id": "111507"
                },
                {
                    "display_label": "Især om natten",
                    "id": "111510"
                },
                {
                    "display_label": "Scherfig-mosaik: Der er ingen så døv som den, der ikke vil høre",
                    "id": "111513"
                },
                {
                    "display_label": "Mester og Lærling",
                    "id": "111502"
                },
                {
                    "display_label": "Det bli´r i familien",
                    "id": "111503"
                },
                {
                    "display_label": "Fristelse",
                    "id": "111511"
                },
                {
                    "display_label": "Store Klaus og Lille Klaus",
                    "id": "155599"
                },
                {
                    "display_label": "Prinsesse Sutte Mætte",
                    "id": "155600"
                },
                {
                    "display_label": "Indenfor Murene",
                    "id": "111504"
                },
                {
                    "display_label": "Lyset over Skagen",
                    "id": "111505"
                },
                {
                    "display_label": "Matematik eller kærlighed",
                    "id": "111512"
                },
                {
                    "display_label": "West Glamorgan Youth Theatre",
                    "id": "112939"
                },
                {
                    "display_label": "Laser og pjalter",
                    "id": "111506"
                },
                {
                    "display_label": "Da jeg var en lille pige plejede jeg at råbe og skrige",
                    "id": "111509"
                },
                {
                    "display_label": "Walczak",
                    "id": "112819"
                }
                ]
            },
            {
                "display_label": "Sæson 1989-90",
                "children": [
                {
                    "display_label": "Raquetta Bombardina (Sofies hjertebanken)",
                    "id": "111564"
                },
                {
                    "display_label": "Én for alle - alle mod én",
                    "id": "111559"
                },
                {
                    "display_label": "Titus Andronicus",
                    "id": "111562"
                },
                {
                    "display_label": "Hjælp - det er jul",
                    "id": "111560"
                },
                {
                    "display_label": "I min morfars hua",
                    "id": "111565"
                },
                {
                    "display_label": "Stor ståhej for ingenting",
                    "id": "111563"
                },
                {
                    "display_label": "Knud, Krig og Kærlighed",
                    "id": "112778"
                },
                {
                    "display_label": "Parasitterne",
                    "id": "111417"
                },
                {
                    "display_label": "Lige for lige",
                    "id": "111418"
                },
                {
                    "display_label": "En sommerdag",
                    "id": "112744"
                },
                {
                    "display_label": "Vildanden",
                    "id": "111419"
                },
                {
                    "display_label": "Mrs. Klein",
                    "id": "111420"
                },
                {
                    "display_label": "Klokkeren fra Notre Dame",
                    "id": "111421"
                },
                {
                    "display_label": "Laser og pjalter",
                    "id": "111558"
                },
                {
                    "display_label": "Tell me on a Sunday",
                    "id": "111561"
                },
                {
                    "display_label": "Greven af Monte-Cristo",
                    "id": "111422"
                }
                ]
            },
            {
                "display_label": "Sæson 1990-91",
                "children": [
                {
                    "display_label": "Barnet ovenpå",
                    "id": "112726"
                },
                {
                    "display_label": "Kærestebreve",
                    "id": "112855"
                },
                {
                    "display_label": "Og silden sover med hovedet nedad",
                    "id": "112856"
                },
                {
                    "display_label": "Café Mårnsko",
                    "id": "112857"
                },
                {
                    "display_label": "Dracula",
                    "id": "112858"
                },
                {
                    "display_label": "Aarhus Teaters 90 Års Fødselsdag",
                    "id": "155613"
                },
                {
                    "display_label": "Kongen i kassen",
                    "id": "112859"
                },
                {
                    "display_label": "Denn für dieses Leben",
                    "id": "112860"
                },
                {
                    "display_label": "Gæstespil (uidentificerede)",
                    "id": "112861"
                },
                {
                    "display_label": "Stjerner på morgenhimlen",
                    "id": "118467"
                },
                {
                    "display_label": "Showtime",
                    "id": "111423"
                },
                {
                    "display_label": "Hexeri eller blind alarm",
                    "id": "111481"
                },
                {
                    "display_label": "Elverhøj",
                    "id": "111424"
                },
                {
                    "display_label": "Huckleberry Finn",
                    "id": "112935"
                },
                {
                    "display_label": "Hjælp - det er jul",
                    "id": "118106"
                },
                {
                    "display_label": "Døgnvæsener",
                    "id": "111425"
                },
                {
                    "display_label": "Henrik og Pernille",
                    "id": "112934"
                },
                {
                    "display_label": "Gengældelsens veje",
                    "id": "111406"
                },
                {
                    "display_label": "Johnny Frankikso",
                    "id": "111482"
                },
                {
                    "display_label": "Memphis Tennessee",
                    "id": "111407"
                },
                {
                    "display_label": "Hvide nætter",
                    "id": "118559"
                },
                {
                    "display_label": "Maria Stuart i Skotland",
                    "id": "111408"
                },
                {
                    "display_label": "Kronbruden",
                    "id": "111409"
                },
                {
                    "display_label": "Brødrene Løvehjerte",
                    "id": "111410"
                },
                {
                    "display_label": "William Heinesen Mosaik",
                    "id": "111688"
                }
                ]
            },
            {
                "display_label": "Sæson 1991-92",
                "children": [
                {
                    "display_label": "Rygter",
                    "id": "112803"
                },
                {
                    "display_label": "Parfumeret sild",
                    "id": "112892"
                },
                {
                    "display_label": "Teatersport Alt på et bræt",
                    "id": "112944"
                },
                {
                    "display_label": "Cirkus Montebello",
                    "id": "118370"
                },
                {
                    "display_label": "Roberto Zucco",
                    "id": "111411"
                },
                {
                    "display_label": "Nattergalen",
                    "id": "112943"
                },
                {
                    "display_label": "Rock Clock",
                    "id": "112891"
                },
                {
                    "display_label": "Den forbudte planet",
                    "id": "111412"
                },
                {
                    "display_label": "Don Juans sidste dage",
                    "id": "111413"
                },
                {
                    "display_label": "Tiden of værelset"
                },
                {
                    "display_label": "Kys det hele fra mig - en PH-Cabaret",
                    "id": "111405"
                },
                {
                    "display_label": "Sanering",
                    "id": "111414"
                },
                {
                    "display_label": "Hamlet",
                    "id": "111415"
                },
                {
                    "display_label": "Ordet er frit",
                    "id": "111416"
                },
                {
                    "display_label": "Til hvilken side hver anden gang",
                    "id": "112831"
                },
                {
                    "display_label": "Mellem venner",
                    "id": "112890"
                },
                {
                    "display_label": "Kære Frøken Jelena",
                    "id": "111426"
                },
                {
                    "display_label": "Gösta Berlings Saga",
                    "id": "111427"
                }
                ]
            },
            {
                "display_label": "Sæson 1992-93",
                "children": [
                {
                    "display_label": "Et enfoldigt pigebarn",
                    "id": "112741"
                },
                {
                    "display_label": "Den kærlige kikkert",
                    "id": "112748"
                },
                {
                    "display_label": "Oda - satans kvinde",
                    "id": "112801"
                },
                {
                    "display_label": "Skyldig - ikke skyldig",
                    "id": "118335"
                },
                {
                    "display_label": "Richard III",
                    "id": "111434"
                },
                {
                    "display_label": "Den lille heks",
                    "id": "112889"
                },
                {
                    "display_label": "Aspects of love (kærlighed)",
                    "id": "111435"
                },
                {
                    "display_label": "Dans under høstmånen",
                    "id": "111436"
                },
                {
                    "display_label": "Det farlige venskab",
                    "id": "111437"
                },
                {
                    "display_label": "Kys og Kaos",
                    "id": "118333"
                },
                {
                    "display_label": "Skaf mig en tenor",
                    "id": "112812"
                },
                {
                    "display_label": "Den forbudte planet",
                    "id": "112738"
                },
                {
                    "display_label": "Tommelise",
                    "id": "118337"
                },
                {
                    "display_label": "De fortabte spillemænd",
                    "id": "111428"
                },
                {
                    "display_label": "Nattergalen",
                    "id": "118336"
                },
                {
                    "display_label": "Morgen og aften",
                    "id": "111438"
                },
                {
                    "display_label": "Matiné transportable",
                    "id": "118338"
                },
                {
                    "display_label": "Goldberg-variationer",
                    "id": "111439"
                },
                {
                    "display_label": "Gengangere",
                    "id": "111440"
                },
                {
                    "display_label": "Jordisk paradis",
                    "id": "118334"
                },
                {
                    "display_label": "De tre Musketerer",
                    "id": "111441"
                },
                {
                    "display_label": "Weekend med sne",
                    "id": "112817"
                },
                {
                    "display_label": "Vinger",
                    "id": "112821"
                }
                ]
            },
            {
                "display_label": "Sæson 1993-94",
                "children": [
                {
                    "display_label": "ægtemand på deltid",
                    "id": "112815"
                },
                {
                    "display_label": "Hva' så Vivi!",
                    "id": "112839"
                },
                {
                    "display_label": "Jesus Christ Superstar",
                    "id": "111429"
                },
                {
                    "display_label": "Gyldne tider",
                    "id": "111442"
                },
                {
                    "display_label": "Ven søges eller Sandheden og søhesten",
                    "id": "118273"
                },
                {
                    "display_label": "Og giv os skyggerne",
                    "id": "111443"
                },
                {
                    "display_label": "Som du vil ha' det",
                    "id": "118274"
                },
                {
                    "display_label": "One man show: Allan Mortensen",
                    "id": "118272"
                },
                {
                    "display_label": "Vinden i piletræerne",
                    "id": "111444"
                },
                {
                    "display_label": "Brændende kærlighed",
                    "id": "118275"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "111445"
                },
                {
                    "display_label": "Mit levende hjerte",
                    "id": "111446"
                },
                {
                    "display_label": "Gensynets trilogi",
                    "id": "111447"
                },
                {
                    "display_label": "Stormen",
                    "id": "111448"
                },
                {
                    "display_label": "Først bliver man jo født",
                    "id": "111450"
                },
                {
                    "display_label": "Den fine mand",
                    "id": "111449"
                },
                {
                    "display_label": "De forkerte",
                    "id": "111451"
                },
                {
                    "display_label": "Tordenskjold",
                    "id": "112830"
                }
                ]
            },
            {
                "display_label": "Sæson 1994-95",
                "children": [
                {
                    "display_label": "Det makedonske hus",
                    "id": "112732"
                },
                {
                    "display_label": "Hvad fanden er meningen?",
                    "id": "112757"
                },
                {
                    "display_label": "Alpeglød",
                    "id": "111453"
                },
                {
                    "display_label": "Hurra for Blues Brothers",
                    "id": "111430"
                },
                {
                    "display_label": "Syg Ungdom",
                    "id": "111454"
                },
                {
                    "display_label": "Præsidentinderne",
                    "id": "111455"
                },
                {
                    "display_label": "Odysseen",
                    "id": "111433"
                },
                {
                    "display_label": "Øgledage",
                    "id": "112814"
                },
                {
                    "display_label": "Ollywood Sisters",
                    "id": "112838"
                },
                {
                    "display_label": "Glædelig jul",
                    "id": "111431"
                },
                {
                    "display_label": "På rejse med tante Agatha",
                    "id": "118547"
                },
                {
                    "display_label": "Fyrtøjet",
                    "id": "118107"
                },
                {
                    "display_label": "Nørden",
                    "id": "150063"
                },
                {
                    "display_label": "Et dukkebarn",
                    "id": "150065"
                },
                {
                    "display_label": "Sushi",
                    "id": "150064"
                },
                {
                    "display_label": "Engle i Amerika",
                    "id": "111452"
                },
                {
                    "display_label": "Volpone",
                    "id": "111432"
                },
                {
                    "display_label": "Kærlighed på Krim",
                    "id": "111456"
                },
                {
                    "display_label": "Ingenmandsland",
                    "id": "111458"
                },
                {
                    "display_label": "Vi er alle i samme båd",
                    "id": "111463"
                }
                ]
            },
            {
                "display_label": "Sæson 1995-96",
                "children": [
                {
                    "display_label": "Magisk cirkel",
                    "id": "112788"
                },
                {
                    "display_label": "Lipstick Killer",
                    "id": "111465"
                },
                {
                    "display_label": "Spillemand på en tagryg",
                    "id": "111459"
                },
                {
                    "display_label": "Når bare det kommer fra hjertet",
                    "id": "111466"
                },
                {
                    "display_label": "På knæ for livet",
                    "id": "111471"
                },
                {
                    "display_label": "Rocky Horror Show",
                    "id": "111467"
                },
                {
                    "display_label": "Hjælp - staten betaler",
                    "id": "111460"
                },
                {
                    "display_label": "Fyrtøjet",
                    "id": "111461"
                },
                {
                    "display_label": "Et arvestykke",
                    "id": "118359"
                },
                {
                    "display_label": "Helligtrekongersaften",
                    "id": "111462"
                },
                {
                    "display_label": "Det velsignede barn",
                    "id": "111468"
                },
                {
                    "display_label": "Loppen i øret",
                    "id": "111464"
                },
                {
                    "display_label": "Det eftersøgte barn",
                    "id": "111470"
                },
                {
                    "display_label": "Kunst - Eller manden der ikke kunne elske",
                    "id": "111469"
                }
                ]
            },
            {
                "display_label": "Sæson 1996-97",
                "children": [
                {
                    "display_label": "I tilfælde af",
                    "id": "112881"
                },
                {
                    "display_label": "Heaven",
                    "id": "112758"
                },
                {
                    "display_label": "Me and my girl",
                    "id": "111472"
                },
                {
                    "display_label": "Klinikken",
                    "id": "111478"
                },
                {
                    "display_label": "Soyas 100 - eller ærlighed koster mest",
                    "id": "111479"
                },
                {
                    "display_label": "Sammentræf - måske om natten",
                    "id": "111480"
                },
                {
                    "display_label": "Mojo",
                    "id": "111475"
                },
                {
                    "display_label": "Folk og røvere i Kardemommeby",
                    "id": "118108"
                },
                {
                    "display_label": "Den skårede krukke",
                    "id": "111473"
                },
                {
                    "display_label": "Døde komikeres klub",
                    "id": "111477"
                },
                {
                    "display_label": "Teaterkoncert Gasolin´",
                    "id": "111476"
                },
                {
                    "display_label": "At være eller ikke være",
                    "id": "111474"
                },
                {
                    "display_label": "Skylight",
                    "id": "111529"
                },
                {
                    "display_label": "Master Class",
                    "id": "112785"
                },
                {
                    "display_label": "Privatliv i provinsen",
                    "id": "111531"
                },
                {
                    "display_label": "Kærtegn",
                    "id": "111530"
                },
                {
                    "display_label": "Vovet pels",
                    "id": "111528"
                }
                ]
            },
            {
                "display_label": "Sæson 1997-98",
                "children": [
                {
                    "display_label": "Triple Play",
                    "id": "112894"
                },
                {
                    "display_label": "Tonques",
                    "id": "118372"
                },
                {
                    "display_label": "Søster Coma",
                    "id": "111521"
                },
                {
                    "display_label": "Den politiske kandestøber",
                    "id": "111519"
                },
                {
                    "display_label": "Crazy For You",
                    "id": "111514"
                },
                {
                    "display_label": "David og Goliat",
                    "id": "111525"
                },
                {
                    "display_label": "Folk og røvere i Kardemommeby",
                    "id": "111515"
                },
                {
                    "display_label": "Fool for love",
                    "id": "111522"
                },
                {
                    "display_label": "Made in Aarhus",
                    "id": "111520"
                },
                {
                    "display_label": "Le, mens legen er god",
                    "id": "111516"
                },
                {
                    "display_label": "Når lyset bryder frem",
                    "id": "111527"
                },
                {
                    "display_label": "De sorte skove",
                    "id": "111523"
                },
                {
                    "display_label": "En sælgers død",
                    "id": "111517"
                },
                {
                    "display_label": "Livsens ondskab",
                    "id": "111518"
                },
                {
                    "display_label": "Aske til aske - støv til støv",
                    "id": "111526"
                },
                {
                    "display_label": "De sidste fristelser",
                    "id": "111524"
                }
                ]
            },
            {
                "display_label": "Sæson 1998-99",
                "children": [
                {
                    "display_label": "De lystige koner i Windsor",
                    "id": "112448"
                },
                {
                    "display_label": "Fame",
                    "id": "112453"
                },
                {
                    "display_label": "Exklusif",
                    "id": "118371"
                },
                {
                    "display_label": "Hr. Paul",
                    "id": "112874"
                },
                {
                    "display_label": "Les Misérables",
                    "id": "118520"
                },
                {
                    "display_label": "Bakkanterne",
                    "id": "112444"
                },
                {
                    "display_label": "Venteværelset",
                    "id": "112882"
                },
                {
                    "display_label": "Peter Pan",
                    "id": "118224"
                },
                {
                    "display_label": "Paradisets Børn",
                    "id": "112449"
                },
                {
                    "display_label": "Wa' shå-hva?",
                    "id": "112837"
                },
                {
                    "display_label": "Billedmagerne",
                    "id": "112446"
                },
                {
                    "display_label": "En tjener - to herrer",
                    "id": "112447"
                },
                {
                    "display_label": "Det sidste ord er ikke sagt",
                    "id": "112445"
                },
                {
                    "display_label": "Clockwork Orange",
                    "id": "112869"
                },
                {
                    "display_label": "Guder: Fantomsmerter",
                    "id": "112887"
                },
                {
                    "display_label": "Cheek to Cheek",
                    "id": "112718"
                }
                ]
            },
            {
                "display_label": "Sæson 1999-20",
                "children": [
                {
                    "display_label": "Kameliadamen",
                    "id": "112885"
                },
                {
                    "display_label": "Dansetimen",
                    "id": "112896"
                },
                {
                    "display_label": "Ulysses von Ithacia",
                    "id": "112872"
                },
                {
                    "display_label": "Hvor var vi lykkelige",
                    "id": "112883"
                },
                {
                    "display_label": "Emil fra Lønneberg",
                    "id": "112884"
                },
                {
                    "display_label": "Carmen Negra",
                    "id": "112886"
                },
                {
                    "display_label": "Værket",
                    "id": "112910"
                },
                {
                    "display_label": "Jægers Pris",
                    "id": "112888"
                },
                {
                    "display_label": "100 års ensomhed",
                    "id": "112907"
                },
                {
                    "display_label": "Fædra",
                    "id": "112906"
                },
                {
                    "display_label": "Popcorn",
                    "id": "112960"
                },
                {
                    "display_label": "Den blinde maler",
                    "id": "112905"
                },
                {
                    "display_label": "Snart kommer Tiden",
                    "id": "112909"
                },
                {
                    "display_label": "Genboerne",
                    "id": "112908"
                },
                {
                    "display_label": "Han var en mus",
                    "id": "112914"
                },
                {
                    "display_label": "Hard Times",
                    "id": "118625"
                }
                ]
            },
            {
                "display_label": "Sæson 2000-01",
                "children": [
                {
                    "display_label": "Elton Johns briller",
                    "id": "112965"
                },
                {
                    "display_label": "Jubilæumssøndage",
                    "id": "118495"
                },
                {
                    "display_label": "Henrik & Pernille",
                    "id": "112911"
                },
                {
                    "display_label": "Knivskarpe Polaroider",
                    "id": "112913"
                },
                {
                    "display_label": "Piraterne fra Penzance",
                    "id": "112912"
                },
                {
                    "display_label": "Afskåret liv",
                    "id": "112915"
                },
                {
                    "display_label": "Is",
                    "id": "112916"
                },
                {
                    "display_label": "Drømmenes losseplads",
                    "id": "112917"
                },
                {
                    "display_label": "Gensyn i Braunau",
                    "id": "112918"
                },
                {
                    "display_label": "Hvordan man bliver blind",
                    "id": "112919"
                },
                {
                    "display_label": "Smagen af jern",
                    "id": "118558"
                },
                {
                    "display_label": "Suckyula - Vampyrernes herre",
                    "id": "112921"
                },
                {
                    "display_label": "Narnia - Løven, Heksen og Garderobeskabet",
                    "id": "112920"
                },
                {
                    "display_label": "De forviste",
                    "id": "112932"
                },
                {
                    "display_label": "Vennebogen",
                    "id": "112933"
                },
                {
                    "display_label": "Byens Lys eller Det er Sjov at være til",
                    "id": "112922"
                },
                {
                    "display_label": "Den indbildt syge",
                    "id": "112930"
                },
                {
                    "display_label": "Smittefaren",
                    "id": "112927"
                },
                {
                    "display_label": "Vintereventyret",
                    "id": "112928"
                },
                {
                    "display_label": "Ladies' Night",
                    "id": "112925"
                },
                {
                    "display_label": "Tre søstre",
                    "id": "112924"
                },
                {
                    "display_label": "Dansemus",
                    "id": "112926"
                },
                {
                    "display_label": "Ondskaben",
                    "id": "112929"
                }
                ]
            },
            {
                "display_label": "Sæson 2001-02",
                "children": [
                {
                    "display_label": "Anna & tyngdeloven",
                    "id": "112958"
                },
                {
                    "display_label": "Miss Saigon",
                    "id": "112962"
                },
                {
                    "display_label": "Hus & Have",
                    "id": "112961"
                },
                {
                    "display_label": "Til Fædra",
                    "id": "112963"
                },
                {
                    "display_label": "Arsenik og gamle kniplinger",
                    "id": "112964"
                },
                {
                    "display_label": "Soundtracks",
                    "id": "112959"
                },
                        {
                    "display_label": "Absint",
                    "id": "155631"
                },
                {
                    "display_label": "Sleeping Around",
                    "id": "112966"
                },
                {
                    "display_label": "Ronja Røverdatter",
                    "id": "118496"
                },
                {
                    "display_label": "Www.fordihankan.com",
                    "id": "112967"
                },
                {
                    "display_label": "Her er godt at være",
                    "id": "112970"
                },
                {
                    "display_label": "Mordet på Marat",
                    "id": "112969"
                },
                {
                    "display_label": "Liv x 3",
                    "id": "112968"
                },
                {
                    "display_label": "Kvinden fra Dublin",
                    "id": "118358"
                },
                {
                    "display_label": "Det kolde hjerte",
                    "id": "112972"
                },
                {
                    "display_label": "Mig og Bogart",
                    "id": "112971"
                },
                {
                    "display_label": "Natural born orphans",
                    "id": "112973"
                }
                ]
            },
            {
                "display_label": "Sæson 2002-03",
                "children": [
                {
                    "display_label": "Mod til at dræbe",
                    "id": "112989"
                },
                {
                    "display_label": "Pianisten og Bumsen",
                    "id": "112983"
                },
                {
                    "display_label": "Showboat",
                    "id": "112974"
                },
                {
                    "display_label": "Antigone eller Kreons Fald",
                    "id": "112975"
                },
                {
                    "display_label": "Operation Luise og Ferdinand",
                    "id": "112976"
                },
                {
                    "display_label": "She loves you",
                    "id": "118460"
                },
                {
                    "display_label": "Sengekammeraten",
                    "id": "112977"
                },
                {
                    "display_label": "Ronja Røverdatter",
                    "id": "112979"
                },
                {
                    "display_label": "Boblerne i bækken",
                    "id": "112978"
                },
                {
                    "display_label": "At rejse er at leve",
                    "id": "112982"
                },
                {
                    "display_label": "The King",
                    "id": "118149"
                },
                {
                    "display_label": "Emily Dickinson - den smukkeste pige i Amherst",
                    "id": "118150"
                },
                {
                    "display_label": "Anslag mod hendes liv",
                    "id": "112980"
                },
                {
                    "display_label": "Larm i kulissen",
                    "id": "112981"
                },
                {
                    "display_label": "Der er lys og nogen venter",
                    "id": "112990"
                },
                {
                    "display_label": "Verdensteaterdagen",
                    "id": "118403"
                },
                {
                    "display_label": "Hvem er bange for Virginia Woolf?",
                    "id": "112985"
                },
                {
                    "display_label": "King Kongs døtre",
                    "id": "112986"
                },
                {
                    "display_label": "Don Ranudo",
                    "id": "112991"
                },
                {
                    "display_label": "Sød Tøs Lev Vel",
                    "id": "112992"
                },
                {
                    "display_label": "Nattevagten",
                    "id": "118151"
                }
                ]
            },
            {
                "display_label": "Sæson 2003-04",
                "children": [
                {
                    "display_label": "Guys and Dolls",
                    "id": "112993"
                },
                {
                    "display_label": "Macbeth",
                    "id": "112994"
                },
                {
                    "display_label": "Colepepper/Jægergårdsgade",
                    "id": "113009"
                },
                {
                    "display_label": "Træer er der nok af / Stilleben",
                    "id": "113010"
                },
                {
                    "display_label": "Hr. Kolpert",
                    "id": "112999"
                },
                {
                    "display_label": "Limbo/Restaurant d'amour",
                    "id": "113011"
                },
                {
                    "display_label": "Svanesøen",
                    "id": "113006"
                },
                {
                    "display_label": "Korstog",
                    "id": "113003"
                },
                {
                    "display_label": "Peter Pan",
                    "id": "112995"
                },
                {
                    "display_label": "Be-bop-a-lula",
                    "id": "112996"
                },
                {
                    "display_label": "Tornerose",
                    "id": "113007"
                },
                {
                    "display_label": "Det er ganske vist",
                    "id": "118523"
                },
                {
                    "display_label": "Borkman",
                    "id": "113000"
                },
                {
                    "display_label": "På sporet af den tabte tid",
                    "id": "112997"
                },
                {
                    "display_label": "Mine sange er flyvende breve, eller Livet uden for køleskabet",
                    "id": "113002"
                },
                {
                    "display_label": "Store forventninger",
                    "id": "112998"
                },
                {
                    "display_label": "Drøm om efteråret Sa Ka La",
                    "id": "113085"
                },
                {
                    "display_label": "Nøddeknækkeren",
                    "id": "113008"
                }
                ]
            },
            {
                "display_label": "Sæson 2004-05",
                "children": [
                {
                    "display_label": "Männergarten",
                    "id": "113026"
                },
                {
                    "display_label": "Kjeld Petersen Cabaret",
                    "id": "118546"
                },
                {
                    "display_label": "ÅÅÅ",
                    "id": "118551"
                },
                {
                    "display_label": "We are",
                    "id": "118552"
                },
                {
                    "display_label": "Manden fra Estland",
                    "id": "113001"
                },
                {
                    "display_label": "De dødes rige",
                    "id": "113013"
                },
                {
                    "display_label": "Xxx",
                    "id": "118570"
                },
                {
                    "display_label": "Julius Cæsar",
                    "id": "113012"
                },
                {
                    "display_label": "Niels Klims underjordiske rejse",
                    "id": "113014"
                },
                {
                    "display_label": "Kopier",
                    "id": "113020"
                },
                {
                    "display_label": "Faust og reklamekabaretten",
                    "id": "113024"
                },
                {
                    "display_label": "Harun og eventyrhavet",
                    "id": "113015"
                },
                {
                    "display_label": "Angst æder sjæle op",
                    "id": "113018"
                },
                {
                    "display_label": "Trods klingrende frost",
                    "id": "113021"
                },
                {
                    "display_label": "Diana - the Princess",
                    "id": "118339"
                },
                {
                    "display_label": "H. C. Andersen",
                    "id": "118343"
                },
                {
                    "display_label": "Pudemanden",
                    "id": "113023"
                },
                {
                    "display_label": "Visse Hensyn - Gregersen sagaen",
                    "id": "113016"
                },
                {
                    "display_label": "K + M + L + R",
                    "id": "113025"
                },
                {
                    "display_label": "Gullivers rejse",
                    "id": "113022"
                },
                {
                    "display_label": "Fra regnormenes liv",
                    "id": "118340"
                },
                {
                    "display_label": "Cabaret",
                    "id": "113017"
                },
                {
                    "display_label": "Personkreds 3",
                    "id": "113019"
                }
                ]
            },
            {
                "display_label": "Sæson 2005-06",
                "children": [
                {
                    "display_label": "Folkemord - eller min lever er meningsløs",
                    "id": "113042"
                },
                {
                    "display_label": "Shakespeares samlede værker",
                    "id": "113033"
                },
                {
                    "display_label": "Børneteaterfestival - Den grimme ælling",
                    "id": "113034"
                },
                {
                    "display_label": "Børneteaterfestival - Hvad fatter gør",
                    "id": "113035"
                },
                {
                    "display_label": "Børneteaterfestival - I hans sko",
                    "id": "113036"
                },
                {
                    "display_label": "Børneteaterfestival - I digterens skygge",
                    "id": "113037"
                },
                {
                    "display_label": "Børneteaterfestival - Andersens verden",
                    "id": "113038"
                },
                {
                    "display_label": "Mågen",
                    "id": "113027"
                },
                {
                    "display_label": "Stuff happens - hvor der handles",
                    "id": "113028"
                },
                {
                    "display_label": "Charles the Prince",
                    "id": "118468"
                },
                {
                    "display_label": "Manden der ønskede sig en havudsigt",
                    "id": "118464"
                },
                {
                    "display_label": "Det kolde barn",
                    "id": "113029"
                },
                {
                    "display_label": "Theremin",
                    "id": "118469"
                },
                {
                    "display_label": "Verdens ende",
                    "id": "113031"
                },
                {
                    "display_label": "Slumprinsessen og de 7 Smalltime Hustlers",
                    "id": "113030"
                },
                {
                    "display_label": "Elefant og krokodille",
                    "id": "118459"
                },
                {
                    "display_label": "Dögneren - last minute teater",
                    "id": "113032"
                },
                {
                    "display_label": "The King",
                    "id": "118466"
                },
                {
                    "display_label": "Ondskaben",
                    "id": "118463"
                },
                {
                    "display_label": "Når engle skriger",
                    "id": "118426"
                },
                {
                    "display_label": "Kærlighedens sprog",
                    "id": "118465"
                },
                {
                    "display_label": "Melampe",
                    "id": "113041"
                },
                {
                    "display_label": "Faste forhold",
                    "id": "113039"
                },
                {
                    "display_label": "Service selvmord",
                    "id": "113043"
                },
                {
                    "display_label": "Distance opført sammen med På den anden side som I krig og kærlighed",
                    "id": "113044"
                },
                {
                    "display_label": "På den anden side",
                    "id": "113045"
                },
                {
                    "display_label": "En sæk af gode øjeblikke",
                    "id": "113047"
                },
                {
                    "display_label": "Tv2 teaterkoncert: Hele verden fra forstanden",
                    "id": "113040"
                },
                {
                    "display_label": "Flytning",
                    "id": "113046"
                }
                ]
            },
            {
                "display_label": "Sæson 2006-07",
                "children": [
                {
                    "display_label": "Dans!",
                    "id": "113051"
                },
                {
                    "display_label": "En hårfin balance",
                    "id": "113048"
                },
                {
                    "display_label": "Paradis",
                    "id": "118561"
                },
                {
                    "display_label": "Salvador",
                    "id": "118562"
                },
                {
                    "display_label": "Lysbringer",
                    "id": "118560"
                },
                {
                    "display_label": "Alrune",
                    "id": "118564"
                },
                {
                    "display_label": "The Hunter Show",
                    "id": "118313"
                },
                {
                    "display_label": "De siger det skal nok gå",
                    "id": "118563"
                },
                {
                    "display_label": "Hamlet",
                    "id": "118470"
                },
                {
                    "display_label": "Snittet",
                    "id": "113054"
                },
                {
                    "display_label": "Greifswalder Strasse",
                    "id": "113056"
                },
                {
                    "display_label": "Fyrværkerimesterens Datter",
                    "id": "113049"
                },
                {
                    "display_label": "Nick Cave Teaterkoncerten",
                    "id": "113052"
                },
                {
                    "display_label": "Nathan (uden titel)",
                    "id": "113053"
                },
                {
                    "display_label": "Lilleskoven",
                    "id": "113057"
                },
                {
                    "display_label": "Det er lige til",
                    "id": "118311"
                },
                {
                    "display_label": "Rene Linjer",
                    "id": "113050"
                },
                {
                    "display_label": "Tørklædemonologerne",
                    "id": "113055"
                },
                {
                    "display_label": "Midnight Express",
                    "id": "118471"
                },
                {
                    "display_label": "Agurketid og velfærdspølser",
                    "id": "118474"
                },
                {
                    "display_label": "Bunbury",
                    "id": "118473"
                },
                {
                    "display_label": "Hjertets terrorister",
                    "id": "113058"
                },
                {
                    "display_label": "Satisfaction",
                    "id": "118472"
                },
                {
                    "display_label": "Traffucking",
                    "id": "118312"
                }
                ]
            },
            {
                "display_label": "Sæson 2007-08",
                "children": [
                {
                    "display_label": "Satisfaction",
                    "id": "118516"
                },
                {
                    "display_label": "Alle tiders kvinde",
                    "id": "118314"
                },
                {
                    "display_label": "The History Boys",
                    "id": "113059"
                },
                {
                    "display_label": "Energi",
                    "id": "118461"
                },
                {
                    "display_label": "Mit loft under himlen",
                    "id": "118447"
                },
                {
                    "display_label": "Evolution of the robot",
                    "id": "118315"
                },
                {
                    "display_label": "Dorthes hjerte",
                    "id": "118446"
                },
                {
                    "display_label": "Hvordan vi slipper af med de andre",
                    "id": "113060"
                },
                {
                    "display_label": "Forestillingen om Kejserens nye klæder",
                    "id": "113061"
                },
                {
                    "display_label": "Woyzeck",
                    "id": "113062"
                },
                {
                    "display_label": "Sommergæster",
                    "id": "113063"
                },
                {
                    "display_label": "Nøddeknækkeren",
                    "id": "113064"
                },
                {
                    "display_label": "Idioten",
                    "id": "113065"
                },
                {
                    "display_label": "Michael - I'm bad",
                    "id": "118517"
                },
                {
                    "display_label": "Rumlerikkerne",
                    "id": "118405"
                },
                {
                    "display_label": "Realisme",
                    "id": "113066"
                },
                {
                    "display_label": "Gregersen sagaen",
                    "id": "113067"
                },
                {
                    "display_label": "Det lille liv",
                    "id": "113069"
                },
                {
                    "display_label": "Sidste udkald",
                    "id": "113068"
                },
                {
                    "display_label": "Teaterkoncert Beach Boys",
                    "id": "118458"
                },
                {
                    "display_label": "Full Body Treatment",
                    "id": "118515"
                }
                ]
            },
            {
                "display_label": "Sæson 2008-09",
                "children": [
                {
                    "display_label": "Teaterkoncert Beach Boys",
                    "id": "113073"
                },
                {
                    "display_label": "Lulu",
                    "id": "113072"
                },
                {
                    "display_label": "Kosmisk frygt - eller da Brad Pitt fik paranoia",
                    "id": "113074"
                },
                {
                    "display_label": "Marilyn",
                    "id": "118586"
                },
                {
                    "display_label": "Loveplay",
                    "id": "113075"
                },
                {
                    "display_label": "Det gyldne kompas 1",
                    "id": "113076"
                },
                {
                    "display_label": "Nick Cave Teaterkoncerten",
                    "id": "113077"
                },
                {
                    "display_label": "Pietà",
                    "id": "113078"
                },
                {
                    "display_label": "Teaterkoncert Tom Waits",
                    "id": "113079"
                },
                {
                    "display_label": "Slottet",
                    "id": "113080"
                },
                {
                    "display_label": "Don Carlos",
                    "id": "118221"
                },
                {
                    "display_label": "Den eneste anden",
                    "id": "113081"
                },
                {
                    "display_label": "Petra von Kants bitre tårer",
                    "id": "113082"
                },
                {
                    "display_label": "Kødkarrusellen",
                    "id": "113083"
                },
                {
                    "display_label": "Panik",
                    "id": "113084"
                },
                {
                    "display_label": "Maria Magdalena/Wayn Wash III",
                    "id": "118367"
                }
                ]
            },
            {
                "display_label": "Sæson 2009-10",
                "children": [
                {
                    "display_label": "Rester af Alice",
                    "id": "113096"
                },
                {
                    "display_label": "Et grisehjerte",
                    "id": "113097"
                },
                {
                    "display_label": "Sylfiden",
                    "id": "113087"
                },
                {
                    "display_label": "De andres drømme",
                    "id": "118567"
                },
                {
                    "display_label": "Darwins testamente",
                    "id": "113088"
                },
                {
                    "display_label": "Lidt før Søndermarken",
                    "id": "113098"
                },
                {
                    "display_label": "Derude hvor de ikke kan høre os",
                    "id": "113099"
                },
                {
                    "display_label": "Død mands kvinde",
                    "id": "113100"
                },
                {
                    "display_label": "Undskyld gamle, hvor finder jeg tiden, kærligheden og den galskab, der smitter...?"
                },
                {
                    "display_label": "Før/Efter",
                    "id": "113092"
                },
                {
                    "display_label": "Det gyldne kompas 2",
                    "id": "113090"
                },
                {
                    "display_label": "Tommy",
                    "id": "118476"
                },
                {
                    "display_label": "Et Dukkehjem",
                    "id": "113091"
                },
                {
                    "display_label": "Noras sønner",
                    "id": "113101"
                },
                {
                    "display_label": "Mesteren og Margarita",
                    "id": "113102"
                },
                {
                    "display_label": "Kærlighedskarrusellen",
                    "id": "113093"
                },
                {
                    "display_label": "Fremtidens historie",
                    "id": "113094"
                },
                {
                    "display_label": "Fobiskolen",
                    "id": "118566"
                },
                {
                    "display_label": "Teaterkoncert Bob Dylan",
                    "id": "113095"
                }
                ]
            },
            {
                "display_label": "Sæson 2010-11",
                "children": [
                {
                    "display_label": "Teaterkoncert Bob Dylan",
                    "id": "113113"
                },
                {
                    "display_label": "Rødt og grønt",
                    "id": "113105"
                },
                {
                    "display_label": "Antichrist",
                    "id": "113107"
                },
                {
                    "display_label": "Fanny og Alexander",
                    "id": "113103"
                },
                {
                    "display_label": "Romeo og Julie",
                    "id": "113106"
                },
                {
                    "display_label": "Tyve",
                    "id": "113112"
                },
                {
                    "display_label": "Engel",
                    "id": "113108"
                },
                {
                    "display_label": "Pinocchio",
                    "id": "113104"
                },
                {
                    "display_label": "Scener af et ægteskab",
                    "id": "113110"
                },
                {
                    "display_label": "Mens vi venter på Godot",
                    "id": "113109"
                },
                {
                    "display_label": "Teaterkoncert Be kind if I'm a mess",
                    "id": "113114"
                },
                {
                    "display_label": "Sweeney Todd",
                    "id": "113115"
                },
                {
                    "display_label": "Tartuffe",
                    "id": "113111"
                }
                ]
            },
            {
                "display_label": "Sæson 2011-12",
                "children": [
                {
                    "display_label": "Kasimir & Karoline",
                    "id": "113119"
                },
                {
                    "display_label": "Det normale liv",
                    "id": "113120"
                },
                {
                    "display_label": "Hamlet",
                    "id": "113116"
                },
                {
                    "display_label": "Kvinde kend din krop",
                    "id": "118565"
                },
                {
                    "display_label": "Solens børn",
                    "id": "113122"
                },
                {
                    "display_label": "Leonard Cohen Teaterkoncert",
                    "id": "113117"
                },
                {
                    "display_label": "Faces look ugly",
                    "id": "113121"
                },
                {
                    "display_label": "Brødrene Løvehjerte",
                    "id": "113118"
                },
                {
                    "display_label": "De kommer gående",
                    "id": "118319"
                },
                {
                    "display_label": "Name of the next song",
                    "id": "113126"
                },
                {
                    "display_label": "Jeppe på Bjerget",
                    "id": "113124"
                },
                {
                    "display_label": "Hallerne",
                    "id": "113127"
                },
                {
                    "display_label": "Spørg stumtjereren",
                    "id": "118318"
                },
                {
                    "display_label": "Chess",
                    "id": "113123"
                },
                {
                    "display_label": "Gengangere",
                    "id": "113125"
                },
                {
                    "display_label": "Passione",
                    "id": "118316"
                },
                {
                    "display_label": "Jalla:5",
                    "id": "118317"
                }
                ]
            },
            {
                "display_label": "Sæson 2012-13",
                "children": [
                {
                    "display_label": "Chess",
                    "id": "113128"
                },
                {
                    "display_label": "Nekrologer",
                    "id": "113131"
                },
                {
                    "display_label": "Teaterkoncert Mozart",
                    "id": "113130"
                },
                {
                    "display_label": "Other Desert Cities",
                    "id": "113129"
                },
                {
                    "display_label": "Electronic City",
                    "id": "113133"
                },
                {
                    "display_label": "Frankenstein",
                    "id": "113132"
                },
                {
                    "display_label": "Kvartetten",
                    "id": "118408"
                },
                {
                    "display_label": "Snehvide",
                    "id": "113134"
                },
                {
                    "display_label": "Skakten",
                    "id": "113136"
                },
                {
                    "display_label": "Kirsebærhaven",
                    "id": "113135"
                },
                {
                    "display_label": "Uro",
                    "id": "118409"
                },
                {
                    "display_label": "Farlige forbindelser",
                    "id": "113138"
                },
                {
                    "display_label": "La cage aux folles",
                    "id": "113137"
                },
                {
                    "display_label": "The me nobody knows",
                    "id": "118424"
                },
                {
                    "display_label": "Complexe des genres",
                    "id": "118423"
                },
                {
                    "display_label": "Jalla, Jalla 13",
                    "id": "118425"
                }
                ]
            },
            {
                "display_label": "Sæson 2013-14",
                "children": [
                {
                    "display_label": "Osvald",
                    "id": "118361"
                },
                {
                    "display_label": "All my dreams come true",
                    "id": "113139"
                },
                {
                    "display_label": "Winners & Losers",
                    "id": "118420"
                },
                {
                    "display_label": "Den Gerrige",
                    "id": "113140"
                },
                {
                    "display_label": "Kvinde kend din krop",
                    "id": "118421"
                },
                {
                    "display_label": "Den dresserede mand",
                    "id": "118422"
                },
                {
                    "display_label": "Brødrene Løvehjerte",
                    "id": "113141"
                },
                {
                    "display_label": "Ondt blod",
                    "id": "118427"
                },
                {
                    "display_label": "Portrætter",
                    "id": "113142"
                },
                {
                    "display_label": "Dagen før",
                    "id": "113143"
                },
                {
                    "display_label": "Hjertet skælver",
                    "id": "113144"
                },
                {
                    "display_label": "Rosmersholm",
                    "id": "113145"
                },
                {
                    "display_label": "4 ever",
                    "id": "118522"
                },
                {
                    "display_label": "Les Misérables",
                    "id": "113146"
                },
                {
                    "display_label": "Dans under høstmånen",
                    "id": "113147"
                },
                {
                    "display_label": "Borgerscene 1: Inde ved siden af",
                    "id": "118521"
                }
                ]
            },
            {
                "display_label": "Sæson 2014-15",
                "children": [
                {
                    "display_label": "Besøget eller Den gamle dame besøger byen",
                    "id": "113148"
                },
                {
                    "display_label": "Dobbeltkoncert: The Cabin Project & Nils Frahm",
                    "id": "118366"
                },
                {
                    "display_label": "Brun mands byrde",
                    "id": "113153"
                },
                {
                    "display_label": "Dance me to the end on/off love",
                    "id": "118365"
                },
                {
                    "display_label": "Konstellationer",
                    "id": "113157"
                },
                {
                    "display_label": "Karlas kabale",
                    "id": "113149"
                },
                {
                    "display_label": "Andel",
                    "id": "113154"
                },
                {
                    "display_label": "Men lever man",
                    "id": "118593"
                },
                {
                    "display_label": "Processen",
                    "id": "118363"
                },
                {
                    "display_label": "Teaterkoncert Gasolin´",
                    "id": "118594"
                },
                {
                    "display_label": "Jeg forsvinder",
                    "id": "113156"
                },
                {
                    "display_label": "Hedda Gabler",
                    "id": "113150"
                },
                {
                    "display_label": "Ar",
                    "id": "118364"
                },
                {
                    "display_label": "My Fair Lady",
                    "id": "113151"
                },
                {
                    "display_label": "Glasbobler",
                    "id": "113155"
                },
                {
                    "display_label": "On/Off",
                    "id": "113152"
                },
                {
                    "display_label": "Fædre",
                    "id": "113158"
                },
                {
                    "display_label": "The Suit",
                    "id": "118362"
                }
                ]
            },
            {
                "display_label": "Sæson 2015-16",
                "children": [
                {
                    "display_label": "Imagine",
                    "id": "118731"
                },
                {
                    "display_label": "Frk. Julie",
                    "id": "118689"
                },
                {
                    "display_label": "Aftryk",
                    "id": "118726"
                },
                {
                    "display_label": "For enden af kærligheden",
                    "id": "120377"
                },
                {
                    "display_label": "Jeg kan huske alting",
                    "id": "120378"
                },
                {
                    "display_label": "Salon Madam Nielsen",
                    "id": "120376"
                },
                {
                    "display_label": "Bennys Badekar",
                    "id": "120381"
                },
                {
                    "display_label": "The Blazing World",
                    "id": "120382"
                },
                {
                    "display_label": "Lev i fred med deres nerver",
                    "id": "120018"
                },
                {
                    "display_label": "Snedronningen",
                    "id": "120003"
                },
                {
                    "display_label": "På rejse i min krop",
                    "id": "120023"
                },
                {
                    "display_label": "Salamimetoden",
                    "id": "119575"
                },
                {
                    "display_label": "Doppler",
                    "id": "120383"
                },
                {
                    "display_label": "Impossible",
                    "id": "120384"
                },
                {
                    "display_label": "Uropa",
                    "id": "120385"
                },
                {
                    "display_label": "Varmestuen",
                    "id": "120386"
                },
                {
                    "display_label": "Familien der kunne tale om alt",
                    "id": "118784"
                },
                {
                    "display_label": "Til mine brødre",
                    "id": "118786"
                },
                {
                    "display_label": "Sunny Side",
                    "id": "120094"
                },
                {
                    "display_label": "Dig og mig for altid",
                    "id": "120036"
                },
                {
                    "display_label": "Lars Ole 5.C",
                    "id": "120040"
                },
                {
                    "display_label": "Fornuft og følelse",
                    "id": "118788"
                },
                {
                    "display_label": "Det vi ved",
                    "id": "119829"
                },
                {
                    "display_label": "Jalla:13",
                    "id": "120387"
                },
                {
                    "display_label": "Borgerscene Festival",
                    "id": "120389"
                }
                ]
            },
            {
                "display_label": "Sæson 2016-17",
                "children": [
                {
                    "display_label": "American Spirit",
                    "id": "119843"
                },
                {
                    "display_label": "En kvinde uden betydning",
                    "id": "119569"
                },
                {
                    "display_label": "De rene rum",
                    "id": "120095"
                },
                {
                    "display_label": "Living Dead",
                    "id": "120096"
                },
                {
                    "display_label": "H.C. Andersen lever",
                    "id": "120410"
                },
                {
                    "display_label": "HOV",
                    "id": "120411"
                },
                {
                    "display_label": "Min Far",
                    "id": "120412"
                },
                {
                    "display_label": "Kvinde ved 1000 grader",
                    "id": "120413"
                },
                {
                    "display_label": "Sidste diligence fra lykkens by",
                    "id": "120414"
                },
                {
                    "display_label": "Swan Lake",
                    "id": "120415"
                },
                {
                    "display_label": "Fakiren fra Bilbao",
                    "id": "120098"
                },
                {
                    "display_label": "Kaldet",
                    "id": "120099"
                },
                {
                    "display_label": "Aarhus Teater Kor Koncert",
                    "id": "120420"
                },
                {
                    "display_label": "Medea",
                    "id": "120100"
                },
                {
                    "display_label": "En skilsmisse",
                    "id": "120101"
                },
                {
                    "display_label": "Erasmus Montanus",
                    "id": "120102"
                },
                {
                    "display_label": "Habibi",
                    "id": "120422"
                },
                {
                    "display_label": "MORPH",
                    "id": "120423"
                },
                {
                    "display_label": "Jesus Christ Superstar",
                    "id": "120430"
                },
                {
                    "display_label": "Den sidste bølge",
                    "id": "120431"
                },
                {
                    "display_label": "ILT 2017",
                    "id": "120432"
                },
                {
                    "display_label": "PREMIERE",
                    "id": "120433"
                },
                {
                    "display_label": "Freak Out",
                    "id": "120434"
                }
                ]
            },
            {
                "display_label": "Sæson 2017-18",
                "children": [
                {
                    "id": "149860",
                    "display_label": "Lyden af de skuldre vi står på"
                },
                {
                    "id": "149881",
                    "display_label": "Fragt"
                },
                {
                    "id": "149905",
                    "display_label": "#Amlet"
                },
                {
                    "id": "149884",
                    "display_label": "Livet - hvor svært kan det være"
                },
                {
                    "id": "149885",
                    "display_label": "Den gode vilje"
                },
                {
                    "id": "149886",
                    "display_label": "Edda"
                },
                {
                    "id": "149891",
                    "display_label": "Momentet"
                },
                {
                    "id": "149894",
                    "display_label": "Narnia"
                },
                {
                    "id": "149893",
                    "display_label": "Hvad vi taler om når vi taler om kærlighed"
                },
                {
                    "id": "149896",
                    "display_label": "Techno"
                },
                {
                    "id": "149897",
                    "display_label": "Hospitalet"
                },
                {
                    "id": "149899",
                    "display_label": "My heartache brings all the boys to the yard"
                },
                {
                    "id": "149900",
                    "display_label": "West Side Story"
                },
                {
                    "id": "149901",
                    "display_label": "OMG"
                },
                {
                    "id": "149902",
                    "display_label": "Lav sol"
                },
                {
                    "id": "149903",
                    "display_label": "Biedermann og brandstifterne"
                },
                {
                    "id": "149904",
                    "display_label": "Anekdoter - livshistorier fra Møllestien"
                },
                {
                    "id": "149895",
                    "display_label": "The Vampire Revolution"
                },
                {
                    "id": "149889",
                    "display_label": "Komedien hvor alt går galt"
                },
                {
                    "id": "149882",
                    "display_label": "Opvisning i lavt selvværd"
                },
                {
                    "id": "149892",
                    "display_label": "Med sne"
                },
                {
                    "id": "149898",
                    "display_label": "De lystige koner"
                },
                {
                    "id": "149887",
                    "display_label": "Juhu - det er regnvejr"
                },
                {
                    "id": "149888",
                    "display_label": "Barnevognen"
                },
                {
                    "id": "149890",
                    "display_label": "Historisk talkshow med Luther"
                },
                {
                    "id": "149981",
                    "display_label": "Transfervindue"
                }
                ]
            },
            {
                "display_label": "Sæson 2018-19",
                "children": [
                {
                    "display_label": "Friheden",
                    "id": "150474"
                },
                {
                    "display_label": "Revolution",
                    "id": "150478"
                }
                ]
            },
            {
                "display_label": "Sæson 2019-20",
                "children": [
                {
                    "display_label": "Lazarus",
                    "id": "154644"
                },
                {
                    "display_label": "Pagten",
                    "id": "154814"
                },
                {
                    "display_label": "Denungewertherslidelser",
                    "id": "154899"
                },
                {
                    "display_label": "Lyden af de skuldre vi står på",
                    "id": "154907"
                },
                {
                    "display_label": "Ordet",
                    "id": "154912"
                },
                {
                    "display_label": "Se dagens lys",
                    "id": "154654"
                }
                ]
            },
            {
                "display_label": "Sæson 2020-21",
                "children": [
                {
                    "display_label": "Et Juleeventyr",
                    "id": "155534"
                },
                {
                    "display_label": "Kærlighedens forrykte former",
                    "id": "155544"
                },
                {
                    "display_label": "Vita Danica",
                    "id": "155591"
                },
                {
                    "display_label": "Kong Lear",
                    "id": "155642"
                },
                {
                    "display_label": "Leonora Christina – sandhedens dronning",
                    "id": "155791"
                },
                {
                    "display_label": "YCLWB",
                    "id": "155819"
                },
                {
                    "display_label": "The Supreme Gentleman",
                    "id": "155820"
                },
                {
                    "display_label": "Charlie og chokoladefabrikken",
                    "id": "155859"
                }
                ]
            },
            {
                "display_label": "Sæson 2021-22",
                "children": [
                {
                    "display_label": "Girls & Boys",
                    "id": "155924"
                },
                {
                    "display_label": "Sandmanden",
                    "id": "156141"
                },
                {
                    "display_label": "Jeg er jo lige her",
                    "id": "156144"
                },
                {
                    "display_label": "Kagefabrikken",
                    "id": "156193"
                },
                {
                    "display_label": "Alice i Eventyrland",
                    "id": "156200"
                },
                {
                    "display_label": "Til de lyse morgener",
                    "id": "156209"
                },
                {
                    "display_label": "Romeo og Julie",
                    "id": "156211"
                },
                {
                    "display_label": "The Supreme Gentleman",
                    "id": "156221"
                }
                ]
            }
        ]
    }
]

TEMPLATE_GLOBALS = {
    "translate": {
        "identification": "Identifikation",
        "identifier": "Arkivalie ID",
        "ingest_id": "Indkomst ID",
        "related_content": "Relateret arkivalie",
        "curators": "Kuratorer",
        "administration": "Administration",
        "aggrement": "Afleveringsaftale",
        "rightsholders": "Rettighedshavere",
        "copyright_expires": "Copyright udløber (år)",
        "declassification_expires": "Persondata udløber (år)",
        "original_id": "Originalt id",
        "admin_tags": "Administrative tags",
        "admin_notes": "Administrative noter",
        "admin_data": "Administrative data",
        "description": "Beskrivelse",
        "title": "Titel",
        "content_type": "Arkivalietype",
        "collection": "Samling",
        "hierarchical_level": "Arkivserie",
        "series": "Arkivserie",
        "abstract": "Abstrakt",
        "subjects": "Emner",
        "start_date": "Startdato",
        "end_date": "Slutdato",
        "creators": "Skaber",
        "textcontent": "Tekst",
        "collection_tags": "Originale emner",
        "desc_notes": "Noter",
        "desc_data": "Beskrivelsesdata",
        "entities": "Relationer",
        "tags": "Tags",
        "people": "Personer",
        "events": "Forestillinger",
        "licenses": "Brugslicenser",
        "collections": "Samlinger",
        "records": "Arkivalier",
        "people": "Personer",
        "organisations": "Organisationer",
        "events": "Forestillinger",
        "locations": "Steder",
        "digital_content": "Digitalt indhold",
        "checksum": "Checksum",
        "checksum_algorithm": "Checksum-algoritme",
        "last_checksum_date": "Sidste chemsumdato",
        "original_filename": "Originalt filnavn",
        "filename": "Filnavn",
        "mimetype": "Mimetype",
        "digital_size": "Digital størrelse",
        "digital_format": "Digitalt format",
        "filelist": "Indholdsfortegnelse",
        "representations": "Webressourcer",
        "small_size_url": "Frimærke",
        "medium_size_url": "Medium størrelse",
        "large_size_url": "Stor størrelse",
        "download_url": "Link til original fil",
        "analog_content": "Analog indhold",
        "storage_id": "ArkivID/Løbenummer",
        "physical_extent": "Fysisk mængde",
        "storage_room": "Rum",
        "storage_rack": "Reol",
        "storage_unit": "Fag",
        "storage_shelf": "Hylde",
        "physical_condition": "Fysisk tilstand",
        "physical_size": "Fysisk størrelse",
        "physical_format": "Fysisk format",
        "entity_id": "ID",
        "id": "Id",
        "display_name": "Displaynavn",
        "gender": "Køn",
        "place_of_birth": "Fødselssted",
        "date_of_birth": "Fødselsdato",
        "place_of_death": "Dødssted",
        "date_of_death": "Dødsdato",
        "birthname": "Pigenavn (født)",
        "sources": "Kilder",
        "firstnames": "Fornavne",
        "lastnames": "Mellem- og efternavne",
        "portrait": "Portræt",
        "occupation": "Beskæftigelse",
        "industry": "Branche",
        "from_date": "Startdato",
        "to_date": "Slutdato",
        "name": "Navn",
        "named_date": "Navngivt år",
        "zipcode": "Postnummer",
        "longitude": "Breddegrad",
        "latitude": "Længdegrad",
        "rotation": "Rotation",
        "event_type": "Begivenhedstype",
        "notes": "Introduktion",
        "extend": "Omfang",
        "structure": "Struktur",
        "link": "Licenstekst",
    }
}
