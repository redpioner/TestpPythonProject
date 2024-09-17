RESOURSE_DATA_SCHEMA = {
    "type" : "object",
    "properties" : {
        "id" : {"type": "number"},
        "name" : {"type": "string"},
        "year" : {"type": "number"},
        "color" : {"type": "string"},
        "panton_value" : {"type": "string"}
    },
    "required" : ["id", "name", "year", "color", "pantone_value"]
}

RESOURSE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "year": {"type": "number"},
        "color": {"type": "string"},
        "panton_value": {"type": "string"}
    },
    "required": ["id", "name", "year", "color", "pantone_value"]
}