# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума) [5..15]
n = int(input('Введите размер массива: '))

import random
list_1 = []
for i in range(n):
    list_1.append(random.randint(-10, 20))
print(list_1)

list_2 = []
for i in range(len(list_1)-1):
    if 5 <= list_1[i] <= 15:
        list_2.append(i)
print(list_2)