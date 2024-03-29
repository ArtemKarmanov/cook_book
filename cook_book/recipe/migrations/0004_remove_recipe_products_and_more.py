# Generated by Django 5.0.1 on 2024-01-28 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('recipe', '0003_alter_recipeproduct_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='products',
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='product.product'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='recipe_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='recipe.recipe'),
        ),
    ]
