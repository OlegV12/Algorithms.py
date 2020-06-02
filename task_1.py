# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.


# Определить, какое число в массиве встречается чаще всего.

import random
import sys


def my_show(object_):
    size = [sys.getsizeof(object_)]
    if hasattr(object_, '__iter__'):
        if hasattr(object_, 'items'):
            for key, value in object_.items():
                size.append(sys.getsizeof(key))
                size.append(sys.getsizeof(value))
        elif not isinstance(object_, str):
            for item_ in object_:
                my_show(item_)
                size.append(sys.getsizeof(item_))
    return size


SIZE = 400
MIN_ITEM = 0
MAX_ITEM = 80
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

number_1 = 0
max_counter_1 = 0

for itm_1 in array:
    counter_1 = 0
    for item_1 in array:

        if item_1 == itm_1:
            counter_1 += 1

    if counter_1 >= max_counter_1:
        max_counter_1 = counter_1
        number_1 = itm_1

print(f'В массиве {array}\nчаще всего встречается число {number_1}, ({max_counter_1} раз(а))')

mx_num_2 = 0
mx_ind_2 = 0

for item_2 in array:
    new_array_2 = [_ for _, x in enumerate(array) if x == item_2]
    if len(new_array_2) > mx_ind_2:
        mx_ind_2 = len(new_array_2)
        mx_num_2 = item_2

print(f'число {mx_num_2}, встречается {mx_ind_2}')

eggs_3 = sorted(array)
spam_3 = {}

for item_3 in eggs_3:
    spam_3.setdefault(item_3, 0)
    spam_3[item_3] += 1

max_3 = max(spam_3, key=spam_3.get)

print(f'число {max_3}, встречается {spam_3[max_3]}')

result = {key: value for (key, value) in globals().items() if not key.startswith("__")}

result.pop('random')
result.pop('sys')
result.pop('my_show')

res_1 = {key: value for (key, value) in result.items() if key.endswith('1')}
res_2 = {key: value for (key, value) in result.items() if key.endswith('2')}
res_3 = {key: value for (key, value) in result.items() if key.endswith('3')}

print('*' * 50)
print(f'под все переменные выделено: {sum(my_show(result))}')  # 5863
print(f'под переменные в первом решении выделено: {sum(my_show(res_1))}')  # 372
print(f'под переменные во втором решении выделено: {sum(my_show(res_2))}')  # 363
print(f'под переменные в третьем решении выделено: {sum(my_show(res_3))}')  # 3363

#  Вывод: решения 1 и 2 примерно равны по объему выделяемой памяти, решение 3, используя словарь и
#  отсортированный список занимает наибольший объем памяти
