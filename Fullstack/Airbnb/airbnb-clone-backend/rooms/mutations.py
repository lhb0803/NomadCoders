from . import models
from strawberry.types import Info
import typing


def add_room(info: Info, name: str, price: int, rooms: int, toilets: int):
    # print(name)
    new_room = models.Room(
        name=name, 
        price=price,
        rooms=rooms,
        toilets=toilets,
        owner=info.context.request.user
    )
    new_room.save()
    return new_room

def update_room():
    return