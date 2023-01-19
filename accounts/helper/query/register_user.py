import logging

from django.contrib.auth.models import User, Group
from ...models import Profile
from core.utils.file_utils import upload_profile_to_cloudinary

logger = logging.getLogger('accounts')

def register_user_query(request):
    data = request.data
    username = data.get('username')
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')
    try:
        user = User(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        return user
    except Exception as e:
        logger.error(f'helper/query/register_user/register_user_query: {e}')
        return None

def add_user_to_group(user, user_type):
    try:
        group = Group.objects.get(name=f'{user_type}_group')
        user.groups.add(group)
        return True
    except Exception as e:
        logger.error(f'helper/query/register_user/add_user_to_group: {e}')
        return False

def create_user_profile(user, profile_picture):
    try:
        profile = Profile(
            user=user
        )
        url = upload_profile_to_cloudinary(profile_picture, username=user.username)
        profile.profile_picture = url
        profile.save()
        return profile
    except Exception as e:
        logger.error(f'helper/query/register_user/create_user_profile: {e}')
        return None