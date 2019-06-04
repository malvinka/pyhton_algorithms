# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

min_value = array[MIN_ITEM]
index_min = MIN_ITEM
for i in range(SIZE):
    if min_value > array[i]:
        min_value = array[i]
        index_min = i

min_value_2 = array[MIN_ITEM] if index_min != MIN_ITEM else array[MIN_ITEM + 1]

for i in range(SIZE):
    if min_value_2 > array[i] and i != index_min:
        min_value_2 = array[i]

print(f'Исходный массив: {array}')
print(f'Минимальное число 1: {min_value}')
print(f'Минимальное число 2: {min_value_2}')
