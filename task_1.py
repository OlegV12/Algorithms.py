# Определить количество различных подстрок с использованием хеш-функции.
# Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib


def hash_substring(strng):
    result = []
    for i in range(len(strng)):
        for spam in range(i, len(strng) + 1):
            h_subs = [hashlib.sha1(strng[i:spam].encode('utf-8')).hexdigest()]
            if h_subs not in result and h_subs != [hashlib.sha1(''.encode('utf-8')).hexdigest()] and \
                    h_subs != [hashlib.sha1(strng.encode('utf-8')).hexdigest()]:
                result.append(h_subs)
    return len(result)


a = 'papa'
c = 'sova'
b = hash_substring(a)
d = hash_substring(c)

print(b, d, sep='\n')
