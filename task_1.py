# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = [i for i in range(2, 99)]
b = [i for i in range(2, 10)]

for item_b in b:
    counter = 0
    for item_a in a:
        if item_a % item_b == 0:
            counter += 1
    print(f'Числу {item_b} кратны {counter} чисел диапазона от 2 до 99')

print(a)
print(b)
