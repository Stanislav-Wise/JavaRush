from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='posts')
    rating = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', related_name='posts')

    def __str__(self):
        return f'{self.title}!'

    class Meta:
        ordering = ['title']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comments by {self.author}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Author(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author',
        null=True,
        blank=True,
        verbose_name='Пользователь',
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}!"


class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.author.name}"


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
