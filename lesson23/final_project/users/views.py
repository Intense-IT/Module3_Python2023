from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import MyUserForm


# CBV для регистрации пользователя.
class RegisterView(CreateView):
    '''Представление на основе класса для регистрации пользователя.'''
    # Класс формы
    form_class = MyUserForm
    # Явно указаны путь и название используемого шаблона.
    template_name = 'users/register.html'
    # Адрес, куда будет переброшен пользователь после успешной авторизации.
    success_url = reverse_lazy('users:login')
