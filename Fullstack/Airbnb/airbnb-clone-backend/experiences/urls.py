from django.urls import path
from .views import Experiences, ExperienceView, ExperiencePerks, Perks, PerkView

urlpatterns = [
    path("", Experiences.as_view()),
    path("<int:pk>", ExperienceView.as_view()),
    path("<int:pk>/perks", ExperiencePerks.as_view()),
    path("perks/", Perks.as_view()),
    path("perks/<int:pk>", PerkView.as_view()),
]