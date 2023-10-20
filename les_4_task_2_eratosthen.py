"""
Задаём до какого числа будем получать простые числа
"""
def eratosthen(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):

        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    return result

print(eratosthen(40))

"""
1000 loops, best of 5: 19.4 usec per loop 40
1000 loops, best of 5: 51.6 usec per loop 100
1000 loops, best of 5: 3.31 msec per loop 400
1000 loops, best of 5: 52.8 msec per loop 65000
"""