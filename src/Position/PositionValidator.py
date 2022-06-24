position_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 3, "maxLength": 60},
        "description": {"type": "string", "minLength": 3, "maxLength": 120},
      },
    "required": ["title"]
}
