# Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

max_num = 0
digit_sum = 0
user_num = -1


def digits(num, dgt_sum=0):
    """Функция принимает натуральное число и возвращает сумму его цифр"""
    if num == 0:
        return dgt_sum
    else:
        last_dgt = round(num % 10)
        dgt_sum = dgt_sum + last_dgt
        num = (num - last_dgt) / 10
        return digits(num, dgt_sum)


while user_num != 0:
    user_num = int(input('Введите натуральное число (0 - для звершения ввода): '))
    a = digits(user_num)
    if a > digit_sum:
        digit_sum = a
        max_num = user_num
    else:
        continue
else:
    print(f'Число: {max_num}, имеет наибольшую сумму цифр: {digit_sum}')
