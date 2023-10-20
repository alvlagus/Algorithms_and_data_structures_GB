
def get_primes(n):
	
    lst=[2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i%10==5):
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst

# print(get_primes(40))

"""
1000 loops, best of 5: 14.9 usec per loop 40
1000 loops, best of 5: 52.3 usec per loop 100
1000 loops, best of 5: 275 usec per loop 400
1000 loops, best of 5: 141 msec per loop 65000

"""