# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE = 10
ROWS_SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 100
array = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)],
         [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)],
         [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)],
         [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)],
         [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]]

min_elems = [array[0][i] for i in range(SIZE)]

for i in range(SIZE):
    for j in range(ROWS_SIZE):
        if min_elems[i] > array[j][i]:
            min_elems[i] = array[j][i]
    if i == 0 or max_elem < min_elems[i]:
        max_elem = min_elems[i]

print('Исходная матрица:')
for j in range(ROWS_SIZE):
    for i in range(SIZE):
        print(array[j][i], end=' ')
    print()

print('Минимальные элементы столбцов матрицы:')
print(min_elems)

print(f'Максимальны элемент среди минимальных в столбцах: {max_elem}')
