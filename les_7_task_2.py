""" 
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.
"""

import random

def merge_sort(array):
    
    # базовый случай
    if len(array) == 1:
        return array
    
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
            return array
    
    """
    формируем 2 части массива.  left принимает отсортированную часть массива
    от начала до середины. right от середины до конца.   
    """
    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
        
    i, j = 0, 0    
    
    while len(left) > i and len(right) > j:
        
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
            
        else:
            array[i + j] = right[j]
            j += 1
    
    while len(left) > i:        
        array[i + j] = left[i]
        i += 1
        
    while len(right) > j:
        array[i + j] = right[j]
        j += 1
        
    return array


SIZE = 16
LIMIT = 50
data = [round(random.uniform(0, LIMIT), 3) for i in range(SIZE)]
print(data)
merge_sort(data)
print(data)
            
""" 
[13.005, 29.607, 43.408, 44.135, 14.841, 30.031, 12.736, 33.853, 43.67, 37.186, 33.903, 8.904, 16.725, 45.715, 26.712, 20.235]
[8.904, 12.736, 13.005, 14.841, 16.725, 20.235, 26.712, 29.607, 30.031, 33.853, 33.903, 37.186, 43.408, 43.67, 44.135, 45.715]
"""            
