# # from pathlib import Path
# # work_dir = Path.cwd()
# # print(work_dir)
# # path = Path("Lesson 7/task_1(1).py")
# # path2 = Path("Lesson 7/task_1(1).py", "sub1", "file.txt")
# # path3 = Path().joinpath("subdirectory", "sub1")
# #
# # abs_pat1 = Path(Path.cwd(), path)
# # print(abs_pat1)
# # abs_pat2 = Path.cwd().joinpath(path3)
# # print(abs_pat2)
# #
# # print(abs_pat1.is_dir())
# #
# # test_file = Path.cwd().glob('*.py')
# # for i in test_file:
# #     print(i)
#
# # f = open('testfile.txt')
# # print(*f)
# # f2 = open(r'D:\Pyt\Learning\Lesson 9\test_file\testfile.txt', encoding='utf-8')
# # print(f2.read(4))
# # print(f2.read(4))
# # try:
# #     f3 = open('read4.txt', mode="r", encoding='utf-8')
# #     try:
# #         f3.seek((0))
# #         print(f3.read(6))
# #         assert False
# #     finally:
# #         f3.close()
# # except FileNotFoundError:
# #     print("Нету")
#
#
# # with open("read.txt", mode="r", encoding="utf-8") as f4:
# #         f4.seek(0)
# #         print(f4.read())
# #         assert False
# class Locklist:
#     def __init__(self, our_list):
#         self.our_list = our_list
#
#     def __enter__(self):
#         self.temp_list = self.our_list.copy()
#         return self.temp_list
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.our_list[:] = self.temp_list
#
# list1 = [1, 2, 3]
# list2 = [1, 2, 5]
# try:
#     with Locklist(list1) as ll:
#         for i in range(len(ll)):
#             ll[i] += list2[i]
# finally:
#     print(list1)

import time



def conter(count = 10):
    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            for i in range(count):
                start1 = time.time()
                res = func(*args, **kwargs)  # вызов функции
                end1 = time.time()
                print("абоба")
            print(f'Выполнение {end1-start1}')
            print(f'Среднее {end1-start}/10')
            return res
        return wrapper
    return timer


@conter(count = 10)
def seo_file(string):
    """Функция которая чего-то делает"""
    with open('file_new.txt', "w") as f:
        for i in range(100000):
            f.write(f'{str(i)} {string}\n')


seo_file('sbis.ru')