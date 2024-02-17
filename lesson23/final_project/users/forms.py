from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


# Форма регистрации пользователя, наследуется от встроенной.
class MyUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'birth_year']

    # Валидатор-метод для отдельного поля
    # Проверяет, есть ли в имени (поле first_name) слово 'Руслан'.
    # В этом случае поднимается ошибка.
    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if 'Руслан' in data:
            raise forms.ValidationError('Руслану регистрация запрещена!')
        return data
