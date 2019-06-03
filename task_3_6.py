# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

index_min, index_max = 0, 0
min_value, max_value = array[index_min], array[index_max]
for i in range(SIZE):
    if min_value > array[i]:
        min_value = array[i]
        index_min = i
    if max_value < array[i]:
        max_value = array[i]
        index_max = i

print(index_min, index_max)
if index_min > index_max:
    index_min, index_max = index_max, index_min

sum_value = 0
for i in range(index_min+1, index_max):
    sum_value += array[i]

print(f'Исходный массив: {array}')
print(f'Сумма: {sum_value}')
