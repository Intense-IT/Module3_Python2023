# Создаем декоратор
def func_info(func):
    def _f(*args):
        print('Все аргументы функции:', *args)
        func(*args)
        print('Выполнение функции окончено.')
    return _f


@func_info  # применяем декоратор при создании функции
def sum1(num1, num2):
    return num1 + num2


sum1(5, 10)
