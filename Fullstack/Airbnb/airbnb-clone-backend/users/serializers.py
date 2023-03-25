from rest_framework.serializers import ModelSerializer
from .models import User

class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "profile_photo",
        )

class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password", 
            "is_superuser",
            "id",
            "is_host",
            "first_name",
            "last_name",
            "groups",
            "is_staff",
            "is_active",
            "user_permissions",
        )