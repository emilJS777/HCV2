user_create_schema = {
    "type": "object",
    "properties": {
        "email_address": {"type": "string", "minLength": 6,  'pattern': "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"},
        "first_name": {"type": "string", "minLength": 3, "maxLength": 24},
        "last_name": {"type": "string", "minLength": 3, "maxLength": 24},
        "position_id": {"type": "number"}
      },
    "required": ["email_address", "first_name", "last_name", "position_id"]
}

user_registration_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 6, "maxLength": 24},
        "password": {"type": "string", "minLength": 6, "maxLength": 24},
        "ticket": {"type": "string", "minLength": 6, "maxLength": 120},
      },
    "required": ["name", "password", "ticket"]
}
