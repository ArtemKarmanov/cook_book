from django.urls import path

from .views import show_recipes_without_product

urlpatterns = [
    path('recipes_without_product', show_recipes_without_product, name='recipes_without_product')
]