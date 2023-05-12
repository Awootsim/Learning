#
#
# my_dict = {'key_string': 'ключ-строка', 2: 'ключ-число', (1, 2, 3): 'ключ-кортеж'}
# print(my_dict)
#
# dict_1 = {1:12, 2:45}
# print(dict_1, type(dict_1))
# dict_2 = dict(ana="43643", ono="5645")
# dict_3 = dict([("ana", "43643"), ("ono","5645")])
# print(dict_3)
# print(dict_2)
# dict_4 = {}
# new_dict = dict.fromkeys(['sasha', 'vasya'], 2)
# print(new_dict)
# new_dict2 = {item: item**2 for item in [0,1,2,3,4,5,6]}
# print(new_dict2)
#
# capitals = {'Russia': 'Moscow', 'France': 'Paris', 'England': 'London'}
#
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# print(capitals.get(4, 'Нету'))
# print(capitals.popitem())
# print(capitals)
# capitals['Germany'] = 'Berlin'
# print(capitals)
# capitals['France'] = 'Sochi'
# print(capitals)
# capitals.update({"Poland": "Warshaw"})
# print(capitals)
# # capitals.clear()
# new_cap = capitals.copy()
# # print(capitals)
#

def square(x):
    """
    Возводим число в квадрат
    :return: квадрат числа
    :param x: число которое возводим
    """
    return x**2

print(square(7))

def my_print(a, b, c):
    print(a, "is stored in a")
    print(b, "is stored in b")
    print(c, "is stored in c")
    return a, b, c

my_print(1, 2, 3)
