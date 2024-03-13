from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # Задание значения по умолчанию для скрытого от пользователей поля author.
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('title', 'text', 'pub_date', 'author')
