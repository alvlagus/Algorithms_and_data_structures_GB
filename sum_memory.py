""" 
Подсчитать, сколько было выделено памяти под переменные в
программах, разработанных на первых трех уроках.
Выберите 3 любые ваши программы для подсчёта. 
"""

import sys


def sum_memory(objects, verbose=True):
    sum_mem = 0
    for item in objects:
        if item.startswith('__'):
            # убираем магические функции
            continue
        elif hasattr(objects[item], '__call__'):
            # убираем функции
            continue
        elif hasattr(objects[item], '__loader__'):
            # убираем модули
            continue
        else:
            sum_mem += sys.getsizeof(objects[item])
            if verbose:
                print(f'Переменная = {item};\tкласс = {type(objects[item])};\tзначение = {objects[item]};'
                      f'\tзанимает {sys.getsizeof(objects[item])} байт(а)')
                
    return f'Переменные заняли {sum_mem} байт(а)'
