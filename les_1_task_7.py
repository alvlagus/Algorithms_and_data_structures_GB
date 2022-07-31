'''
7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

Примечание:
Договариваемся об идеальном пользователе, который вводит только верные данные, которые требует программа.
Проверка ввода не обязательна
'''

"""
Распределение високосных годов:
год, номер которого кратен 400, — високосный;
остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
остальные годы, номер которых кратен 4, — високосные[5].
все остальные годы — невисокосные.
"""

year = int(input('Введите номер года: '))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print(f'Введенный {year}-й год не является високосным')
else:
    print(f'Введенный {year}-й год является високосным')

# Введите номер года: 1764
# Введенный 1764-й год является високосным

# Введите номер года: 1800
# Введенный 1800-й год не является високосным
