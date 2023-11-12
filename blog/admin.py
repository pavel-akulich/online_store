from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Класс для админки блога"""
    list_display = ('pk', 'title', 'content', 'is_published', 'views_count',)
    search_fields = ('title',)
