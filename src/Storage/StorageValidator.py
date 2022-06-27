storage_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 3, "maxLength": 40},
        "description": {"type": "string", "minLength": 3, "maxLength": 120},
        "code": {"type": "string", "maxLength": 10},
        "storekeeper": {"type": "string", "minLength": 3, "maxLength": 80},
        "address": {"type": "string", "minLength": 3, "maxLength": 120},
        "firm_id": {"type": "number"},
      },
    "required": ["title", "code", "firm_id"]
}
