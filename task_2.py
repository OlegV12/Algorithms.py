# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# так как именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

print(array)

res_array = []
for item in array:
    if item % 2 == 0:
        res_array.append(array.index(item))
print(res_array)
