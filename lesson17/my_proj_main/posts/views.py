from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная')


def posts_list(request):
    context = {'current_id': 5}
    return render(request, 'posts/posts_list.html', context)


def posts_detail(request, id):
    context = {'id': id}
    return render(request, 'posts/posts_detail.html', context)
