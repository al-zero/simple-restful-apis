from django.urls import path, include
from .models import Product
from .views import ProductView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("product-profile", ProductView)

urlpatterns = [
    path('', include(router.urls))
]
