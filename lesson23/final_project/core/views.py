from django.shortcuts import render


# Представление для пользовательской ошибки 404
def page_not_found(request, exception):
    return render(
        request,
        'core/404.html',
        {'path': request.path},
        status=404
    )
