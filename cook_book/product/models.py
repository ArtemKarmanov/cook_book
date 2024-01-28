from django.db import models


class Product(models.Model):
    """
    Модель продуктов
    """
    class Meta:
        ordering = ['id']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    title = models.CharField(max_length=30)
    cooked = models.IntegerField(default=0)

    def __str__(self):
        return self.title
