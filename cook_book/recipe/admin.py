from django.contrib import admin

from recipe.models import Recipe, RecipeProduct


class RecipeProductTabular(admin.TabularInline):
    model = RecipeProduct


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'
    ordering = 'id',
    search_fields = 'title',
    inlines = [RecipeProductTabular]
