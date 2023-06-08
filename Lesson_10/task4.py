# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest

@pytest.mark.usefixtures("class_fixture")
class TestMyClass:
    """
    Класс для тестов с фикстурами
    """
    @pytest.mark.usefixtures("test_fixture")
    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 2 == 2