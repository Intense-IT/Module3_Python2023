from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# Хоть мы и создали свой класс для объекта пользователя,
# получаем его обычным способом - через метод get_user_model.
User = get_user_model()


# Форма авторизации создается на основе встроенного класса UserCreationForm.
class MyForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'birth_date', 'is_married']
