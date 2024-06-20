from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from apps.users import views

router = DefaultRouter()
router.register('users', views.UsersAPI, basename='api_users')

urlpatterns = router.urls