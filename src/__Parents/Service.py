from flask import make_response, jsonify
import random
import string


class Service:
    # GENERATE TICKET CODE
    @staticmethod
    def generate_ticket_code(length=15, uppercase=True, lowercase=True, numbers=True):
        ticket_code = ''

        if uppercase:
            ticket_code += string.ascii_uppercase
        if lowercase:
            ticket_code += string.ascii_lowercase
        if numbers:
            ticket_code += string.digits

        return ''.join(random.choice(ticket_code) for i in range(length))

    # RESPONSES
    @staticmethod
    def response(success, obj, status_code) -> make_response:
        return make_response(jsonify(success=success, obj=obj), status_code)

    @staticmethod
    def response_conflict(msg=None):
        return Service.response(False, {'msg': msg or 'exist'}, 409)

    @staticmethod
    def response_not_found(msg=None):
        return Service.response(False, {'msg': msg or 'not found'}, 404)

    @staticmethod
    def response_invalid_password():
        return Service.response(False, {'msg': 'incorrect password'}, 403)

    @staticmethod
    def response_created(msg=None):
        return Service.response(True, {'msg': msg or 'successfully created'}, 201)

    @staticmethod
    def response_err_msg(msg):
        return Service.response(False, {'msg': msg}, 200)

    @staticmethod
    def response_updated(msg=None):
        return Service.response(True, {'msg': msg or 'successfully updated'}, 200)

    @staticmethod
    def response_ok(obj):
        return Service.response(True, obj, 200)

    @staticmethod
    def response_deleted(msg=None):
        return Service.response(True, {'msg': msg or 'successfully deleted'}, 200)

    @staticmethod
    def response_invalid_login():
        return Service.response(False, {'msg': 'invalid username and/or password'}, 401)

    @staticmethod
    def response_forbidden(msg=None):
        return Service.response(False, {'msg': msg or 'forbidden'}, 403)
