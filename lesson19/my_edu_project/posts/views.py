from django.shortcuts import render
from django.http import HttpResponse
# Импортируем агрегирующие функции.
from django.db.models import Max, Min, Sum, Count, Avg
# Импортируем Q функцию для логических операций в условиях фильтров.
from django.db.models import Q

from .forms import PostForm
from .models import Post, User


def index(request):
    return HttpResponse('Главная')


# Передаем нашу форму в шаблон.
def posts_list(request):
    # CRUD команды для Django ORM
    # Create - создание записи
    user = User.objects.get(id=1)
    # post = Post.objects.create(title='Заг5', text='Текст5', author=user)
    # Получение записи по первичному ключу
    # post = Post.objects.get(id=1)
    # Обновление записи
    # post = Post.objects.get(id=4)
    # post.text = 'Текст5_обновл'
    # post.save()
    # Удаление записи
    # post.delete()

    # Получение списка публикации
    # posts = Post.objects.all()

    # exclude - исключает из набора записи по заданному условию.
    # posts = Post.objects.exclude(title='Заг2')

    # Метод filter - фильтрует набор записей по заданному условию.
    posts = Post.objects.filter(title='Заг1')
    posts = Post.objects.filter(author=user)
    # contains - поле содержит значение
    posts = Post.objects.filter(text__contains='обновл')
    # startswith, endswith - поле начинается/заканчивается на значение
    posts = Post.objects.filter(text__startswith='Текст')
    posts = Post.objects.filter(text__endswith='новл')
    # in - вхождение значения поля в набор значений
    posts = Post.objects.filter(title__in=('Заг1', 'Заг2'))
    # range - вхождение в диапазон/интервал
    posts = Post.objects.filter(id__range=(1, 4))
    # gt, gte, lt, lte - сравнение значения поля >, >=, <, <=
    posts = Post.objects.filter(id__gte=4)
    # year, month, day, week, week_day, time, hour, minute, second -
    # проверка поля на совпадение по отдельному из значений
    posts = Post.objects.filter(pub_date__hour=17)
    # Можно комбинировать с другими способами фильтрации
    posts = Post.objects.filter(pub_date__hour__gte=16)
    # Можно комбинировать несколько фильтров
    posts = Post.objects.filter(
        pub_date__hour=17).filter(text__endswith='обновл')
    # Можно фильтровать по полям связанных объектов
    posts = Post.objects.filter(author__username='sup')

    # Сортировка объектов
    posts = Post.objects.filter(author__username='sup').order_by('pub_date')

    # Ограничение выдаваемых записей посредством среза
    posts = Post.objects.filter(
        author__username='sup').order_by('pub_date')[:3]

    # defer - исключение отдельных полей
    posts = Post.objects.defer('author').all()

    # count() - считает количество объектов
    count = Post.objects.filter(text__endswith='обновл').count()
    print(count)

    # aggregate - агрегирующие функции Min, Max, Count, Avg, Sum.
    # Это подразумевает, что они применяются сразу для всего набора объектов.
    print(Post.objects.aggregate(Min('id')))
    print(Post.objects.aggregate(Max('id')))
    print(Post.objects.aggregate(Sum('id')))
    print(Post.objects.aggregate(Count('id')))
    print(Post.objects.aggregate(Avg('id')))
    # Применять агрегирующие функции можно после фильтрации.
    print(Post.objects.filter(id__gte=1).aggregate(Avg('id')))

    # annotate - расширение объектов записей дополнительными полями.
    # Записываемые значения могут быть результатом вычислений,
    # в том числе агрегирующих функций.
    users = User.objects.annotate(posts_avg=Avg('posts__id'))
    for elem in users:
        print(elem.posts_avg)

    # Логические операторы для условий в фильтрах
    # Оператор ИЛИ, |
    posts = Post.objects.filter(Q(id=2) | Q(id=5))
    # Оператор И, &
    posts = Post.objects.filter(Q(id__gte=2) & Q(id__lte=5))

    context = {'current_id': 5, 'form': PostForm, 'posts': posts}
    return render(request, 'posts/posts_list.html', context)


def posts_detail(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, 'posts/posts_detail.html', context)
