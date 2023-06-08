class MyRange:

    def __init__(self, start, end=None):
        if end is None:
            start, end = 0, end
        self._start = start
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        current = self._start
        if self._start == self._end:
            raise StopIteration('end')
        self._start += 1
        return current


r = MyRange(1, 3)
print(type(r))
# print(r[0])
# print(next(r))
# print(next(r))
# print(next(r))
#
#
for i in r:
    print(i)

