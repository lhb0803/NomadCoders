from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=50)
    kind = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)