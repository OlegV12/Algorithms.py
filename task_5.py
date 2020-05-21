# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.

import random

SIZE = 10

MIN_ITEM = -10
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

min_item_1 = array[0]
min_item_2 = array[1]

if min_item_2 > min_item_1:
    min_item_1, min_item_2 = min_item_2, min_item_1

for item in array:
    if item < min_item_1:
        min_item_2 = min_item_1
        min_item_1 = item
    elif item < min_item_2:
        min_item_2 = item

print(f'Числа: {min_item_1} и {min_item_2} минимальные в массиве:\n{array}')
