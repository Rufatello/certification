from django.contrib import admin

from shop.models import Factory, Product


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)