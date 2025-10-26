from rest_framework import serializers

from blog_app.models import Post, Author, Tag, Comment


class AuthorShortSerializer(serializers.ModelSerializer):
    """Только read only"""
    user_email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'user_email')

    def get_user_email(self, obj):
        return getattr(obj.user, 'email', None)


class TagShortSerializer(serializers.ModelSerializer):
    """Только read only"""
    class Meta:
        model = Tag
        fields = ('id', 'name')


class PostShortSerializer(serializers.ModelSerializer):
    """Только read only"""
    class Meta:
        model = Post
        fields = ('id', 'title')


class AuthorSerializer(serializers.ModelSerializer):
    """Полный сериализатор автора (CRUD)"""
    user_id = serializers.IntegerField(source='user.id' ,read_only=True)

    user_email = serializers.EmailField(source='user.email' ,read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'user_id', 'user_email')


class TagSerializer(serializers.ModelSerializer):
    """CRUD"""
    class Meta:
        model = Tag
        fields = ('id', 'name')


class PostSerializer(serializers.ModelSerializer):
    """CRUD"""
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        # write_only=True,
        help_text="Автор поста"
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        # write_only=True,
        help_text="Список тэгов"
    )
    # author_info = AuthorShortSerializer(source='author', read_only=True)
    # tags_info = TagShortSerializer(source='tags', many=True,read_only=True)
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            # запись
            'author',
            'tags',
            # чтение
            # 'author_info ',
            # 'tags_info ',
            'rating',
            'created_at'
        )

    read_only_fields = ('created_at', )


class CommentSerializer(serializers.ModelSerializer):
    """CRUD"""
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        # write_only=True,
        help_text="Автор поста"
    )

    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        write_only=True,
        help_text='Пост, к которому относится комментарий'
    )
    # author_info = AuthorShortSerializer(source='author', read_only=True)
    # post_info = PostShortSerializer(source='post', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            # запись
            'author',
            'post',
            # чтение
            # 'author_info ',
            # 'post_info ',
            'created_at'
        )

        read_only_fields = ('created_at',)