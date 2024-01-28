from django.urls import path

from .views import add_product_to_recipe, cook_recipe

urlpatterns = [
    path('add_product', add_product_to_recipe, name='add_product'),
    path('cook', cook_recipe, name='cook'),
]
