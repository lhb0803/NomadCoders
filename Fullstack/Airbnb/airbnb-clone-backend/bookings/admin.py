from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "kind",
        "user",
        "guests",
        "room", "experience",
        "check_in", "check_out",
        "experience_date",
    )

    list_filter = (
        "kind",
    )