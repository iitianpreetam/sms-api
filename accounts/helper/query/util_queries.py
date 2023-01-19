from django.contrib.auth.models import User

def is_user_by_username_exists(username):
    user = User.objects.filter(username=username).exists()
    return user

def is_user_by_email_exists(email):
    user = User.objects.filter(email=email).exists()
    return user