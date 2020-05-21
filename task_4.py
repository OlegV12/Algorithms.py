# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 15

MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]


number = 0
max_counter = 0
for i in array:
    counter = 0
    for item in array:
        if item == i:
            counter += 1
    if counter >= max_counter:
        max_counter = counter
        number = i
print(f'В массиве {array}\nчаще всего встречается число {number}, ({max_counter} раз(а))')
