# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

a = [0] * 8

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            a[j - 2] += 1

# for i, item in enumerate(a, start=2):
#     print(f'Числу {i} кратно {item} чисел')

# 1000 loops, best of 5: 16.8 nsec per loop
    