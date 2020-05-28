# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


def equal_len(lst1, lst2):
    """
    Функция выравнивает длину списков.
    :param lst1: list
    :param lst2: list
    :return: list, list
    """
    if len(lst1) > len(lst2):
        while len(lst1) != len(lst2):
            lst2.appendleft('0')
    elif len(lst1) < len(lst2):
        while len(lst1) != len(lst2):
            lst1.appendleft('0')
    return lst1, lst2


def list_sum(list1, list2):
    """
    Функция суммирует два списка по элементам и возвращает список.
    :param list1: list
    :param list2: list
    :return: list
    """
    result_ = deque()
    for x, y in zip(reversed(list1), reversed(list2)):
        result_.appendleft(int(x, base=16) + int(y, base=16))
    return result_


def sum_list_to_hex(lst):
    """
    Функция переводит список(результат от сложения 2х списков) в список шестнадцатиричных чисел.
    :param lst: list
    :return: list
    """
    lst.reverse()
    for ind, item in enumerate(lst):
        if item > 15:
            try:
                lst[ind + 1] += item // 16
            except IndexError:
                lst.append(item // 16)
                lst[ind] = item % 16
                break
            lst[ind] = item % 16
    lst.reverse()

    for ind, itm in enumerate(lst):
        lst[ind] = hex(itm)[2:].upper()
    return lst


def mul_func(num, lst):
    """
    Функция перемножает число num с каждым элементом списка lst.
    :param num: int
    :param lst: list
    :return: list
    """
    mul_result = deque([])
    num = int(num, base=16)
    for i in lst:
        e = num * int(i, base=16)
        mul_result.append(e)
    return mul_result


user_num1 = input('Введите первое шестнадцатиричное число ')
a = deque(list(user_num1))

user_num2 = input('Введите второе шестнадцатиричное число ')
b = deque(list(user_num2))
print(*a)
print(*b)

if len(a) < len(b):
    a, b = b, a

res = []
counter = len(b) - 1
for _ in b:
    v = mul_func(_, a)
    for u in range(counter):
        v.append(0)

    res.append(v)
    counter -= 1


for ind, _ in enumerate(res):
    res[ind] = sum_list_to_hex(_)

for ind, _ in enumerate(res):
    equal_len(res[ind], res[ind - 1])

final = [0 for i in range(len(res[0]))]
for i in range(len(res)):
    final = list_sum(sum_list_to_hex(final), res[i])
final = sum_list_to_hex(final)
print('Произведение чисел: ')
print(*final)

print("*" * 20)

equal_len(a, b)
res = list_sum(a, b)
result = sum_list_to_hex(res)
print('Сумма чисел: ')
print(*result)
