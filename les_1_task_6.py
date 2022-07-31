'''
6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным
или равносторонним.

Примечание:
Договариваемся об идеальном пользователе, который вводит только верные данные, которые требует программа.
Проверка ввода не обязательна
'''

"""
Треугольник существует только тогда, когда сумма длин любых его двух сторон больше третьей стороны. 
Иначе две стороны просто «укладываются» на третьей.
Треугольник является разносторонним, если все его стороны имеют разную длину; треугольник будет равнобедренным, 
если любые две его стороны равны между собой, но отличны от третьей; и треугольник является равносторонним, 
когда все его стороны равны.
"""

a = float(input('Введите длину первого отрезка: '))
b = float(input('Введите длину второго отрезка: '))
c = float(input('Введите длину третьего отрезка: '))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Из указанных отрезков возможно составить равносторонний треугольник')
    elif a == b or a == c or b == c:
        print('Из указанных отрезков возможно составить равнобедренный треугольник')
    else:
        print('Из указанных отрезков возможно составить разносторонний треугольник')
else:
    print('Из указанных отрезков невозможно составить треугольник')

# Введите длину первого отрезка: 4
# Введите длину второго отрезка: 4
# Введите длину третьего отрезка: 6
# Из указанных отрезков возможно составить равнобедренный треугольник
