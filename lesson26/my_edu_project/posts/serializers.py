from django.utils import timezone
from rest_framework import serializers
from .models import Post, Category


# Создаем собственный тип поля сериализатора.
class BigName(serializers.Field):
    def to_representation(self, value):
        return value.upper()

    def to_internal_value(self, data):
        data = data[0] + data[1:].lower()
        return data


class PostSerializer(serializers.ModelSerializer):
    # По умолчанию для внешнего ключа задается тип поля
    # serializers.PrimaryKeyRelatedField. Можем заменить на:
    # 1. serializers.StringRelatedField,
    # 2. serializers.SlugRelatedField,
    # 3. serializers.HyperlinkedRelatedField
    author = serializers.StringRelatedField(read_only=True)

    # Задаем полю title созданный нами тип данных - BigName.
    title = BigName()

    # Реализация общей проверки на уровне объекта.
    def validate(self, attrs):
        if attrs['title'] not in attrs['text']:
            raise serializers.ValidationError(
                'Заголовок статьи должен фигурировать в тексте.')
        return attrs

    # Реализация проверки на уровне поля, даты публикации.
    # Нельзя опубликовать статью в прошлом.
    # Способ именования метода валидации поля - validate_<имя поля>()
    def validate_pub_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                'Публикация статьи не может произойти в прошлом.')
        return value

    class Meta:
        model = Post
        fields = (
            'title', 'text', 'pub_date', 'create_date', 'author', 'category')


class CategorySerializer(serializers.ModelSerializer):
    # Вместо списка id возвращаем строковое представление объектов Post.
    # posts = serializers.StringRelatedField(read_only=True, many=True)

    # Вместо списка id возвращаем сериализованные объекты Post.
    posts = PostSerializer(read_only=True, many=True)

    # Добавляем новое поле, которого нет в модели.
    count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('title', 'posts', 'count')

    # Вычисляем значение нового поля count - количество публикаций в категории.
    # Способ именования метода - get_<имя поля>().
    def get_count(self, obj):
        return obj.posts.count()
