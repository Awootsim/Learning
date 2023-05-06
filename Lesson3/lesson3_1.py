list1 = [1, 2, 3]
print(list1)

a = [1, "привет", 3, "Негры", [1, 2, 3]]
print(a)

b = list('string')
print(b)

c = list()
print(c)

print((a + b) * 2)

print(a[0:2])

a[2] = "пока"
print(a)

b[1:3] = 2, 3, 5
print(b)

print(len(b))

print(111 in a)
print(a[4][2])

d = [1, 2, -11, 3, 4, 5, 6, 7, 99, 99, 99]
e = [1, 2, 3, 4, 5]
print(sum(d), max(d), min(d))

print(d.index(99))
print(d.count(99))
#  e.clear()
#  e.remove(3)
e.pop(3)
#  del d
print(d)
e.insert(0, 123)
print(e)

e.append(273)
print(e)
e.append(list('sama'))
print(e)
e.extend([1, 2, 3])
print(e)
e.reverse()
e.reverse()
print(e)
d.sort()
print(d)

c = e.copy()
print(c)
p = "".join(["a", 'b', 'c'])
print(p)

print(sorted(d))
print(d.sort())
l = ['a', 'aaa', 'aaaaa', 'aaasaaaasdas', 'a', 'www']
l1 = sorted(l, key=len)
print(l1)


