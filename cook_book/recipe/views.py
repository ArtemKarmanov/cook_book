from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from product.models import Product
from recipe.models import RecipeProduct, Recipe


def add_product_to_recipe(request: HttpRequest) -> HttpResponse:
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    try:
        recipe = Recipe.objects.get(pk=recipe_id)
        product = Product.objects.get(pk=product_id)
        recipe_product, created = RecipeProduct.objects.get_or_create(recipe_id=recipe, product_id=product)

        recipe_product.weight = weight
        recipe_product.save()

        if created:
            return HttpResponse(
                f'Продукт {product.title} весом {weight}г '
                f'успешно добавлен в рецепт {recipe.title}'
            )
        else:
            return HttpResponse(f'Вес продукта {product.title} изменен на {weight}')

    except Exception:
        return HttpResponse(f'Указанный продукт или рецепт не найдены')


def cook_recipe(request: HttpRequest) -> HttpResponse:
    recipe_id = request.GET.get('recipe_id')

    try:
        recipe = (
            Recipe.objects
            .prefetch_related('products')
            .get(pk=recipe_id)
        )
        products = recipe.products.all()

        for product in products:
            product.cooked += 1
            product.save()

        return HttpResponse(f'Продукты: {", ".join([product.title for product in products])} успешно использованы для приготовления')
    except Exception:
        return HttpResponse(f'Указанный рецепт не найден')
