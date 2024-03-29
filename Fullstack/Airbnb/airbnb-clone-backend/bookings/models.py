from django.db import models
from common.models import CommonModel

class Booking(CommonModel):
    """
    Booking Model Definition
    """
    class BookingKindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"
    
    kind = models.CharField(max_length=15, choices=BookingKindChoices.choices)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey("rooms.Room", null=True, blank=True, on_delete=models.SET_NULL, related_name="bookings")
    experience = models.ForeignKey("experiences.Experience", null=True, blank=True, on_delete=models.SET_NULL, related_name="bookings")
    guests = models.PositiveIntegerField()

    # for Room booking
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)

    # for Experience booking
    experience_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.kind.title()} booking by {self.user}"