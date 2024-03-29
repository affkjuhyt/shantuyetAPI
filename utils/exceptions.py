from rest_framework.exceptions import APIException


class APIError(APIException):
    status_code = 400
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'api_error'
