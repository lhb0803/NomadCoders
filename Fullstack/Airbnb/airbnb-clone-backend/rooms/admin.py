from django.contrib import admin
from .models import Room, Amenity

@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices, )
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
