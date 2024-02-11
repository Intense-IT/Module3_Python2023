# Использование представлений от классов, CBV, для обработки адресов.
from django.views.generic import TemplateView
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Использование представления на основе функции, FBV.
    # path('post_form/<int:pk>', views.post_form),

    # Использование представления на основе класса, CBV.
    # path('post_detail/<int:pk>', views.PostView.as_view()),

    # CBV может принимать именованные аргументы для переназначения свойств.
    # Это создает возможность получать разный функционал у одного CBV.
    # path('post_detail2/<int:pk>', views.PostView.as_view(
    #     template_name='user_form.html',
    #     form_class='SecondForm',
    # )),

    # Если необходимо отрисовать шаблон без передачи данных в форме контекста,
    # удобнее использовать встроенный класс TemplateView.
    path('contacts/', TemplateView.as_view(
        template_name='posts/contacts.html')),

    # Можем воспользоваться CBV на основе встроенного класса TemplateView.
    # В нашем случае результат будет тот же, что и в примере выше.
    # path('contacts/', views.ContactsView.as_view()),

    # Применим представление на основе встроенного класса ListView.
    path('posts_list/', views.PostList2View.as_view(), name='post_list'),
]
