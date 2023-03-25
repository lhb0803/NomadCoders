from django.urls import path
from .views import Wishlists, WishlistView, WishlistToggle

urlpatterns = [
    path("", Wishlists.as_view()),
    path("<int:pk>", WishlistView.as_view()),
    path("<int:pk>/rooms/<int:room_pk>", WishlistToggle.as_view())
]