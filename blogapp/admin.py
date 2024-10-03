from django.contrib import admin
from blogapp.models import *

# admin.site.register(User)
# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(Comments)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_display_links = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', )
    list_display_links = ('category_name', )


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created')
    list_display_links = ('user', )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', )
    list_display_links = ('username', )
