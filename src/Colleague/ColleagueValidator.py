colleague_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 2, "maxLength": 40},
        "code": {"type": "string", "maxLength": 10},
        "activity_address": {"type": "string", "minLength": 3, "maxLength": 60},
        "legal_address": {"type": "string", "minLength": 3, "maxLength": 60},
        "phone_number": {"type": "number"},
        "hvhh": {"type": "string", "minLength": 3, "maxLength": 60},
        "account_number": {"type": "string", "maxLength": 60},
      },
    "required": ["title"]
}
