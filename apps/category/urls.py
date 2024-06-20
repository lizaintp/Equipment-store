from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.category import views

router = DefaultRouter()
router.register('category', views.CategoryAPI, basename='api_category')

urlpatterns = router.urls