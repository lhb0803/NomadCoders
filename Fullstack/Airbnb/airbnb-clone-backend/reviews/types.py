import strawberry
import typing
from . import models
from users.types import UserType


@strawberry.django.type(models.Review)
class ReviewType:
    id: strawberry.auto
    payload: strawberry.auto
