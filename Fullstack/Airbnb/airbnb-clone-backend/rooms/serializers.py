from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Room, Amenity
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = (
            "id",
            "name",
            "country",
            "city",
            "price",
            "rating",
        )
    
    def get_rating(self, room):
        return room.rating_average()

class RoomViewSerializer(ModelSerializer):
    owner = TinyUserSerializer(read_only = True)
    amenities = AmenitySerializer(read_only = True, many = True)
    category = CategorySerializer(read_only = True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"
        depth = 1

    def get_rating(self, room):
        return room.rating_average()