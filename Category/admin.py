from django.contrib import admin
from . import models
# Register your models here.

class CategoryAutoSlug(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.CategoryClass, CategoryAutoSlug)