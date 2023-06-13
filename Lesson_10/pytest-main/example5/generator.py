import types


def my_range(start, end=None):
    if end is None:
        start, end = 0, start
    yield start
    start += 1
    if start == end:
        raise StopIteration('end')


r = my_range(1, 3)
print(r)
print(type(r))
# for j in r:
#     print(j)

print(isinstance(r, types.GeneratorType))


a = (i for i in range(10))
b = [(i for i in range(10))]
print(type(b))
print(b[0])

print(type(a))
print(a[0])

