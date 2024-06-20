from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.product import models
from apps.product import serializers

from apps.category.models import Category
from apps.category.serializers import CategorySerializer

class ProductAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class CategoryAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer