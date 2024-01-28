from django.contrib import admin

from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'cooked'
    ordering = 'id', 'title'
    search_fields = 'title',
    readonly_fields = 'cooked',
