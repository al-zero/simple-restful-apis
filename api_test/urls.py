from django.urls import path, include
from . import views
from .views import SimpleApiView, SimpleGenericsView, SimpleGenericsUpdateView, SimpleViewSetView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("simple-viewset", SimpleViewSetView)

urlpatterns = [
    path('', views.simple, name='simple'),

    # API view method
    path('simple_api/', SimpleApiView.as_view(), name='simple_api'),
    path('simple_api/<int:id>', SimpleApiView.as_view(), name='simple_api_update'),

    # Generics API view method
    path('simple_generics_view/', SimpleGenericsView.as_view(), name='simple_generics_view'),
    path('simple_generics_view/<int:id>/', SimpleGenericsUpdateView.as_view(), name='simple_generics_update_view'),

    # ViewSet method
    path('view-set/', include(router.urls)),
]
