from django.contrib import admin
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from .models import Post, Comment, Author, AuthorProfile, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'tag_list')
    ordering = ('author', '-rating',)
    list_filter = ('rating', 'author')
    search_fields = ('title', 'content')
    search_help_text = "Введите часть заголовка или текста"

    # fields = ('title', 'content', 'author', 'tags', 'rating')
    # readonly_fields = ('rating',)

    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('Дополнительная информация', {
            'fields': ( 'author', 'tags', 'rating'),
            'classes': ('collapse',)
        }),
    )
    # exclude = ('author',)

    @admin.action(description='Увеличить рейтинг постов на 1')
    def increase_rating(self, request, queryset):
        """ Метод увеличения рейтинга."""
        for post in queryset:
            post.rating += 1
            post.save()
        self.message_user(request, f"{queryset.count()} постов обновлено")

    actions = (increase_rating, )

    def tag_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    tag_list.short_description = 'Тэги'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'profile_bio')
    list_filter = ('name', 'user',)
    search_fields = ('name', 'user',)
    search_help_text = "Введите имя автора"

    def profile_bio(self, obj):
        return obj.profile.bio if obj.profile else 'Профиль отсутствует'
    profile_bio.short_description = 'Биография'

admin.site.register(Author, AuthorAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    search_help_text = "Введите тэг"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'post')
    list_filter = ('author', )
    search_fields = ('text',)
    search_help_text = "Введите текст для поиска"

    @admin.action(description='Изменить текст')
    def change_text(self, request, queryset):
        """ Метод """
        for comment in queryset:
            comment.text = comment.text.capitalize()
            comment.save()
        self.message_user(request, f"{queryset.count()} комментов обновлено")

    actions = (change_text, )