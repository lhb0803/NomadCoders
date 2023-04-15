import strawberry
from . import models

@strawberry.django.type(models.Room)
class RoomType:
    id: strawberry.auto
    name: strawberry.auto
    kind: strawberry.auto