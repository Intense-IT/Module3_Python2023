# Blueprint - независимый модуль, отделяемый от основного приложения.
# Является инструментом для разделения логики, включает в себя
# набор обработчиков адресов, объединенных общей логикой.
from flask import Blueprint


# Создаем экземпляр Blueprint
analytics_blueprint = Blueprint(
    'analytics',
    __name__,
    template_folder='templates'
)


# Используем blueprint для создания обработчика адреса.
@analytics_blueprint.route('/analytics')
def get_analytics():
    return 'Аналитика по данному сервису'
