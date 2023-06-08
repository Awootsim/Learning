# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
filename = 'test_file/task_3.txt'
with open(filename, 'r') as file:
    purchases = file.readlines()

prices = []
purchase = []
for line in purchases:
    if line.strip():
        price = float(line.strip())
        purchase.append(price)
        prices.append(price)
    else:
        purchase_sum = sum(purchase)
        prices.append(purchase_sum)
        purchase = []

prices.sort(reverse=True)
three_most_expensive_purchases = sum(prices[:3])

assert three_most_expensive_purchases == 202346
