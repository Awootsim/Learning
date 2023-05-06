a = 45
b = 9.1
c = '2'
d = 5
e = -2

# print(a, b, c, type(a), type(b), type(c))

# print(a + b)  # Сложение
# print(a * b)  # Умножение
# print(a ** b)  # Степень
# print(a - b)  # Вычитание
# print(a / b)  # Деление

# print(d % e)  # Деление с получением в результате остатка
# print(d // e)  # Деление целочисленное


a1 = 1
a2 = 2
a3 = 3

print(a1 + a2 * a3 ** a1 * (a1 + a2))

# Сокращенные операторы
# b += a  # Сложение
b -= a  # Вычитание
print(b)
# b *= a  # Умножение
# b /= a  # Деление
# b **= a  # Степень
# b %= a  # Деление с получением в результате остатка
# b //= a  # Деление целочисленное

a4 = int(7.3)
a5 = round(7.49)
print(a4)
print(a5)

string1 = "Амогус\n"
print(string1)

string2 = """
Амогус
Амогус
Амогус
Амогус \"Слова\"
"""
print(string2)

string3 = ("Слова "
           "Могут "
           "Убить")
print(string3)

string4 = "Много слов \nсвидетельствует об обилии слов"
print(string4)

string5 = r'C:\python\name'
print(string5)
print(string5 + string3)
print(string1 * 12)
print(string1[0] * 2)
print(string1[0:6] * 2)
my_org = "ООО Амонгас среди нас"
print(my_org[-2:-1])
print("Евреи " + my_org[-9:])
print(my_org[0:200])
print(len("10"))
c6 = str(2)
c7 = c6 + "2"
print(c7, type(c7))

c8 = int(2345)
print(c8, type(c8))

print(my_org.replace("Амонгас", "Негры"))
print(my_org)
my_org_new = my_org.replace("Амонгас", "Негры")
print(my_org_new)
my_org_new_2 = my_org_new.replace("е", "")
print(my_org_new_2)

aa = "Пришёл! ответ от правоохранительных !органов по поводу преподавателя трансгендера в ВШЭ."
print(aa.upper())
print(aa.isdigit())
print(aa.isalpha())
print(aa.startswith("Пришёл"))
print(aa.split("а"))

my_org1 = "Копатель"
address = "Проезд копателя"
boss = "Макарович"

org = f"Организация %s находится по адресу %s. Ее начальник %s." %(my_org1, address, boss)
print(org)
org2 = "Организация {0} находится по адресу {2}. Ее начальник {0}." .format(my_org1, boss, boss)
print(org2)
