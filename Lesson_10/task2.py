# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_division_first():
    """
    Проверка правильности деления
    """
    assert all_division(2, 2) == 1


@pytest.mark.smoke
def test_division_second():
    """
    Проверка правильности деления с более чем 2 аргументами
    """
    assert all_division(2, 2, 2) == 0.5


def test_division_third():
    """
    Проверка правильности деления с отрицательными аргументами
    """
    assert all_division(-100000, 5, 10) == -2000


@pytest.mark.negative
def test_division_fourth():
    """
    Проверка ошибки при вводе строки
    """
    with pytest.raises(TypeError) as exc_info:
        all_division(-100000, "5", 10)

    assert str(exc_info.value) == "unsupported operand type(s) for /=: 'int' and 'str'"


@pytest.mark.negative
def test_division_fifth():
    """
    Проверка деления на 0
    """
    with pytest.raises(ZeroDivisionError) as exc_info:
        all_division(20, 0, 10)

    assert str(exc_info.value) == 'division by zero'
