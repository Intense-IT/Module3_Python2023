# Сериализаторы (Serializers) - инструмент для преобразования (сериализации)
# сложных типов данных (queryset-ы, объекты моделей) в типы данных Python и
# после в JSON для последующей отправки сервисам,
# а также для обратного процесса преобразования (десериализации) JSON
# в сложные типы данных после валидации (проверки на ошибки).
from rest_framework import serializers
from .models import Post
from datetime import datetime


# Два способа создания сериализатора:
# 1. Класс Serializer, не привязанный к модели.
# Все поля такого сериализаторанеобходимо задавать явно.
# Также явно задаются методы сохранения и обновления данных в БД.
# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=150)
#     text = serializers.CharField()
#     pub_date = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.text = validated_data.get('text', instance.text)
#         return instance


# 2. Класс ModelSerializer, связанный с конкретной моделью.
# Поля, методы .create() и .update(), валидаторы создаются автоматически.
class PostSerializer(serializers.ModelSerializer):
    # Имена полей отталкиваются от имен полей в модели.
    # Задать свое имя можно благодаря атрибуту source,
    # связывающему новое имя с полем модели.
    post_title = serializers.CharField(source='title')

    # У нас сохраняется возможность переопределить методы .create() и .update()
    # def create(self, validated_data):
    #     pass

    # def update(self, instance, validated_data):
    #     pass

    # Метод .to_representation() отвечает за преобразование
    # собственных типов данных в представление, подходящее для сериализации.
    # Вызывается, когда сериализатору необходимо преобразовать объект Python
    # (будь то объект модели Django или набор данных queryset)
    # в сериализуемое представление (например, словарь).
    def to_representation(self, instance):
        # Преобразуем объект instance в словарь унаследованным методом.
        representation = super().to_representation(instance)
        # Переопределим значение поля 'pub_date' на более читабельное.
        representation['pub_date'] = instance.pub_date.strftime('%d/%m/%Y')
        # Возвращаем словарь для последующего преобразования в JSON.
        return representation

    # Метод .to_internal_value() отвечает за преобразование
    # сериализованных данных, полученных от клиента,
    # во внутреннее представление, пригодное для обработки.
    # Вызывается, когда сериализатору необходимо преобразовать
    # входящие сериализованные данные (напр., словарь Python)
    # в собственные типы данных.
    def to_internal_value(self, data):
        # Получаем словарь с данными и изменяем нужные данные.
        data['pub_date'] = datetime.strptime(
            data.get('pub_date', '01/01/2024'), '%d/%m/%Y')
        # Возвращаем преобразованные в собственный тип данные.
        return super().to_internal_value(data)

    # В классе Meta задаются связанная модель и используемые поля.
    class Meta:
        model = Post
        # Вместо перечисления всех полей модели можно указать сразу все
        # командой '__all__', однако такой подход нерекомендуем,
        # т.к. явное лучше неявного.
        # fields = '__all__'

        # Перечисляем поля модели в нужном нам порядке,
        # которые хотим передавать в сериализаторе.
        # При переопределении имени поля через атрибут source
        # передавать необходимо новое имя, а не название поля в модели.
        fields = ('post_title', 'text', 'pub_date')
