from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Experience, Perk
from users.serializers import TinyUserSerializer

class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = (
            "name",
            "explanation",
        )

class ExperienceListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = (
            "id",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_host",
            "start_at",
            "end_at",
        )

    def get_rating(self, experience):
        return experience.rating_average()
    
    def get_is_host(self, experience):
        request = self.context["request"]
        return experience.host == request.user

class ExperienceViewSerializer(ModelSerializer):
    host = TinyUserSerializer(read_only = True)
    perks = PerkSerializer(read_only = True, many = True)

    class Meta:
        model = Experience
        fields = "__all__"
        depth = 1

