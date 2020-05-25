# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования решета Эратосфена;
# С использованием решета Эратосфена.
import itertools
import timeit
import cProfile


def prime_num(a):
    counter = 0
    while counter < a:
        for i in itertools.count(2):

            for j in range(2, i + 1):
                if i % j == 0 and i != j:
                    break
                elif i % j == 0 and i == j:
                    counter += 1
            if counter == a:
                return i


def sieve_func(num, n=1000):
    try:
        sieve = [item for item in range(n)]
        sieve[1] = 0

        for item in range(2, n):
            if sieve[item] != 0:
                k = item + item
                while k < n:
                    sieve[k] = 0
                    k += item

        res = [item for item in sieve if item != 0]
        result = res[num - 1]

        return result
    except IndexError:
        n += 1000
        return sieve_func(num, n)


w = prime_num(1000)
q = sieve_func(1000)

print(w, q)

print(timeit.timeit("prime_num(10)", number=100, globals=globals()))  # 0.007315887999999937
print(timeit.timeit("prime_num(100)", number=100, globals=globals()))  # 0.7552745570000001
print(timeit.timeit("prime_num(1000)", number=100, globals=globals()))  # 123.15882781500001

print(timeit.timeit("sieve_func(10)", number=100, globals=globals()))  # 0.08253115300000502
print(timeit.timeit("sieve_func(100)", number=100, globals=globals()))  # 0.08032028399999547
print(timeit.timeit("sieve_func(1000)", number=100, globals=globals()))  # 3.2133929059999957

cProfile.run('prime_num(10)')    # 1    0.000    0.000    0.000    0.000 task_2.py:9(prime_num)
cProfile.run('prime_num(100)')   # 1    0.007    0.007    0.007    0.007 task_2.py:9(prime_num)
cProfile.run('prime_num(1000)')  # 1    1.294    1.294    1.294    1.294 task_2.py:9(prime_num)

cProfile.run('sieve_func(10)')      # 1    0.001    0.001    0.001    0.001 task_2.py:25(sieve_func)
cProfile.run('sieve_func(100)')     # 1    0.001    0.001    0.001    0.001 task_2.py:25(sieve_func)
cProfile.run('sieve_func(1000)')  # 8/1    0.029    0.004    0.036    0.036 task_2.py:25(sieve_func)


# Вывод: функция с решетом Эратосфена эффективнее особенно если необходимо найти простые
# числа с большим порядковым номером
