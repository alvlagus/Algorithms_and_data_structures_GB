"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
 число 3486, надо вывести 6843.

 Примечания:
В заданиях 2, 3, 4, 7, 8, 9 пользователь вводит только натуральные числа.
Попытайтесь решить задания без использования массивов в любых вариациях (массивы будут рассмотрены на следующем уроке).
Для простоты понимания любые квадратные скобки [ и ] считаются массивами и их наличие в коде расценивается как неверное
решение.
Договариваемся об идеальном пользователе, который вводит только верные данные, которые требует программа.
Проверка ввода не обязательна.
"""


def rotation(num):
    s = ''
    while num > 0:
        s = f'{s}{num % 10}'
        num //= 10
    return f'Обратное число введенному: {s}'


print(rotation(1234567890))

# Обратное число введенному: 0987654321
