from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.product import views
from apps.category.views import CategoryAPI

router = DefaultRouter()
router.register('product', views.ProductAPI, basename='api_product')
router.register('category', CategoryAPI, basename='api_category')

urlpatterns = router.urls