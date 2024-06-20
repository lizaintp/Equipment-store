from django.db import models
from apps.category.models import Category
# Create your models here.

class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        verbose_name='Категория',
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
