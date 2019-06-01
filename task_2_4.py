# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.


def gen_seq(n):
    if n == 0:
        return 1
    else:
        return gen_seq(n - 1) + (-1) ** n * (1.5 / 2 ** (n - 1))


n = int(input("Введите число n: "))

res_sum = 0

for i in range(n):
    res_sum += gen_seq(i)

print(res_sum)
