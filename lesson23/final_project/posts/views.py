from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post


class PostListView(ListView):
    '''Представление на основе класса для получения списка публикаций.'''
    queryset = Post.objects.filter(is_visible=True)
    paginate_by = 4
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    '''Представление на основе класса для получения отдельной публикации.'''
    model = Post
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'


class PostAddView(LoginRequiredMixin, CreateView):
    '''Представление на основе класса для добавления новой публикации.'''
    model = Post
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('posts:post_list')
    fields = ['title', 'text']

    def form_valid(self, form):
        # Зададим создаваемым публикациям в качестве автора
        # авторизированного пользователя.
        # Подобные действия можно осуществить через определение
        # метода form_valid(), вызываемого после успешной проверки формы.

        # Явно обозначаем, что публикацию с данными из формы (в виде объекта)
        # сохранять в базу данных пока не надо.
        instance = form.save(commit=False)

        # Задаем данной публикации авторизированного пользователя как автора.
        instance.author = self.request.user

        # После этого сохраняем дополненный объект в БД.
        instance.save()

        # При успешном сохранении перенаправляем пользователя
        # на страницу со списком публикаций.
        return redirect(reverse_lazy('posts:post_list'))


# Ниже пример приведен для сравнения.
# Считываем данные из формы посредством представления на основе функции (FBV).
# Автор задается публикации только после получения данных из формы.
# @login_required
# def add_post(request):
#     form = PostForm(request.POST)
#     if form.is_valid():
#         post = form.save(commit=False)
#         post.author = request.user
#         post.save()
