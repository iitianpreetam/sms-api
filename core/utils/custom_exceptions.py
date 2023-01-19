from rest_framework import status
from rest_framework.exceptions import APIException

from ..common import messages as glob_msg

class InternalServerError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = glob_msg.INTERNAL_SERVER_ERROR
    default_code = 'internal_server_error'