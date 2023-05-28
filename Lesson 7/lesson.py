# # # class Cats:
# # #
# # #     MAX_AGE = 38
# # #
# # #     def __init__(self, name, breed, age):
# # #         self.name = name
# # #         self.breed = breed
# # #         self.age = age
# # #         if age > self.MAX_AGE:
# # #             self.__class__.MAX_AGE = age
# # #
# # #     # def print_data(self):
# # #     #     print(
# # #     #         f"Имя: {self.name}\n"
# # #     #         f"Возраст: {self.age}"
# # #     #     )
# # #     def __repr__(self):
# # #         return (
# # #                      f"Имя: {self.name}\n"
# # #                      f"Порода: {self.breed}\n"
# # #                      f"Возраст: {self.age}"
# # #         )
# # #
# # # sema = Cats("Sema", "kot1", 12)
# # # sema2 = Cats("Sema2", "kot2", 40)
# # # sema.name = "васька"
# # # print(sema2.name, sema.name)
# # # print(sema)
# # # cats_list = [sema, sema2]
# # # # for cat in cats_list:
# # # #     cat.print_data()
# # # # Cats.MAX_AGE = 40
# # # print(sema.__class__.__dict__)
# # # print(sema.MAX_AGE)
# # # print(sema2.MAX_AGE)
# #
# # import time
# # class Counter:
# #
# #     @staticmethod
# #     def get_current_time():
# #         return  time.perf_counter()
# #
# #     def __init__(self):
# #         self.start = self.get_current_time()
# #
# #     def delta(self):
# #         return self.get_current_time() - self.start
# #
# # print(Counter.get_current_time())
# #
# # c = Counter()
# # time.sleep(1)
# # print(c.delta())
#
#
# class By:
#     CSS_SELECTOR = "css selector"
#     XPATH = "xpath"
#
#     def __init__(self):
#         self.my_variable = 1
#
#     @classmethod
#     def valid(cls, selector):
#         return selector in cls.__dict__.values()
#
# "css selector"
# print(By.CSS_SELECTOR)
# print(By.valid("css selector1"))



# class Employee:
#     def __init__(self, name, post):
#         self.__name = name
#         self.post = post
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         assert type(name) == str
#         self.__name = name
#
# ivan = Employee("Иванов Иван", "Программист")
# ivan.name = "1"
# print(ivan.get_name)


# class Goods:
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(
#             f'Name: {self.name}\nPrice: {self.price}
#         )
#
#     def set_name
#
# class Laptop(Goods):
#
#     def __init__(self, name, weight, price, os):
#         super().__init__(name, weight, price)
#         self.os = os
#
#     def print_info(self):
#         print(
#             f'Name: {self.name}\nPrice: {self.price}\nOS:{self.os}
#         )
#
#
# asus = Laptop("asus", 7, 55, "win10")
# print(asus)
# asus.print.info()

class loggingdict(dict):

    def __setitem__(self, key, value):
        print(f'key = {key} = {value}')
        super().__setitem__(key, value)

ld = loggingdict()
ld['a'] = "test"