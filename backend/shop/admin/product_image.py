from django.contrib import admin

from shop.models import ProductImageModel


class ProductImageInline(admin.TabularInline):
    model = ProductImageModel
    extra = 1