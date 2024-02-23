# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


# # Представление для списка ресурсов
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# # Представление для отдельного ресурса
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# Реализация представления на основе класса APIView.
# Это подразумевает явное описание методов для разных типов запросов.
class PostListAPIView(APIView):
    # Метод для GET-запроса - на получение списка ресурсов.
    def get(self, request):
        posts = Post.objects.all()
        # Создается объект сериализатора, ему передаются набор данных и
        # указание many=True - что сериализуем несколько объектов.
        serializer = PostSerializer(posts, many=True)
        # Сериализованные данные возвращаются через конструкцию serializer.data
        return Response(serializer.data)

    # Метод для POST-запроса - на добавление новой записи.
    def post(self, request):
        # Передаем следующие данные в формате JSON (без поля pub_date):
        # {
        #     "post_title": "Заголовок",
        #     "text": "Текст",
        # }
        # На каждом из шагов для наглядности будем описывать содержимое
        # объекта serializer и его свойств.
        # Ниже перечислены команды вывода данных, вызываемые нами:
        # a. print(serializer, type(serializer))
        # b. print(serializer.initial_data, type(serializer.initial_data))
        # c. print(serializer.validated_data, type(serializer.validated_data))
        # d. print(serializer.data, type(serializer.data))

        # Шаг 1 - создается объект сериализатора, ему передаются данные
        # с запроса, после чего объект сохраняется в переменной serializer.
        serializer = PostSerializer(data=request.data)
        # a. Объект типа PostSerializer со значениями полей post_title и text.
        # b. Данные полей post_title и text в виде словаря.
        # с. Поднимается ошибка, .validated_data работает только
        # после проверки .is_valid().
        # d. Поднимается ошибка, .data работает должным образом только
        # после сохранения данных в модели методом .save().

        # Шаг 2 - вызов метода .is_valid(), проверяющего входных данных и
        # подтверждающего (или нет), что эти данные содержат
        # все обязательные поля и все поля имеют правильные типы.
        if serializer.is_valid():
            # a. Объект типа PostSerializer со значениями полей post_title,
            # text и pub_date. Все значения преобразованы в соответствии
            # с методом .to_internal_value().
            # b. Данные полей post_title, text и pub_date в виде словаря.
            # c. Данные полей post_title, text и pub_date в виде
            # упорядоченного словаря (OrderedDict) со списком кортежей.
            # d. Поднимается ошибка, .data работает должным образом только
            # после сохранения данных в модели методом .save().

            # Шаг 3 - вызов метода .save(), создающего или обновляющего запись
            # в базе данных, используя значения validated_data и
            # дополнительные данные, переданные как именованные аргументы
            # (текущий пользователь, текущее время).
            # Например, serializer.save(user=request.user)
            serializer.save()
            # a. Объект типа PostSerializer со значениями полей post_title,
            # text и pub_date.
            # b. Данные полей post_title, text и pub_date в виде словаря.
            # c. Данные полей post_title, text и pub_date в виде
            # упорядоченного словаря (OrderedDict) со списком кортежей.
            # d. Данные полей post_title, text и pub_date в виде
            # словаря встроенного в DRF типа ReturnDict. Все значения
            # преобразованы в соответствии с методом .to_representation()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
