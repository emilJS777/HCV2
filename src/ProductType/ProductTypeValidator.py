product_type_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 3, "maxLength": 40},
        "description": {"type": "string", "minLength": 0, "maxLength": 60},
      },
    "required": ["title", "description"]
}
