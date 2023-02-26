from django.urls import path
from . import views

urlpatterns = [
    path("", views.CategoriesView.as_view()),
    path("<int:pk>", views.CategoryView.as_view()),
]