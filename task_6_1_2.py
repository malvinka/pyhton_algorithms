# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import types
import sys
# import random

SIZE = 10
# MIN_ITEM = 0
# MAX_ITEM = 100
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array = [18, 1, 10, 29, 29, 74, 3, 22, 87, 14]

index_min = 0
min_value = array[index_min]
for i in range(SIZE):
    if min_value > array[i]:
        min_value = array[i]
        index_min = i

index_max = 0
max_value = array[index_max]
for i in range(SIZE):
    if max_value < array[i]:
        max_value = array[i]
        index_max = i

spam = []
if index_min < index_max:
    for i in range(index_min + 1, index_max):
        spam.append(array[i])
else:
    for i in range(index_max + 1, index_min):
        spam.append(array[i])

print(f'Исходный массив: {array}')
print(f'Сумма: {sum(spam)}')


def accumulate_variables_set(variables_set, variables_list):
    for elems in variables_list:
        variable = globals()[elems]
        if not elems.startswith('__') \
                and not isinstance(variable, types.ModuleType) \
                and not isinstance(variable, types.FunctionType):
            variables_set.add(elems)


def get_sum_memory(dir_list, locals_dict):
    variables = set()
    accumulate_variables_set(variables, dir_list)
    accumulate_variables_set(variables, locals_dict.keys())

    sum_memory = 0
    for variable_name in variables:
        spam = globals()[variable_name]
        if isinstance(spam, list):
            for elem in spam:
                sum_memory += sys.getsizeof(elem)
        sum_memory += sys.getsizeof(spam)
    return sum_memory

# ОС - Windows 8 x64
# Python - 3.7.3 x32
# Было выделено 452 байта памяти
# Модифицировала алгоритм, разделив в нем поиск наименьшего и наибольшего элемента массива, а также избавилась от присваивания:
# if index_min > index_max:
#     index_min, index_max = index_max, index_min
# Вместо этого выполняется проверка какой из индексов больше, какой меньше и с какого из них стоит начинать подсчет суммы в массиве.
# Однако на объем выделенной памяти все эти изменения не повлияли.
# Для того, чтобы добиться изменения объема занимаемой памяти добавила переменную spam типа list для хранения всех промежуточных
# элементов между минимальным и максимальным элементами списка. Использование промежуточного списка повлекло за собой
# существенный прирост используемой памяти.


if __name__ == '__main__':
    print(f'Было выделено памяти под алгоритм: {get_sum_memory(dir(), locals())} байт')