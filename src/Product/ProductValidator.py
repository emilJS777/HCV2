product_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 3, "maxLength": 60},
        "description": {"type": "string", "minLength": 3, "maxLength": 120},
        "product_type_id": {"type": "number"},
        "storage_id": {"type": "number"},
        "code": {"type": "string", "minLength": 1, "maxLength": 10},
        "wholesale_price": {"type": "number"},
        "retail_price": {"type": "number"},
        "unit_id": {"type": "number"},
        "count": {"type": "number"}
      },
    "required": ["name", "product_type_id", "storage_id", "wholesale_price", "retail_price", "unit_id", "count"]
}
