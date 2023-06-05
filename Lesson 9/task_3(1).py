# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
def find_three_most_expensive_purchases(filename):
    """
    Программа находит сумму 3-х самых дорогих покупок
    :param filename: путь к файлу с данными
    :return: сумма 3-х самых дорогих покупок
    """
    with open(filename, 'r') as file:
        purchases = file.read().split('\n\n')

    prices = []
    for purchase in purchases:
        purchase_prices = [float(price) for price in purchase.strip().split('\n')]
        prices.extend(purchase_prices)
        purchase_sum = sum(purchase_prices)
        prices.append(purchase_sum)


    prices.sort(reverse=True)
    three_most_expensive_purchases = sum(prices[:3])

    return three_most_expensive_purchases

filename = 'test_file/task_3.txt'
three_most_expensive_purchases = find_three_most_expensive_purchases(filename)

assert three_most_expensive_purchases == 202346
