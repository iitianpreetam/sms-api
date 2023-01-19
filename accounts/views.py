import logging
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from cerberus import Validator

from .helper.function import (
    register_user
)

from core.utils.custom_validators import is_email

logger = logging.getLogger('accounts')

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            schema = {
                'username': {
                    'required': True,
                    'empty': False,
                    'type': 'string',
                },
                'email': {
                    'required': True,
                    'empty': False,
                    'type': 'string',
                    'check_with': is_email
                },
                'first_name': {
                    'required': True,
                    'empty': False,
                    'type': 'string',
                },
                'last_name': {
                    'required': True,
                    'empty': False,
                    'type': 'string',
                },
                'password': {
                    'required': True,
                    'empty': False,
                    'type': 'string',
                    'minlength': 8
                },
                'password2': {
                    'required': True,
                    'empty': False,
                    'type': 'string',
                    'minlength': 8
                },
                'profile_picture': {
                    'required': True,
                    'empty': False,
                },
                'user_type': {
                    'required': True,
                    'empty': False,
                    'type': 'string',
                    'allowed': ['hod', 'staff', 'teacher', 'student']
                },
            }
            validator = Validator(schema)
            is_valid = validator.validate(request.data)
            if is_valid:
                return register_user.register_user_fn(request)
            return Response({
                'error': validator.errors,
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f'views/RegisterUserView/post: {e}')
            return Response({
                'error': 'Something Went Wrong. We are Working on it!',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)