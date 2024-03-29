# Generated by Django 5.0.1 on 2024-01-28 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('recipe', '0005_recipe_products_alter_recipeproduct_recipe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(related_name='recipes', through='recipe.RecipeProduct', to='product.product'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
