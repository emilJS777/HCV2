product_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 3, "maxLength": 60},
        "description": {"type": "string", "minLength": 3, "maxLength": 120},
        "product_type_id": {"type": "number"},
        "storage_id": {"type": "number"},
      },
    "required": ["name", "product_type_id", "storage_id"]
}
