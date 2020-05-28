# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

from collections import Counter

a = Counter({})
q = 0
num = int(input('Ввдеите количество предприятий '))

while q < num:
    q += 1
    company_name = input('введите название предприятия ')
    first_quarter = float(input('ввелите прибыль за 1й квартал '))
    second_quarter = float(input('ввелите прибыль за 2й квартал '))
    third_quarter = float(input('ввелите прибыль за 3й квартал '))
    forth_quarter = float(input('ввелите прибыль за 4й квартал '))
    a[company_name] = (first_quarter + second_quarter + third_quarter + forth_quarter) / 4

print(a)
print(f'Средняя прибыль предприятий {sum(a.values()) / num}')

lower = []
higher = []

for _ in a:
    if a[_] < sum(a.values()) / num:
        lower.append(_)
    elif a[_] > sum(a.values()) / num:
        higher.append(_)
print(f'предприятия с прибылью ниже среднего {lower},\nвыше сденего {higher}')
