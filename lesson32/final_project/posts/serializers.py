from rest_framework import serializers

from .models import Post, Category


BAD_WORDS = ['блин', 'черт']


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для публикации."""

    post_author = serializers.StringRelatedField(
        source='author', read_only=True)
    tags = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name')

    def to_representation(self, instance):
        return super().to_representation(instance)

    def to_internal_value(self, data):
        return super().to_internal_value(data)

    def validate(self, attrs):
        return super().validate(attrs)

    def validate_text(self, value: str) -> str:
        for word in BAD_WORDS:
            if word in value.lower():
                raise serializers.ValidationError(
                    f'Запрещено использовать {word}.')
        return value

    class Meta:
        model = Post
        fields = ['title', 'text', 'pub_date', 'post_author', 'category',
                  'tags']


class PostListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка публикаций."""

    class Meta:
        model = Post
        fields = ['title', 'author']


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий."""

    posts = PostListSerializer(read_only=True, many=True)
    count = serializers.SerializerMethodField()

    def get_count(self, obj) -> int:
        return obj.posts.count()

    class Meta:
        model = Category
        fields = ['title', 'posts', 'count']
