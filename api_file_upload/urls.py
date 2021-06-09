from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserProfileView
from django.conf.urls.static import static

router = DefaultRouter()
router.register("user-profile", UserProfileView)

urlpatterns = [
    path('', include(router.urls))
]
