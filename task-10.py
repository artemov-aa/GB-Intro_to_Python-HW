# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

print("\033[H\033[J", end="")

num_of_coins = int(input('Введите количество монеток: '))

num_of_heads = 0

# Кидаем num_of_heads монеток
for i in range(num_of_coins):
    # Считаем количество выпавших "орлов"
    num_of_heads += random.randint(0, 1)

num_of_tails = num_of_coins - num_of_heads

if num_of_heads >= num_of_tails:
    min_num = num_of_tails
else:
    min_num = num_of_heads

print(f'Количество монет, лежащих вверх решкой - {num_of_tails}, а вверх орлом - {num_of_heads}')
print(f'Минимальное количество монет, которое необходимо перевернуть - {min_num}')

print('\n')