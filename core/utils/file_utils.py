from cloudinary import uploader
from ..common.constants import BASE_STATIC_ENTRY_FOLDER

def upload_profile_to_cloudinary(profile_picture, username):
    folder = f'{BASE_STATIC_ENTRY_FOLDER}/profile/'
    public_id = f'{username}_profile'
    file_ext = profile_picture.name.split('.')[-1]
    profile_picture.name = f'{username}_profile.{file_ext}'

    result = uploader.upload(
        profile_picture,
        folder=folder,
        public_id=public_id,
        overwrite = True,
        invalidate = True
    )
    return result.get('secure_url')