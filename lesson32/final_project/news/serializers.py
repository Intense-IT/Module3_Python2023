from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор модели News."""

    class Meta:
        model = News
        fields = ['title', 'text', 'pub_date', 'author']
