from django.db import models

from product.models import Product


class Recipe(models.Model):

    class Meta:
        ordering = ['id']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    title = models.CharField(max_length=30)
    products = models.ManyToManyField(Product, through='RecipeProduct', related_name='recipes')


class RecipeProduct(models.Model):

    class Meta:
        ordering = ['id']
        verbose_name = 'Продукт в рецепте'
        verbose_name_plural = 'Продукты в рецептах'

    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.SmallIntegerField(default=0)
