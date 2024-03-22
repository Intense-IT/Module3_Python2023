from django.contrib import admin

from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']
    list_filter = ['create_date']
    search_fields = ['title', 'text']
    empty_value_display = '-empty-'
    fields = ['title', 'text', 'pub_date', 'author', 'category',
              'create_date', 'update_date']
    readonly_fields = ['create_date', 'update_date']


admin.site.register(Category)
admin.site.register(Tag)
