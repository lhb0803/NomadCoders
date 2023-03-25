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

    def validate(self, data):
        check_in = data["check_in"]
        check_out = data["check_out"]
        if check_in >= check_out:
            raise serializers.ValidationError("Check in should be smaller then Check out.")
        
        if Booking.objects.filter(check_in__lte=check_out, check_out__gte=check_in).exists():
            raise serializers.ValidationError("Already booked.")

        return data

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