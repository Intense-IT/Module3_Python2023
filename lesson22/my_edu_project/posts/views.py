# CBV, Class Based Views, Представления на основе классов

# Перечень встроенных CBV
# https://ccbv.co.uk/projects/Django/5.0/

# from django.shortcuts import render
# from django.http import HttpResponseRedirect

# Импорт базовых классов View, TemplateView и ListView
# from django.views import View
# from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Post


# Рассмотрим два варианта представлений,
# FBV (на основе функций) и CBV (на основе классов) для страницы,
# отображающей форму добавления публикации.

# FBV
# def post_form(request, pk):
#     template_name = 'post_form.html'
#     form = MyForm()

#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('post_list/')
#     return render(request, template_name, {'form': form})

# CBV
# class PostView(View):
#     template_name = 'post_form.html'
#     form_class = MyForm

#     Для каждого типа запросов (GET, POST и т.д.) создается отдельный метод,
#     который вызывается при получении соответствующего типа запроса.
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('post_list/')
#         else:
#             return render(request, self.template_name, {'form': form})


# Создаем класс представления на основе встроенного класса TemplateView.
# По функционалу он ничем от обычного применения TemplateView не отличается.
# class ContactsView(TemplateView):
#     Передаем путь и название шаблона, который будет применяться,
#     встроенному свойству класса template_name.
#     template_name = 'posts/contacts.html'


# Рассмотрим кейс получения списка публикаций двумя способами,
# посредством FBV и CBV.

# FBV
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'post_list.html', {'post_list': posts})

# CBV
# Для этого создаем класс представления, дочерний встроенному классу ListView.
# class PostListView(ListView):
#     Для определения набора данных, которые будут переданы в качестве
#     контекста зададим значение встроенному свойству model.
#     model = Post


# Реализация представления для списка публикаций с настройкой параметров.
class PostList2View(ListView):
    # Если хотим получить не все объекты модели, а только часть,
    # определим значение встроенного свойства queryset (тип данных QuerySet).
    queryset = Post.objects.filter(title__endswith='2')

    # Для возможности переопределения имени переменной, в которой передается
    # шаблону набор объектов (вместо автоматически сформированного имени),
    # зададим встроенное свойство context_object_name.
    context_object_name = 'posts'

    # Для переопределения шаблона, использованного по умолчанию,
    # необходимо задать значение встроенному свойству template_name.
    template_name = 'posts/post_list_new.html'
