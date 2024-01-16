# Перечень всех функций-обработчиков.
from django.shortcuts import render, HttpResponse
from .forms import PostForm


def index(request):
    context = {'username': 'Saeed'}
    return render(request, 'index.html', context)


def posts_list(request):
    return HttpResponse("Список публикаций")


def posts_detail(request, pk):
    return HttpResponse(f"Отдельная публикация {pk}")


# Прописываем обработчик страницы формы.
def form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            date = form.cleaned_data['date']
            return HttpResponse(f'{title}, {text}, {date}')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'form.html', context)
