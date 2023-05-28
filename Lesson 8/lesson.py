# # def my_funk():
# #     a = input("Введите а")
# #     b = input("Введите b")
# #     try:
# #         result = int(a) / int(b)
# #         print("Результат:", result)
# #
# #     except ZeroDivisionError:
# #         print("Нельзя делить на ноль")
# #     # except ValueError:
# #     #     print("Вводи числа")
# #     # else:
# #     #     print("Рузультат в квадрате", result**2)
# #     finally:
# #         print(int(a)+int(b))
# #     print("Программа выполнена")
# #
# # my_funk()
# #
# #
# # a, b = int(input("Введи число 1:")), int(input("Введи число 2:"))
# # r = ZeroDivisionError("ЫЫЫЫЫА")
# # if b == 0:
# #     raise r
#
# def print_my_dict(city):
#     my_dict = {"Ярославль": "Локомотив"}
#     try:
#         print(my_dict[city])
#     except KeyError:
#         print("Клуба нет")
#     except TypeError:
#         city = city[0]
#         print(my_dict[city])
#
# print_my_dict(["Ярославль"])

def prin_t(index):
    my_list = [2, 3, 4, 5, 6, 7]
    try:
        print(my_list[index])
    except IndexError:
        print(len(my_list), my_list[-1])

prin_t(8)

my_list2 = [2, 3, 4, 5, 6, 7]
for i in my_list2:
    print(i)