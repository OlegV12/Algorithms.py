# Найти сумму и произведение цифр введённого пользователем трехзначного числа.
# https://drive.google.com/file/d/11R2UgAUpJkJXzZBVy7VNwdetTc7UKIWR/view?usp=sharing

a = int(input("ведите трехзначное число "))

x = a % 10
y = round(((a - x) % 100) / 10)
z = round((a - x - 10 * y) / 100)
num_sum = x + y + z
num_mul = x * y * z

print(f"ваше число {a}, сумма цифр {num_sum}, произведение цифр {num_mul}")

"""
есть решение через индекс строки, но оно наверное не подойдет
т.к. вы сказали, что нельзя использовать прямые скобки в коде.


a = input("введите число ")
x = int(a[0])
y = int(a[1])
z = int(a[2])
print(f"ваше число {a}, сумма цифр {x + y + z}, произведение цифр {x * y * z}")

"""
