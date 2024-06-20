from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.category import models
from apps.category import serializers

class CategoryAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer