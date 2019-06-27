# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10


def bubble_sorting(array):
    n = 1
    while n < len(array):
        change = None
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                change = True
        if change is None:
            break
        n += 1


sorted_array = [random.randrange(-100, 100) for x in range(SIZE)]
print('Исходный массив: ', sorted_array)
bubble_sorting(sorted_array)
print('Отсортированный массив: ', sorted_array)