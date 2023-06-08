# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("args, expected_result", [
    pytest.param
    ((2, 2, 2), 0.5, marks=pytest.mark.smoke()),
    pytest.param((10, 2), 5, marks=pytest.mark.skip(reason="some bug")),
    ((100, 5, 2), 10),
])
def test_division(args, expected_result):
    """
    Проверка деления с параметрами
    """
    assert all_division(*args) == expected_result

