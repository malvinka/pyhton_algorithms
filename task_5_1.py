# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import deque

n = int(input("Введите количество предприятий: "))

enterprises = {}

i = 0
while i < n:
    name = input("Имя предприятия: ")
    profits = deque()
    for j in range(4):
        profits.append(int(input(f"Прибыль предприятия за квартал {j + 1}: ")))
    enterprises[name] = profits
    i += 1

total_profit = 0
enterprises_profits = {}

for name, profits_list in enterprises.items():
    profit_sum = sum(profits_list)
    total_profit += profit_sum
    enterprises_profits[name] = profit_sum

avg_profit = total_profit / n

lower_profit_enterprises, more_profit_enterprises = deque(), deque()
for name, enterprise_profit in enterprises_profits.items():
    if enterprise_profit > avg_profit:
        more_profit_enterprises.append(name)
    elif enterprise_profit < avg_profit:
        lower_profit_enterprises.append(name)

print(f'Средняя прибыль для всех предприятий: {avg_profit}')
print('Предприятия с прибылью выше среднего: ', *more_profit_enterprises)
print('Предприятия с прибылью ниже среднего: ', *lower_profit_enterprises)
