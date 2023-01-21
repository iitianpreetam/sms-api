from django.db import models
from django.contrib.auth.models import User
from core.common.constants import BASE_STATIC_ENTRY_FOLDER

class Profile(models.Model):
    GENDER = (('Male', 'Male'),('Female', 'Female'),('Other', 'Other'))

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length = 10, choices = GENDER, null=True, blank=True)
    address = models.TextField(null = True, blank=True)
    profile_picture = models.CharField(max_length=400, default='', blank=True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    def __str__(self):
        return f'@{self.user.username}\'s Profile'