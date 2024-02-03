# Пагинация
# Это инструмент для разбиения записей на отдельные страницы
# с ограниченным количеством записей на каждой.
# Предельное количество записей на одной странице задается явно.
# https://docs.djangoproject.com/en/5.0/topics/pagination/
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


def posts_list(request):
    # Данные, которые будут разбиты на отдельные блоки.
    posts = Post.objects.all()
    # Объект пагинации, которому указываются данные для разбиения и
    # предельное количество записей на одной странице.
    paginator = Paginator(posts, 2)
    # Общее количество записей
    print(paginator.count)
    # Общее кКоличество страниц
    print(paginator.num_pages)
    # Можно получить отдельную страницу пагинации с записями.
    # page1 = paginator.page(1)
    # print(page1)
    # Вывод объектов записей, хранящихся в полученной странице пагинации.
    # print(page1.object_list)
    # Считывается номер страницы пагинации, передаваемый в поле запроса.
    page_num = request.GET.get('page')
    # На основе номера страницы получаем объект страницы с записями.
    page_obj = paginator.get_page(page_num)
    # Передаем этот объект с записями в шаблон.
    context = {'page_obj': page_obj}
    return render(request, 'posts/posts_list.html', context)


def posts_detail(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, 'posts/posts_detail.html', context)
