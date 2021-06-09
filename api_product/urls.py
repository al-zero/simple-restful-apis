from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api_overview'),
    path('product-list/', views.ProductListView, name='product-list'),
    path('product-create/', views.ProductCreateView, name='product-create'),
    path('product-detail/<str:pk>/', views.ProductDetailView, name='product-detail'),
    path('product-update/<str:pk>/', views.ProductUpdateView, name='product-update'),
    path('product-delete/<str:pk>/', views.ProductDeleteView, name='product-delete'),

]
