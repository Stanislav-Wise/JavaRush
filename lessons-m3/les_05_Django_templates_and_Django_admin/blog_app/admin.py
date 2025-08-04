from django.contrib import admin
from .models import Post, Comment, Author, AuthorProfile, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating')
    ordering = ('author', '-rating',)
    list_filter = ('rating', 'author')
    search_fields = ('title', 'content')
    search_help_text = "Введите часть заголовка или текста"