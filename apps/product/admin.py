from django.contrib import admin
from apps.product import models
# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'updated_at', 'created_at', 'category')
    list_filter = ('title', 'price', 'updated_at', 'created_at', 'category')

