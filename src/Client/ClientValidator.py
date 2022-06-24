client_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 3, "maxLength": 60},
        "description": {"type": "string", "minLength": 3, "maxLength": 120},
      },
    "required": ["name", "description"]
}