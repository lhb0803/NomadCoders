from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    # configure serializer
    class Meta:
        model = Category
        fields = (
            "name",
            "kind",
        )