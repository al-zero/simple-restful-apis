from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileView

from . import views

router = DefaultRouter()
router.register("user", ProfileView)

urlpatterns = [
    # path('', views.overview, name='overview'),
    path('', include(router.urls))
]
