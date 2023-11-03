"""
Задаём до какого числа будем получать простые числа
"""

from sum_memory import sum_memory
from collections import namedtuple

QUARTERS = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input("Введите количество предприятий: "))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Введите название предприятия {i}: ')
    
    for j in range(QUARTERS):
        quarters.append(int(input(f'Прибыль за {j + 1}-й квартал: ')))
        profit += quarters[j]
        
    comp = Company(name=name, quarters=tuple(quarters), profit=profit)
    all_companies.add(comp)
    total_profit += profit
    
average = total_profit / num

print(f'\nСредняя прибыль = {average}')

print(f'\nПредприятия с прибылью выше среднего: ')
for comp in all_companies:
    if comp.profit > average:
        print(f'Компания {comp.name} заработала {comp.profit}')
        
print(f'\nПредприятия с прибылью ниже среднего: ')
for comp in all_companies:
    if comp.profit < average:
        print(f'Компания {comp.name} заработала {comp.profit}')

print(sum_memory(locals(), verbose=True))

"""
Введите количество предприятий: 3
Введите название предприятия 1: aaa
Прибыль за 1-й квартал: 1000
Прибыль за 2-й квартал: 1200
Прибыль за 3-й квартал: 600
Прибыль за 4-й квартал: 1500
Введите название предприятия 2: bbb
Прибыль за 1-й квартал: 1500
Прибыль за 2-й квартал: 2000
Прибыль за 3-й квартал: 300
Прибыль за 4-й квартал: 1500
Введите название предприятия 3: ccc
Прибыль за 1-й квартал: 520
Прибыль за 2-й квартал: 1256
Прибыль за 3-й квартал: 3245
Прибыль за 4-й квартал: 5214

Средняя прибыль = 6611.666666666667

Предприятия с прибылью выше среднего: 
Компания ccc заработала 10235

Предприятия с прибылью ниже среднего: 
Компания bbb заработала 5300
Компания aaa заработала 4300
Переменная = QUARTERS;  класс = <class 'int'>;  значение = 4;   занимает 28 байт(а)
Переменная = all_companies;     класс = <class 'set'>;  значение = {Company(name='bbb', quarters=(1500, 2000, 300, 1500), profit=5300), Company(name='ccc', quarters=(520, 1256, 3245, 5214), profit=10235), Company(name='aaa', quarters=(1000, 1200, 600, 1500), profit=4300)};        занимает 216 байт(а)
Переменная = num;       класс = <class 'int'>;  значение = 3;   занимает 28 байт(а)
Переменная = total_profit;      класс = <class 'int'>;  значение = 19835;       занимает 28 байт(а)
Переменная = i; класс = <class 'int'>;  значение = 3;   занимает 28 байт(а)
Переменная = profit;    класс = <class 'int'>;  значение = 10235;       занимает 28 байт(а)
Переменная = quarters;  класс = <class 'list'>; значение = [520, 1256, 3245, 5214];     занимает 88 байт(а)
Переменная = name;      класс = <class 'str'>;  значение = ccc; занимает 52 байт(а)
Переменная = j; класс = <class 'int'>;  значение = 3;   занимает 28 байт(а)
Переменная = comp;      класс = <class '__main__.Company'>;     значение = Company(name='aaa', quarters=(1000, 1200, 600, 1500), profit=4300);  занимает 64 байт(а)
Переменная = average;   класс = <class 'float'>;        значение = 6611.666666666667;   занимает 24 байт(а)
Переменные заняли 612 байт(а)
"""