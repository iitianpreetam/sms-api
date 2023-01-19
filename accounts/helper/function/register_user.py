import logging
from rest_framework import status
from rest_framework.response import Response

from core.utils.custom_exceptions import (
    InternalServerError
)

from ..query.register_user import (
    register_user_query,
    add_user_to_group,
    create_user_profile
)
from ..query.util_queries import (
    is_user_by_username_exists,
    is_user_by_email_exists
)

logger = logging.getLogger('accounts')

def register_user_fn(request):
    data = request.data
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    password2 = data.get('password2')
    profile_picture = data.get('profile_picture')
    user_type = data.get('user_type')

    if is_user_by_username_exists(username):
        return Response({
            'error': 'User with this Username already exists',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)
        
    if is_user_by_email_exists(email):
        return Response({
            'error': 'User with this Email already exists',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if password != password2:
        return Response({
            'error': 'password did not matched',
            'data': None
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = register_user_query(request)
        add_user_to_group(user, user_type)
        profile = create_user_profile(user, profile_picture)
        return Response({
            'success': 'User Regitered Successfully',
            'data': {
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'profile_picture': profile.profile_picture
            }
        }, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f'helper/function/register_user/register_user_fn: {e}')
        raise InternalServerError