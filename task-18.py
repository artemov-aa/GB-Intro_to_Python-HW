# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

print("\033[H\033[J", end="")

num_of_elements = int(input('Введите количество элементов в массиве: '))
min_element = int(input('Введите минимальное значение элементов массива: '))
max_element = int(input('Введите максимальное значение элементов массива: '))

list_1 = []
for i in range(num_of_elements):
    list_1.append(random.randint(min_element, max_element))

print(list_1)

num_X = int(input('Введите заданное число: '))
elem_1 = elem_2 = num_X - list_1[0]
for i in range(1, num_of_elements):
    if (num_X - list_1[i]) < elem_1:
        