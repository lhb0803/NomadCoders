from django.urls import path
from .views import PhotoView

urlpatterns = [
    path("photos/<int:pk>", PhotoView.as_view()),
]