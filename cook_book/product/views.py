from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from product.models import Product
from recipe.models import RecipeProduct, Recipe


def show_recipes_without_product(request: HttpRequest) -> HttpResponse:
    product_id = request.GET.get('product_id')

    try:
        product = (
            Product.objects
            .prefetch_related('recipes')
            .get(pk=product_id)
        )
        product_recipes = product.recipes.all()

        recipes_weight = (
            RecipeProduct.objects
            .filter(recipe_id__in=product_recipes, product_id=product, weight__lt=10)
        )
        recipes = [recipe_product.recipe_id for recipe_product in recipes_weight]

        recipes_without_product = Recipe.objects.exclude(pk__in=product_recipes)
        recipes.extend(recipes_without_product)

        data = {
            'product': product,
            'recipes': recipes
        }
    except Exception:
        data = {
            'product': None,
            'recipes': None
        }

    return render(request, 'product/product-index.html', context=data)
