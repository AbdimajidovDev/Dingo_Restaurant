from django.contrib import admin
from django.utils.html import format_html

from .models import *


@admin.register(FoodModel)
class FoodModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'about', 'price', 'created')
    list_display_links = ('title', 'about')


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created')
    list_display_links = ('category_name',)


@admin.register(ChefModel)
class ChefModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'level')
    list_display_links = ('full_name',)


@admin.register(ChefLevel)
class ChefLevelAdmin(admin.ModelAdmin):
    list_display = ('ch_level', )
    list_display_links = ('ch_level', )


@admin.register(BookingModel)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'num_of_g', 'time', 'date')
    list_display_links = ('name', 'date', 'time')
    search_fields = ('name', 'phone_number')


@admin.register(TagsModel)
class TagsModelAdmin(admin.ModelAdmin):
    list_display = ('tag', )
    list_display_links = ('tag', )
