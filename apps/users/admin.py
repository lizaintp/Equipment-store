from django.contrib import admin
from apps.users import models
# Register your models here.
@admin.register(models.Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_filter = ('username',)
