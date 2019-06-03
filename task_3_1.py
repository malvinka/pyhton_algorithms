# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

count_multiples = [0, 0, 0, 0, 0, 0, 0, 0]

for num in range(2, 99):
    if num % 2 == 0:
        count_multiples[0] += 1
    if num % 3 == 0:
        count_multiples[1] += 1
    if num % 4 == 0:
        count_multiples[2] += 1
    if num % 5 == 0:
        count_multiples[3] += 1
    if num % 6 == 0:
        count_multiples[4] += 1
    if num % 7 == 0:
        count_multiples[5] += 1
    if num % 8 == 0:
        count_multiples[6] += 1
    if num % 9 == 0:
        count_multiples[7] += 1

for i in range(7):
    print(f'Цифра {i + 2} встречается {count_multiples[i]} раз')
