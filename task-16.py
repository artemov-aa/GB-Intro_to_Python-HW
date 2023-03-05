# Задача 16
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

print("\033[H\033[J", end="")

num_of_elements = int(input('Введите количество элементов в массиве: '))
min_element = int(input('Введите минимальное значение элементов массива: '))
max_element = int(input('Введите максимальное значение элементов массива: '))

list_1 = []
for i in range(num_of_elements):
    list_1.append(random.randint(min_element, max_element))

print(list_1)

num_X = int(input('Введите искомое число: '))

count = 0
for i in list_1:
    if i == num_X:
        count += 1

print(f'Число {num_X} встречается в массиве {count} раз')

print('\n')