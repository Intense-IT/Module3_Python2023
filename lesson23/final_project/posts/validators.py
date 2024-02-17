# Файл для хранения функций-валидаторов
from django import forms


# Функция-валидатор, определяющая, много ли символов в поле
def validate_long_value(value):
    if len(value) >= 50:
        raise forms.ValidationError(
            'Слишком много символов.',
            params={'value': value},
        )
