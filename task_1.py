# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.

# замеры делал с SIZE = 10000 / 100000 / 1000000

import random
import timeit
import cProfile

SIZE = 1000000


MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]


def min_numbers_1(arr):
    min_item_1 = arr[0]
    min_item_2 = arr[1]
    if min_item_2 > min_item_1:
        min_item_1, min_item_2 = min_item_2, min_item_1

    for item in arr:
        if item < min_item_1:
            min_item_2 = min_item_1
            min_item_1 = item
        elif item < min_item_2:
            min_item_2 = item
    return min_item_1, min_item_2


def min_numbers_2(arr):
    min1 = float('inf')
    min_ind1 = 0
    min2 = float('inf')
    for ind_1, elem in enumerate(arr):
        if elem < min1:
            min1 = elem
            min_ind1 = ind_1
    for ind_2, elem in enumerate(arr):
        if elem < min2 and ind_2 != min_ind1:
            min2 = elem
    return min1, min2


def min_numbers_3(arr):
    arr.sort()
    a = array[0]
    b = array[1]
    return a, b


print(timeit.timeit("min_numbers_1(array)", number=100, globals=globals()))
# 0.15761386800000002 / 1.5440556479999998 / 15.209805204

print(timeit.timeit("min_numbers_2(array)", number=100, globals=globals()))
# 0.29807752000000004 / 2.9722080259999997 / 29.293097115000002

print(timeit.timeit("min_numbers_3(array)", number=100, globals=globals()))
# 0.01618643200000003 / 0.16160388599999997 / 1.705487313000006

cProfile.run('min_numbers_1(array)')
# 1 0.001 0.001 0.001 0.001 task_1.py:18(min_numbers_1)
# 1 0.015 0.015 0.015 0.015 task_1.py: 18(min_numbers_1)
# 1 0.158 0.158 0.158 0.158 task_1.py:18(min_numbers_1)

cProfile.run('min_numbers_2(array)')
# 1    0.003    0.003    0.003    0.003 task_1.py:33(min_numbers_2)
# 1    0.031    0.031    0.031    0.031 task_1.py:33(min_numbers_2)
# 1    0.307    0.307    0.307    0.307 task_1.py:33(min_numbers_2)

cProfile.run('min_numbers_3(array)')
#  1    0.000    0.000    0.001    0.001 task_1.py:47(min_numbers_3)
#  1    0.000    0.000    0.000    0.000 task_1.py:47(min_numbers_3)
#  1    0.000    0.000    0.015    0.015 task_1.py:47(min_numbers_3)

# Вывод: вторая функция в 2 раза медленнее первой так как проходит массив 2 раза вместо одного
# 3 функция самая быстрая т.к. использует встроеную функцию сортировки  (почитал про Timsort на википедии)
