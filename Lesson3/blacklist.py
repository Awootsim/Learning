# data = [
#     [1, 2, 3, 4, 5, 6, 7],
#     [-1, -2, -3, -4, -5, -6, -7],
#     [99, 56, 209, -308, -12, -18, 42],
#     [-1, -2, -3, 0, 1, 2, 3],
# ]
# min_elem = min(data[2])
# max_elem = max(data[2])
# sum_list = sum(data[2])
# average = sum(data[2]) / len(data[2])
# print(min_elem, max_elem, sum_list, average)

# data = [
#     [1, 2, 3, 4, 5, 6, 7],
#     [-1, -2, -3, -4, -5, -6, -7],
#     [99, 56, 209, -308, -12, -18, 42],
#     [-1, -2, -3, 0, 1, 2, 3],
# ]
# print(sum(data[0][::2]))

data = [
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    ['н', 'л', 'о', 'с']
]

# a = data[1][0]
# b = data[1][-1]
# data[1][-1] = a
# data[1][0] = b
# lst = data[1]

change = data[0][0], data[0][-1]
data[0][-1], data[0][0] = change
lst1 = data
print(lst1)