from django.urls import path
from .views import Perks, PerkView

urlpatterns = [
    path("perks/", Perks.as_view()),
    path("perks/<int:pk>", PerkView.as_view()),
]