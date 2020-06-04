# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99

array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

print(array)


def bubble_sort(arr):
    """
    Функция сортировки пузырьком, доработана так, что если при проходе циклом по массиву,
    не произошло ни одной перестановки, массив считается отсортированным и функция завешает работу.
    :param arr: array
    :return: sorted array
    """
    n = 1
    spam = 0
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                spam += 1
            if i == len(arr) - n - 1 and spam == 0:
                return arr
        spam = 0
        n += 1
    return arr


a = bubble_sort(array)
print(a)
