from django.utils import timezone
from rest_framework import serializers
from .models import Booking

class CreateRoomBookingSerializer(serializers.ModelSerializer):
    
    # override to make mandatory fields
    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )
    
    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if value >= now:
            return value
        else:
            raise serializers.ValidationError("Cant' book in the past!")
    
    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if value >= now:
            return value
        else:
            raise serializers.ValidationError("Cant' book in the past!")

class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )