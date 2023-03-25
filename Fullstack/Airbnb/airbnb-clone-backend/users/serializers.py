from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import User
from reviews.models import Review

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

class PublicUserSerializer(ModelSerializer):
    reviews_cnt = SerializerMethodField()

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
    
    def get_reviews_cnt(self, user):
        return Review.objects.filter(user=user).count()