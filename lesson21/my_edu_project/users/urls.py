from django.urls import path
from . import views


app_name = 'users'

# Все пути приложения users.
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('secret/', views.secret_page, name='secret_page'),
]
