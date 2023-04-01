from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Experience, Perk

class ExperienceListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = (
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_host",
        )

    def get_rating(self, experience):
        return experience.rating_average()
    
    def get_is_host(self, experience):
        request = self.context["request"]
        return experience.host == request.user

class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"