from django import forms
from .models import Post


# Создаем форму на основе конкретной модели.
class PostForm(forms.ModelForm):
    class Meta:
        # Указываем, на основе какой модели создавать форму.
        model = Post
        # Определяем список и порядок полей формы.
        fields = ['title', 'text', 'tags', 'author']
        # Явно обозначаем содержимое элементов label.
        labels = {
            'title': 'Заг-к публ-ии'
        }
