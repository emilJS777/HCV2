income_type_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 3, "maxLength": 40},
        "description": {"type": "string", "maxLength": 80},
      },
    "required": ["title"]
}
