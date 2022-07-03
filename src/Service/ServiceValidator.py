service_schema = {
    "type": "object",
    "properties": {
        "code": {"type": "string", "maxLength": 10},
        "title": {"type": "string", "maxLength": 60},
        "check": {"type": "string", "maxLength": 60},
        "wholesale_price": {"type": "number"},
        "retail_price": {"type": "number"},
        "unit_id": {"type": "number"}
      },
    "required": ["code", "title"]
}
