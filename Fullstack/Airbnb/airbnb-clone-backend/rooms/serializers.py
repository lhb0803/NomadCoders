from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Room, Amenity
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = (
            "id",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
            "photos",
        )
    
    def get_rating(self, room):
        return room.rating_average()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user


class RoomViewSerializer(ModelSerializer):
    owner = TinyUserSerializer(read_only = True)
    amenities = AmenitySerializer(read_only = True, many = True)
    category = CategorySerializer(read_only = True)
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = "__all__"
        depth = 1

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user

    def get_rating(self, room):
        return room.rating_average()
    
    def get_is_liked(self, room):
        request = self.context["request"]
        if request.user.is_authenticated:
            return Wishlist.objects.filter(user=request.user, rooms__pk=room.pk).exists()
        else:
            return False