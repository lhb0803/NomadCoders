from django.contrib import admin
from .models import Room, Amenity

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "rating_average",
        "kind",
        "total_amenities",
        "owner",
        "created_at",
    )
    list_filter = (
        "name",
        "country",
        "city",
        "price",
        "pet_friendly",
        "amenities",
    )
    search_fields =  (
        "name",
        "price",
        "owner__username",
    )

    # 7.3 Option 2
    def total_amenities(self, room):
        return room.amenities.count()

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
