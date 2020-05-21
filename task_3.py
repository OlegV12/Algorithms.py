# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

print(array)

max_item = array[0]
max_item_ind = 0

min_item = array[0]
min_item_ind = 0
for ind, item in enumerate(array):
    if item >= max_item:
        max_item = item
        max_item_ind = ind
    elif item <= min_item:
        min_item = item
        min_item_ind = ind

print(f'Максимальное число {max_item}, с индексом {max_item_ind}')
print(f'Минимальное число {min_item}, с индексом {min_item_ind}')

array[min_item_ind] = max_item
array[max_item_ind] = min_item

print(array)
