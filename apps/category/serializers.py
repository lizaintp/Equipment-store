from rest_framework import serializers
from apps.category import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'title', 'description']
