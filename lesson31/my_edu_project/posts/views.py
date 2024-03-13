# Фильтры в DRF
# https://www.django-rest-framework.org/api-guide/filtering/

from rest_framework import generics
from django.contrib.auth import get_user_model
# Импорт необходимых фильтров.
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

from .models import Post
from .serializers import PostSerializer
# Импорт кастомного фильтра.
# from .filters import MyFilter

User = get_user_model()


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Задание бэкенда фильтрации на уровне представления:
    # filter_backends = [<ИмяКлассаФильтрации>]

    # DjangoFilterBackend
    # Позволяет фильтровать queryset на основе значений выбранных полей модели,
    # передаваемых в виде набора параметров запроса.
    # http://127.0.0.1:8000/api/v1/posts/?title=Zagolovok1&author=
    # Его необходимо предварительно установить и добавить в приложения.
    # pip install django-filter
    # filter_backends = [DjangoFilterBackend]
    # Перечисляем, по каким полям появляется возможность фильтрации:
    # filterset_fields = ['title', 'author']

    # SearchFilter
    # Простой поиск посредством одного параметра запроса.
    # http://127.0.0.1:8000/api/v1/posts/?search=text123
    # Значение параметра может содержать несколько условий поиска,
    # разделенных запятыми и/или пробелами.
    # http://127.0.0.1:8000/api/v1/posts/?search=zagolovok123%2Csuperadmin
    # По умолчанию ищутся частичные совпадения без учета регистра.
    # filter_backends = [SearchFilter]
    # Применим кастомный фильтр поиска, созданный на основе встроенного.
    # filter_backends = [MyFilter]
    # Перечисляем, по каким полям набора происходит поиск.
    # search_fields = ['title']
    # Поддерживается связанный поиск по ForeignKey или ManyToManyField
    # посредством двойного подчеркивания "__".
    # search_fields = ['title', 'author__username']
    # Посредством специальных символов можно конкретизировать поведение поиска:
    # "^" - поле начинается со значения; "=" - точное совпадение;
    # "$" - поиск по регулярному выражению; "@" - полнотекстовый поиск.
    # search_fields = ['title', '^author__username']

    # OrderingFilter
    # Дает возможность упорядочить результаты через параметр запроса.
    # http://127.0.0.1:8000/api/v1/posts/?ordering=title
    filter_backends = [OrderingFilter]
    # Перечисляем, по каким полям клиенту разрешено упорядочивать данные.
    ordering_fields = ['title', 'text']
    # Можно задать явно, по какому полю упорядочены данные по умолчанию.
    ordering = ['-text']

    # При необходимости можно задействовать несколько бэкендов фильтрации.
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Фильтрация возвращаемых данных посредством метода get_queryset().
    # def get_queryset(self):
    #     # user = self.request.user
    #     # user_id = self.kwargs.get('id')
    #     user_id = self.request.query_params.get('id')
    #     user = User.objects.get(pk=user_id)
    #     return Post.objects.filter(author=user)
