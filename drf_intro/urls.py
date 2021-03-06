"""drf_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('api.urls')),
                  path('api_product/', include('api_product.urls')),
                  path('api_test/', include('api_test.urls')),
                  path('user-profile/', include('api_file_upload.urls')),
                  path('api-ecommerce/v1/', include('api_ecommerce.urls')),
                  path('api-notes/v1/', include('api_notes.urls')),
                  path('api-profile/v1/', include('api_profile.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
