# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках.

import random

m = 10
MIN_ITEM = 0
MAX_ITEM = 5
my_array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(2 * m + 1)]

print(my_array)


def median(array):
    """
    Функция нахождения медианы по количеству бОльших, меньших и равных элементов в массиве
    :param array: array
    :return: медианное число
    """
    for eggs in array:
        left = 0
        right = 0
        equal = 0
        arr = array.copy()
        arr.remove(eggs)
        for spam in arr:
            if eggs > spam:
                left += 1
            elif eggs < spam:
                right += 1
            else:
                equal += 1
        if left + equal == right or left == right + equal or abs(left - right) <= equal:
            return eggs


x = median(my_array)
print(f'Медианное число: {x}')
print(f'для проверки - отсортированный массив:\n{sorted(my_array)}')
