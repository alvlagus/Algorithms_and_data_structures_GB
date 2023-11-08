""" 
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). 
Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. 
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random

def bubble_sort(array, reverse=False):
    """ 
    приводим логическое значение reverse к целому типу. Если True - получаем 1, 
    если False, то получаем 0. 
    """    
    sing = int(reverse) * 2 - 1 
    pos = 1
    
    while pos < len(array):
        is_sorted = True 
        
        for i in range(len(array) - pos):
            if array[i] * sing < array[i + 1] * sing: 
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
                
        if is_sorted:
            break
        
        pos += 1
        

# константы для генерации массива        
SIZE = 42
LIMIT = 100
data = [random.randrange(-LIMIT, LIMIT) for i in range(SIZE)] # генерация массива
print(data)
bubble_sort(data, reverse=True)
print(data)

""" 
[71, -25, 30, -58, -29, -37, -26, -58, 56, 68, 64, 42, 1, -15, 97, -80, -51, -76, -62, -79, -92, 74, -50, 39, -87, -98, -59, -65, -3, 84, 83, 14, -61, 36, -21, -28, 54, 5, 42, 19, 93, -45]
[97, 93, 84, 83, 74, 71, 68, 64, 56, 54, 42, 42, 39, 36, 30, 19, 14, 5, 1, -3, -15, -21, -25, -26, -28, -29, -37, -45, -50, -51, -58, -58, -59, -61, -62, -65, -76, -79, -80, -87, -92, -98]
"""
