import os.path


def test_internal_fixture(tmp_path):
    """Создает и возвращает путь до временной директории"""
    print(tmp_path)
    print(os.path.isdir(tmp_path))


def test_internal_fixture2(request):
    """Получает доступ"""
    print(request.node.nodeid)
