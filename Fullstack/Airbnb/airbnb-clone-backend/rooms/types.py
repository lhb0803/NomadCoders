import strawberry
from . import models
from users.types import UserType

@strawberry.django.type(models.Room)
class RoomType:
    id: strawberry.auto
    name: strawberry.auto
    kind: strawberry.auto
    owner: "UserType"