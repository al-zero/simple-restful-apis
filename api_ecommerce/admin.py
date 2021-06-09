from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "category", "availability", "price"]


admin.site.register(Product, ProductAdmin)
