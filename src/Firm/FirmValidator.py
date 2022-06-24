firm_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 3, "maxLength": 60},
        "email_address": {"type": "string", 'pattern': "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"},
        "activity_address": {"type": "string", "minLength": 3, "maxLength": 60},
        "legal_address": {"type": "string", "minLength": 3, "maxLength": 60},
        "phone_number": {"type": "number"},
        "hvhh": {"type": "string", "minLength": 3, "maxLength": 60},
        "tax_area_code": {"type": "number"},
        "chapter_registration_number": {"type": "number"},
        "insurer_account_number": {"type": "number"},
        "sphere_id": {"type": "number"},
      },
    "required": ["title", "email_address", "legal_address", "phone_number", "hvhh", "tax_area_code", "chapter_registration_number", "insurer_account_number", "sphere_id"]
}
