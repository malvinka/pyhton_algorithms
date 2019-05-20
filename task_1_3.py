# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

x1 = int(input("Введите координату x1: "))
y1 = int(input("Введите координату y1: "))

x2 = int(input("Введите координату x2: "))
y2 = int(input("Введите координату y2: "))

if x1 - x2 == 0:
    k = y1 - y2
    b = y2 * x1 - y1 * x2
else:
    k = (y1 - y2) / (x1 - x2)
    b = (y2 * x1 - y1 * x2) / (x1 - x2)

if k == 0:
    if b == 0:
        print('Уравнения прямой не существует')
    else:
        print('y = {}'.format(b))
elif b == 0:
    print('y = {}x'.format(k))
elif b > 0:
    print('y = {}x + {}'.format(k, b))
else:
    print('y = {}x {}'.format(k, b))