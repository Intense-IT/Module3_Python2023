from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import MyForm


# Главная страница
def index(request):
    return render(request, 'users/index.html')


# Функция для регистрации пользователя
def register(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = MyForm()
    return render(request, 'registration/register.html', {'form': form})


# Функция для авторизации, начала сеанса
def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # authenticate - метод проверки учетных данных.
        # Принимает в качестве аргументов имя пользователя и пароль.
        # Если данные действительны и доступ к ресурсы имеется,
        # возвращается объект пользователя, иначе возвращается None.
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login - функция входа, авторизации пользователя.
            # Сохраняет id пользователя в сеансе Django.
            login(request, user)
            return redirect('index')
    return render(request, 'registration/login.html')


# Функция для выхода, завершении авторизации.
def my_logout(request):
    # logout - функция, позволяющая авторизированному пользователю
    # закончить сеанс и выйти.
    # При выходе все данные сеанса удаляются.
    logout(request)
    return redirect('users:login')


# Для ограничения доступа к странице неавторизированным пользователям
# необходимо добавить декоратор login_required.
# Если требуется определить, куда будет перенаправлен
# неавторизированный пользователь, задается параметр login_url.
@login_required(login_url='users:login')
def secret_page(request):
    return HttpResponse('Секретные данные')
