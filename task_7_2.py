# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
from collections import deque
from itertools import islice

SIZE = 10


def get_sorted(left_deque, right_deque):
    if len(left_deque) == 1 and len(right_deque) == 1:
        left_elem = left_deque.pop()
        right_elem = right_deque.pop()
        if left_elem < right_elem:
            return deque([left_elem, right_elem])
        else:
            return deque([right_elem, left_elem])
    else:
        len_left_array = len(left_deque) // 2
        len_right_array = len(right_deque) // 2
        if len_left_array >= 1:
            left_deque = get_sorted(deque(islice(left_deque, len_left_array)),
                                    deque(islice(left_deque, len_left_array, len(left_deque))))
        if len_right_array >= 1:
            right_deque = get_sorted(deque(islice(right_deque, len_right_array)),
                                     deque(islice(right_deque, len_right_array, len(right_deque))))

        left_elem = left_deque.popleft()
        right_elem = right_deque.popleft()
        res = deque()
        while left_elem and right_elem:
            if left_elem < right_elem:
                res.append(left_elem)
                left_elem = left_deque.popleft() if len(left_deque) > 0 else None
            else:
                res.append(right_elem)
                right_elem = right_deque.popleft() if len(right_deque) > 0 else None
        if left_elem:
            res.append(left_elem)
            res.extend(left_deque)
        if right_elem:
            res.append(right_elem)
            res.extend(right_deque)
        return res


def merge_sorting(array):
    if len(array) == 1:
        return array
    else:
        len_array = len(array) // 2
        return get_sorted(deque(islice(array, len_array)), deque(islice(array, len_array, len(array))))


sorted_array = [random.random() * 50 for x in range(SIZE)]
print('Исходный массив: ', sorted_array)
print('Отсортированный массив: ', merge_sorting(sorted_array))
