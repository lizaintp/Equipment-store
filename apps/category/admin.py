from django.contrib import admin
from apps.category import models
# Register your models here.
@admin.register(models.Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title', 'description')