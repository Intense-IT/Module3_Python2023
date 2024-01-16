"""views.py это файл, хранящий функции-обработчики,
вызываемые при обращении к конкретному, связанному с ними URL-у.
Также мы тут применяем генерацию страниц по шаблону.
В качестве шаблонизатора используется DTL (Django Template Lenguage).
"""
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'username': 'Ruslan1'}
    return render(request, 'index.html', context)


# def greet(request, name):
#     return HttpResponse(f'Hello, {name}!')

def greet(request):
    return HttpResponse('Hello, Saeed!')
