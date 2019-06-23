# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

num1 = list(input("Введите первое 16-ичное число: "))
num2 = list(input("Введите второе 16-ичное число: "))

BASE_HEX_SYSTEM = 16

hex_to_int = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

int_to_hex = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}


def zfill_deque(deque1, deque2):
    len1 = len(deque1)
    len2 = len(deque2)
    if len1 < len2:
        for i in range(len2 - len1):
            deque1.appendleft('0')
    elif len2 < len1:
        for i in range(len1 - len2):
            deque2.appendleft('0')


def sum_hex_deque(num1_deque, num2_deque):
    zfill_deque(num1_deque, num2_deque)

    res_num = deque()

    remainder = 0
    for i in range(len(num1_deque)):
        int_sum_numbsers = hex_to_int[num1_deque.pop()] + hex_to_int[num2_deque.pop()] + remainder
        if int_sum_numbsers < BASE_HEX_SYSTEM:
            res_num.append(int_to_hex[int_sum_numbsers])
            remainder = 0
        else:
            remainder = int_sum_numbsers // BASE_HEX_SYSTEM
            res_num.append(int_to_hex[int_sum_numbsers % BASE_HEX_SYSTEM])
    if remainder > 0:
        res_num.append(int_to_hex[remainder])
    res_num.reverse()
    return res_num


def sum_hex(num1, num2):
    num1_deque = deque(num1)
    num2_deque = deque(num2)
    return sum_hex_deque(num1_deque, num2_deque)


def mul_hex(num1, num2):
    if len(num1) > len(num2):
        num1, num2 = num2, num1

    i = len(num1) - 1
    k = 0
    res_deque = deque()
    while i >= 0:
        interim_res_deque = deque()
        remainder = 0
        j = len(num2) - 1
        while j >= 0:
            mult = hex_to_int[num1[i]] * hex_to_int[num2[j]] + remainder
            if mult < BASE_HEX_SYSTEM:
                interim_res_deque.append(int_to_hex[mult])
                remainder = 0
            else:
                remainder = mult // BASE_HEX_SYSTEM
                interim_res_deque.append(int_to_hex[mult % BASE_HEX_SYSTEM])
            j -= 1
        if remainder > 0:
            interim_res_deque.append(int_to_hex[remainder])
        interim_res_deque.reverse()
        for _ in range(k):
            interim_res_deque.append('0')
        k += 1
        i -= 1
        res_deque = sum_hex_deque(res_deque, interim_res_deque)
    return res_deque


print('Сумма чисел: ', *sum_hex(num1, num2))
print('Произведение чисел: ', *mul_hex(num1, num2))
