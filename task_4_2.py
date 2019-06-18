# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
# вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

import cProfile

# i = int(input("Введите номер простого числа: "))


# 100 loops, best of 5: 919 nsec per loop - n = 1
# 100 loops, best of 5: 32.6 usec per loop - n = 10
# 100 loops, best of 5: 2.61 msec per loop - n = 100
# 100 loops, best of 5: 363 msec per loop - n = 1000
# cProfile
# 1    0.000    0.000    0.000    0.000 task_4_2.py:14(get_prime_number_divsion) - n = 1
# 1    0.000    0.000    0.000    0.000 task_4_2.py:16(get_prime_number_divsion) - n = 10
# 1    0.003    0.003    0.003    0.003 task_4_2.py:17(get_prime_number_divsion) - n = 100
# 1    0.367    0.367    0.367    0.367 task_4_2.py:18(get_prime_number_divsion) - n = 1000
# Обычный алгоритм
def get_prime_number_divsion(k):
    count = 0
    i = 2
    end_loop = k if k > i else i
    while i <= end_loop:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            if count == k:
                return i
        if i == end_loop:
            end_loop = end_loop * 2
        i += 1


# Решето Эратосфена
def get_prime_number_by_sive(k, sieve):
    upper_bound = len(sieve)

    if upper_bound > 1:
        sieve[1] = 0
        count = 0

        for i in range(2, upper_bound):
            if sieve[i] != 0:
                count += 1
                if count == k:
                    return sieve[i]
                j = i + i
                while j < upper_bound:
                    sieve[j] = 0
                    j += i


def get_prime_number(k, sieve):
    prime_number = get_prime_number_by_sive(k, sieve)
    if prime_number is None:
        len_sieve = len(sieve)
        sieve = [i for i in range(2*len_sieve + 1)]
        prime_number = get_prime_number(k, sieve)
    if prime_number is not None:
        return prime_number


# 100 loops, best of 5: 2.63 usec per loop - n = 1
# 100 loops, best of 5: 28 usec per loop - n = 10
# 100 loops, best of 5: 679 usec per loop - n = 100
# 100 loops, best of 5: 7.95 msec per loop - n = 1000
# cProfile
#  1    0.000    0.000    0.000    0.000 task_4_2.py:39(get_prime_number_by_sive) - n = 1
#  1    0.000    0.000    0.000    0.000 task_4_2.py:57(get_prime_number)
#  1    0.000    0.000    0.000    0.000 task_4_2.py:87(get_prime_number_sieve)
# ------------------------------------------------------------------------------
# 2    0.000    0.000    0.000    0.000 task_4_2.py:39(get_prime_number_by_sive) - n = 10
# 2/1    0.000    0.000    0.000    0.000 task_4_2.py:57(get_prime_number)
# 1    0.000    0.000    0.000    0.000 task_4_2.py:87(get_prime_number_sieve)
# ------------------------------------------------------------------------------
# 3    0.001    0.000    0.001    0.000 task_4_2.py:39(get_prime_number_by_sive) - n = 100
# 3/1    0.000    0.000    0.001    0.001 task_4_2.py:57(get_prime_number)
# 1    0.000    0.000    0.001    0.001 task_4_2.py:87(get_prime_number_sieve)
# ------------------------------------------------------------------------------
#  3    0.008    0.003    0.008    0.003 task_4_2.py:39(get_prime_number_by_sive) - n = 1000
# 3/1    0.000    0.000    0.008    0.008 task_4_2.py:57(get_prime_number)
#  1    0.000    0.000    0.009    0.009 task_4_2.py:87(get_prime_number_sieve)
def get_prime_number_sieve(i):
    sieve = [x for x in range(i*2 + 1)]
    return get_prime_number(i, sieve)


cProfile.run("get_prime_number_sieve(1)")

# print(get_prime_number_sieve(i))

# Вывод: поиск простых чисел при использовании алгоритма решето Эратосфена работает быстрее при правильно подобранной
# длине последовательности чисел, поскольку обычный алгоритм близок к сложности О(n**2), т.к. выполняет правктически
# два полных перебора в цикле, а алгоритм, реализующий алгоритм решето Эратосфена, выполняет не полный перебор,
# а перебор с шагом i во внутреннем цикле и только по ненулевым элементам во внешнем цикле, что существенно снижает
# его сложность.
