expense_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "maxLength": 60},
        "description": {"type": "string", "maxLength": 120},
        "price": {"type": "number"},
        "count": {"type": "number"},
        "colleague_id": {"type": "number"},
        "expense_type_id": {"type": "number"},
        "firm_id": {"type": "number"},
      },
    "required": []
}
