from rest_framework import serializers

from blog_app.models import Post, Author, Tag, Comment


class AuthorShortSerializer(serializers.ModelSerializer):

    user_email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'user_email')

    def get_user_email(self, obj):
        return getattr(obj.user, 'email', None)