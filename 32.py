# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
a = []
for i in range(10):
	a1 = int(random.randint(1, 100))  
	a.append(a1)
print(a)
	
 
minimum = int(input('Min: '))
maximum = int(input('Max: '))
 
b = []
i = 0
for i in a:
	if minimum <= i <= maximum:
		b.append(a.index(i))
print("Индексы: ", b)
