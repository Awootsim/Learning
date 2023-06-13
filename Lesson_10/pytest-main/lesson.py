import inspect


def plus(a, b):
    return a + b


def test1():
    assert plus(2, 2) == 4

def test1():
    assert plus(3, 3) == 6

g = globals().copy()
for k , v in g.items():
    if k.startswith('test') and inspect.isfunction(v):
        try:
            print(f'exec{k}')
            v()
            print(f'SUCCESS {k}')
        except Exception as err:
            exist
            print(f'FAILED {k}')