from rest_framework.filters import SearchFilter, BaseFilterBackend


# При необходимости есть создать свой механизм фильтрации.
# Кастомный класс должен наследоваться от SearchFilter
# и переопределять метод get_search_fields(self, view, request).

# Пример ниже сужает фильтрацию до поля 'text' при наличии в запросе
# параметра 'text_only'.
class MyFilter(SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('text_only'):
            return ['text']
        return super().get_search_fields(view, request)
# При добавлении параметра 'text_only' вместо заданного в представлении набора
# полей для поиска ['title', 'author__username'] с работающим запросом:
# http://127.0.0.1:8000/api/v1/posts/?search=zag1+sup
# задействуется набор полей из функции ['text'] с работающим запросом:
# http://127.0.0.1:8000/api/v1/posts/?text_only=1&search=text1


# Создание кастомного фильтра на основе класса BaseFilterBackend.
# Необходимо задать метод filter_queryset(self, request, queryset, view),
# возвращающий новый отфильтрованный набор запросов.
class CustomFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(author=request.user)
