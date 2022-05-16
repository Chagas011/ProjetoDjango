from django.contrib import admin

from .models import Category, Recipe

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'slug', 'is_publish', 'creat_at'
    list_display_links = 'title', 'id', 'slug'
    search_fields = 'id', 'title', 'slug', 'creat_at', 'description'
    list_filter = 'category', 'author', 'is_publish'
    list_per_page = 10
    list_editable = 'is_publish',
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('title',)
    }


admin.site.register(Category, CategoryAdmin)
