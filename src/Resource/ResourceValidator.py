resource_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 3, "maxLength": 60},
        "hm_type": {"type": "string", "maxLength": 80},
        "hm_group": {"type": "string", "maxLength": 80},
        "employee_bank_account": {"type": "string", "maxLength": 80},
        "location": {"type": "string", "maxLength": 80},
        "input_date": {"type": "string", "maxLength": 20},
        "operation_date": {"type": "string", "maxLength": 20},
        "firm_id": {"type": "number"}
      },
    "required": ["title"]
}
