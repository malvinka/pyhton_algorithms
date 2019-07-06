# Определение количества различных подстрок с использованием хеш - функции. Пусть на вход функции  дана строка. Требуется
# вернуть количество различных подстрок в этой строке.

import hashlib


def count_substr(input_str):
    substr_set = set()
    for i in range(len(input_str)):
        for j in range(i, len(input_str)):
            if not(i == 0 and (j + 1 == len(input_str))):
                substr_set.add(hashlib.sha1(input_str[i : j+1].encode("utf-8")).hexdigest())
    return len(substr_set)


target_str = input("Введите строку: ")
print("Разных подстрок в строке: ", count_substr(target_str))
