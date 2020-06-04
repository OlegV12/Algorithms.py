# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50

array = [random.random() * random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]


def merge(left_arr, right_arr):
    """
    Функция слияния двух отсортированных массивов в результирующий отсортированный массив
    :param left_arr: 1й массив
    :param right_arr: 2й массив
    :return: отсортированный массив
    """
    result = []
    left_ind = 0
    right_ind = 0
    # пока индексы не выйдут за предел одного из списков
    # берем по одному элементу из двух списков
    # добаляем в результирующий список наименьший элемент из сравниваемых,
    # переходим к следующему элементу увеличивая индекс
    while left_ind < len(left_arr) and right_ind < len(right_arr):
        if left_arr[left_ind] <= right_arr[right_ind]:
            result.append(left_arr[left_ind])
            left_ind += 1
        else:
            result.append(right_arr[right_ind])
            right_ind += 1
    # если мы дошли до конца первого списка то второй добавляется в результат целиком
    # и наоборот
    if left_ind == len(left_arr):
        for i in range(right_ind, len(right_arr)):
            result.append(right_arr[i])
    elif right_ind == len(right_arr):
        for i in range(left_ind, len(left_arr)):
            result.append(left_arr[i])

    return result


def my_split(arr):
    """
    Функция разбивания массива на 2 примерно равных
    :param arr: array
    :return: array[:middle], array[middle:]
    """
    list_len = len(arr)
    middle = list_len // 2
    return arr[:middle], arr[middle:]


def merge_sort(arr):
    """
    Функция сортировки слиянием
    :param arr: array
    :return: sorted array
    """
    if len(arr) <= 1:
        return arr
    else:
        left, right = my_split(arr)
        return merge(merge_sort(left), merge_sort(right))


a = merge_sort(array)
print(array)
print(a)
