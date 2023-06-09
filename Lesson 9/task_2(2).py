# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


# Здесь пишем код

import datetime


def func_log(file_log='log.txt'):
    """
    Декоратор для записи вызовов функции в лог файл
    :param file_log: Путь до файла
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            """
            Функция, записывающая в лог-файл время вызова
            """
            with open(file_log, 'a', encoding="utf-8") as log_file:
                log_entry = f"{func.__name__} вызвана {datetime.datetime.now().strftime('%d.%m %H:%M:%S')}\n"
                log_file.write(log_entry)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@func_log()
def func1():
    """
    Функция для теста декоратора @func_log, выводит "Тест1"
    """
    print("Тест1")


@func_log(file_log='func2.txt')
def func2():
    """
    Функция для теста декоратора @func_log, выводит "Тест2", лог загружается в func2.txt
    """
    print("Тест2")


func1()
func2()
func1()
