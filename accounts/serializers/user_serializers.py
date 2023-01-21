from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class GetAuthorizedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']