# # # # from pprint import pprint
# # # # # # h = "hello"
# # # # # #
# # # # # # def my_funk():
# # # # # #     global h
# # # # # #     h = "HELL"
# # # # # #     print(h)
# # # # # #
# # # # # # my_funk()
# # # # # # print(h)
# # # # #
# # # # # n = 3
# # # # #
# # # # # def global_1():
# # # # #     n = 1
# # # # #
# # # # #     def local_funk():
# # # # #         nonlocal  n
# # # # #         n = 2
# # # # #
# # # # #         print(n, "local")
# # # # #
# # # # #     local_funk()
# # # # #
# # # # #     print(n, "global")
# # # # #
# # # # # global_1()
# # # #
# # # # def hello(*args):
# # # #     name = "Ivan"
# # # #     print ("Hello,", name, args)
# # # #
# # # # def bye(*args):
# # # #     name = "Ivan"
# # # #     print ("bye,", name, args)
# # # #
# # # # pprint(locals())
# # # import math
# # # print(dir(math))
# # # print(math.pi)
# # from  sys import  path
# # from  pprint import  pprint
# # pprint(path)
# # import lesson
# # print(lesson.n)
# # lesson.n = 2
# # print(lesson.n)
# # import lesson
# # print(lesson.n)
# #
# # import importlib
# # importlib.reload(lesson)
# # print(lesson.n)
# # print(locals())
#
# from math import pi, e
# print(e)
# print(pi)
# def pi():
#     print("Hellp")
# pi()

from package import  file1
print(file1.a)
