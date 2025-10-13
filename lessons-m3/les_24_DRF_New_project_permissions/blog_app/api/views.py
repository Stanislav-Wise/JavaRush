from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError

from blog_app.api.serializers import PostSerializer, CommentSerializer, TagSerializer, AuthorSerializer
from blog_app.api.permissions import IsOwnerOrReadOnly
from blog_app.models import Post, Comment, Tag, Author


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        """Для метода POST."""
        user = self.request.user
        author = getattr(user, 'author', None)
        if author is None:
            raise ValidationError('Нет автора')
        serializer.save(author=author)

    def perform_update(self, serializer):
        """Для метода PUT/PATCH."""

        instance = self.get_object()
        serializer.save(author=instance.author)


