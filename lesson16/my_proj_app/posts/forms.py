# Создаем свою форму для отображении в шаблоне.
from django import forms


# Класс формы наследуюется от родительского класса forms.Form
class PostForm(forms.Form):
    # Прописываем все поля, требуемые в форме.
    # В зависимости от типа поля будут накладываться разные проверки
    # на введеные данные.
    title = forms.CharField(label='Заголовок', max_length=100)
    text = forms.CharField(label='Текст статьи', widget=forms.Textarea)
    date = forms.DateField(label='Дата публикации')
