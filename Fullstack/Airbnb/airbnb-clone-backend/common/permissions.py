from strawberry.types import Info
import typing
from strawberry.permission import BasePermission

class OnlyLoggedIn(BasePermission):
    message = "You need to be logged in for this!" # when permssion blocks user

    def has_permission(self, source: typing.Any, info: Info, **kwargs):
        return info.context.request.user.is_authenticated