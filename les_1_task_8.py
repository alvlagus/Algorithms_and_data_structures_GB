'''
8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

Примечание:
Договариваемся об идеальном пользователе, который вводит только верные данные, которые требует программа.
Проверка ввода не обязательна.
'''
print('Введите три разных числа')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

n = a

if n < b and n < c:
    if b < c:
        n = b
    else:
        n = c
else:
    if n > b and n > c:
        if b > c:
            n = b
        else:
            n = c

print(f'Среднее число из трёх: {n}')

# Введите три разных числа
# Введите первое число: 1
# Введите второе число: 5
# Введите третье число: 7
# Среднее число из трёх: 5
