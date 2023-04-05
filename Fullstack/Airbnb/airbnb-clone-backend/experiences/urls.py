from django.urls import path
from .views import Experiences, ExperienceView, ExperiencePerks, Perks, PerkView, Bookings, BookingView

urlpatterns = [
    path("", Experiences.as_view()),
    path("<int:pk>", ExperienceView.as_view()),
    path("<int:pk>/perks", ExperiencePerks.as_view()),
    path("<int:pk>/bookings", Bookings.as_view()),
    path("<int:pk>/bookings/<int:booking_pk>", BookingView.as_view()),
    path("perks/", Perks.as_view()),
    path("perks/<int:pk>", PerkView.as_view()),
]