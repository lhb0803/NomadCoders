from django.shortcuts import render
from .models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view()
def categories(request):
    all_categories = Category.objects.all()
    return Response(
        {
            "ok": True,
        }
    )