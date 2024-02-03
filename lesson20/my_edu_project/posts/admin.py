# Админка - более тонкая настройка отображения записей модели.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
from django.contrib import admin
from .models import Post


# Для настройки отображения отдельной модели в админке создается
# специальный класс, дочерний ModelAdmin.
# В нем прописываются все свойства, влияющие на форму
# списка всех записей модели и страницы отдельной модели админки.
class PostAdmin(admin.ModelAdmin):
    # Настройка полей списка записей - какие поля и их порядок
    list_display = ['text', 'pub_date', 'title']

    # Добавление фильтра публикаций
    list_filter = ['pub_date']

    # Поисковая строка по значению указанных полей
    search_fields = ['title', 'text']

    # Значение по умолчанию для пустого поля всех записей
    # empty_value_display = "-empty-"
    # Значение по умолчанию для определенного пустого поля
    # @admin.display(empty_value="-empty-")
    # def text(self, obj):
    #     return obj.text

    # Исключение отдельных полей при добавлении записи
    # Стоит закомментировать, если в дальнейшем используете поле 'text'.
    # exclude = ['text']

    # Группировка и доп. настройка полей при добавлении записи
    fieldsets = (
        ('Главные', {
            'fields': ('title',)
        }),
        ('Вторичные поля', {
            'classes': ['collapse'],
            'fields': ('text', 'author')
        })
    )


# Для применения созданного класса с настройками указываем
# созданный класс админки после класса модели.
admin.site.register(Post, PostAdmin)

# Альтернативный способ связывания класса админки с классом модели
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     Блок со свойствами для настройки админки модели Post
