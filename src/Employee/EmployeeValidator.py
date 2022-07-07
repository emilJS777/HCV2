employee_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 3, "maxLength": 60},
        "code": {"type": "string", "minLength": 1, "maxLength": 10},
        "position": {"type": "string", "minLength": 1, "maxLength": 60},
        "adoption_date": {"type": "string", "maxLength": 10},
        "birth_date": {"type": "string", "maxLength": 10},

        "employee_bank_account": {"type": "string", "maxLength": 60},
        "social_card": {"type": "string", "maxLength": 60},
        "passport_number": {"type": "string", "maxLength": 60},
        "phone_number": {"type": "string", "maxLength": 60},
        "firm_id": {"type": "number"},

      },
    "required": ["title"]
}