from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.users import models
from apps.users import serializers

class UsersAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = models.Users.objects.all()
    serializer_class = serializers.UsersSerializer